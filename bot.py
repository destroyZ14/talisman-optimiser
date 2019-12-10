import os
import discord
import skypy
from skypy import SkyblockError
import traceback
from itertools import product

from dotenv import load_dotenv

load_dotenv()

notnotmelon = 270352691924959243
api_key = os.getenv('API_KEY')

damaging_potions = [
    {'name': 'critical', 'stats': {'crit chance': [0, 10, 15, 20, 25], 'crit damage': [0, 10, 20, 30, 40]}},
    {'name': 'strength', 'stats': {'strength': [0, 5.25, 13.125, 21, 31.5, 42, 52.5, 63, 78.75]}},  # Assume cola
    {'name': 'spirit', 'stats': {'crit damage': [0, 10, 20, 30, 40]}}
    # 'archery': irrelevant since it multiplies afterwards everything else
]

relavant_reforges = {
    'forceful': (None, None, (7, 0, 0), (10, 0, 0), (15, 0, 0)),
    'itchy': ((1, 0, 3), (2, 0, 5), (2, 0, 8), (3, 0, 12), (5, 0, 15)),
    # 'unpleasant': ((0, 1, 1), None, (0, 3, 2), (0, 6, 3), (0, 8, 5)), -- too laggy not worth keeping
    'strong': (None, None, (4, 0, 4), (7, 0, 7), (10, 0, 10)),
    'godly': ((1, 1, 1), (2, 2, 2), (4, 2, 3), (7, 3, 6), (10, 5, 8))
}
reforges_list = list(relavant_reforges.values())


class Route:
    def __init__(self, talismans, rarity):
        self.strength, self.crit_chance, self.crit_damage = [sum(reforges_list[y][rarity][x] * talismans[y] for y in
                                                                 range(len(reforges_list)) if reforges_list[y][rarity])
                                                             for x in range(3)]
        self.counts = talismans
        self.rarity = rarity

    def __repr__(self):
        return ', '.join([f'{c} '
                          f'{"godly/zealous" if self.rarity < 2 and name == "godly" else name} '
                          f'{rarity_grammar(["common", "uncommon", "rare", "epic", "legendary"][self.rarity], c)}'
                          for name, c in zip(relavant_reforges.keys(), self.counts) if c != 0])


def rarity_grammar(rarity, count=0):
    # I really did have to bring the grammar. You know how it goes
    if count == 1:
        return rarity
    return f'{rarity[:-1]}ies' if rarity[-1] == 'y' else f'{rarity}s'


class Session(skypy.Player):
    def __init__(self, bot, user):
        self.bot = bot
        self.user = user
        self.f = self.greet

    async def advance(self, message):
        self.f = await self.f(message)
        return self.f

    async def greet(self, message):
        embed = discord.Embed(title='Before you start:', color=discord.Color.green())
        for i, rule in enumerate([
            'Put the armor on that you will optimize with',
            'Put the weapon you want to optimise with in the first hotbar slot',
            'Enable your skyblock API settings [skyblock menu > settings > api settings]',
            'Log out of Hypixel so that the API syncs'
        ]):
            embed.add_field(name=f'\t{i + 1} >', value=rule, inline=False)
        await self.user.send(f'Hi {self.user.mention}!\nWelcome to notnotmelon\'s talisman optimizer!', embed=embed)
        return await self.ask_uname(message)

    async def ask_uname(self, message):
        await self.user.send('What is your minecraft username?')
        return self.collect_uname

    async def collect_uname(self, message):
        try:
            super().__init__(os.getenv('API_KEY'), message.content)
            await self.user.send('Username accepted')
            return await self.ask_profile(message)
        except skypy.NeverPlayedSkyblockError:
            await self.user.send('You have never played skyblock! Try again')
            return await self.ask_uname(message)
        except SkyblockError:
            await self.user.send('Invalid username! Try again')
            return await self.ask_uname(message)

    async def ask_profile(self, message):
        if len(self.profiles) == 1:
            self.set_profile(list(self.profiles.values())[0])
            return await self.display_talisman_warnings(message)
        else:
            embed = discord.Embed(
                title='Which profile do you want to use?',

                description='(Sorted by date created)',
                color=discord.Color.gold()
            )
            embed.add_field(name='\u200b', value='\n\n'.join(self.profiles.keys()))
            await self.user.send(embed=embed)
            return self.collect_profile

    async def collect_profile(self, message):
        try:
            self.set_profile(self.profiles[message.content.capitalize()])
            return await self.display_talisman_warnings(message)
        except KeyError:
            await self.user.send("Invalid profile! Try again")
            return await self.ask_profile(message)
        except SkyblockError:
            await self.user.send(
                embed=discord.Embed(
                    title='Your API settings are (probably) disabled!',
                    description='Re-enable them with [skyblock menu > settings > api settings]'
                ).set_footer(
                    text='Sometimes this message appears even if your API settings are enabled. If so, exit Hypixel '
                         'and try again '
                )
            )
            return await self.ask_profile(message)

    async def display_talisman_warnings(self, message):
        bad = []
        names = [tali.internal_name() for tali in self.active_talismen]
        for tali in self.inventory + self.talisman_bag:
            if tali.classifier() == 'accessory':
                if tali.internal_name() not in names:
                    bad.append(tali.name())
        if bad:
            await self.user.send(
                embed=discord.Embed(
                    name='Warning!',
                    description='You have unnecessary talismen',
                    color=discord.Color.red()
                ).add_field(
                    name='\u200b',
                    value='\n'.join(bad)
                )
            )
        return await self.ask_weapon(message)

    async def ask_weapon(self, message):
        if len(self.weapons) == 0:
            await self.user.send(
                'You are not carrying any weapons!\n'
                'Place one in your inventory and try again'
            )
        if len(self.weapons) == 1:
            self.weapon = self.weapons[0]
            return await self.test_profile(message)
        else:
            await self.user.send(embed=discord.Embed(
                title='Which weapon do you want to use?',
                color=discord.Color.gold()
            ).add_field(name='\u200b', value='\n\n'.join(
                [weapon.name() for weapon in self.weapons])
            ))
            return self.collect_weapon

    async def collect_weapon(self, message):
        names = [weapon.name().lower() for weapon in self.weapons]
        content = message.content.lower()
        if content in names:
            self.weapon = self.weapons[names.index(content)]
            return await self.test_profile(message)
        else:
            return await self.ask_weapon(message)

    async def test_profile(self, message):
        embed = discord.Embed(
            title='Profile accepted!',
            description='Is this the correct equipment? [YES/NO]',
            color=discord.Color.magenta()
        ).add_field(
            name='Weapon: ',
            value=self.weapon.name()
        )
        for piece in ['helmet', 'chestplate', 'leggings', 'boots']:
            embed.add_field(
                name=piece.capitalize(),
                value=next((a.name() for a in self.armor if a.classifier() == piece), None)
            )
        for name, amount in self.talisman_counts().items():
            embed.add_field(name=rarity_grammar(name).capitalize(),
                            value=amount)

        await self.user.send(embed=embed)
        return self.collect_profile_test

    async def collect_profile_test(self, message):
        response = message.content.lower()
        if response == 'yes':
            return await self.start_potions(message)
        elif response == 'no':
            return await self.ask_profile(message)
        else:
            await self.user.send('Please answer with YES or NO')
            return await self.test_profile(message)

    async def start_potions(self, message):
        self.potion_id = 0
        self.potion_stats = {}
        return await self.ask_potion(message)

    async def ask_potion(self, message):
        await self.user.send(f'Do you use {damaging_potions[self.potion_id]["name"]} pots with this build? [YES/NO]')
        return self.collect_potion

    async def collect_potion(self, message):
        response = message.content.lower()
        if response == 'yes':
            return await self.ask_potion_level(message)
        elif response == 'no':
            self.potion_id += 1
            if self.potion_id >= len(damaging_potions):
                print(f'Potion stats for {self.user}: {self.potion_stats}')
                return await self.calculate_optimal_talismans(message)
            else:
                return await self.ask_potion(message)
        else:
            await self.user.send('Please answer with YES or NO')
            return await self.ask_potion(message)

    async def ask_potion_level(self, message):
        await self.user.send(f'Which level of {damaging_potions[self.potion_id]["name"]} potions do you use?')
        return self.collect_potion_level

    async def collect_potion_level(self, message):
        try:
            self.potion_stats.update({
                stat: amounts[int(message.content)] + self.potion_stats.get(stat, 0)
                for stat, amounts in damaging_potions[self.potion_id]['stats'].items()
            })
            self.potion_id += 1
            if self.potion_id >= len(damaging_potions):
                print(self.potion_stats)
                return None
            else:
                return await self.ask_potion(message)
        except (KeyError, ValueError):
            await self.user.send('Invalid response! Enter a number')
            return await self.ask_potion_level(message)

    def enchantment_modifier(self, weapon):
        enchantments = weapon.enchantments()
        name = weapon.internal_name()
        result = self.skills['combat'] * 4

        if weapon.classifier() == 'SWORD':
            result += enchantments.get('sharpness', 0) * 5
            result += 25 if 'giant killer' in enchantments else 0
            if 'smite' in enchantments or 'bane of arthropods' in enchantments or name in [
                'REAPER_FALCHION',
                'REVENANT_FALCHION',
                'RECLUSE_FANG',
                'SCORPION_FOIL',
                'SHAMAN_SWORD',
                'POOCH_SWORD'
            ]:
                result += enchantments.get('bane of arthropods', 0) * 8
                result += enchantments.get('smite', 0) * 8
                result += enchantments.get('execute', 0) * 50
            else:
                result += enchantments.get('first strike', 0) * 25
                result += enchantments.get('ender slayer', 0) * 12
        elif weapon.classifier() == 'BOW':
            if name == 'SCORPION_BOW':
                return 0
            result += enchantments.get('dragon hunter', 0) * 8
            result += enchantments.get('power', 0) * 8
            result += enchantments.get('snipe', 0) * 2
        elif weapon.classifier() == 'FISHING ROD':
            result += enchantments.get('spiked hook', 0) * 5
        return result

    async def calculate_optimal_talismans(self, message):
        def routes(count, size, rarity):
            def helper(count, idx, current):
                if count == 0:
                    yield Route(current, rarity)
                elif idx == size - 1:
                    new = current.copy()
                    new[idx] += count
                    yield Route(new, rarity)
                else:
                    if reforges_list[idx][rarity]:
                        new = current.copy()
                        new[idx] += 1
                        for x in helper(count - 1, idx, new):
                            yield x
                    for x in helper(count, idx + 1, current):
                        yield x

            return helper(count, 0, [0] * size)

        def apply_stats(additional):
            for key, value in additional.items():
                stats[key] += value

        stats = self.base_stats()
        apply_stats(self.fairy_soul_stats())
        apply_stats(self.armor_stats())
        apply_stats(self.slayer_stats())
        apply_stats(self.skill_stats())
        apply_stats(self.talisman_stats(include_reforges=False))
        apply_stats(self.weapon.stats())
        apply_stats(self.potion_stats)

        weapon_damage = stats['damage']
        base_str = stats['strength']
        base_cc = stats['crit chance']
        base_cd = stats['crit damage']
        ench_modifier = (1 + self.enchantment_modifier(self.weapon) / 100)

        counts = self.talisman_counts()

        route_set = [routes(counts[i], 4, rarity_num) for rarity_num, i in enumerate(counts.keys())]
        all_routes_to_max_crit = (x for x in product(*route_set) if
                                  base_cc + x[0].crit_chance + x[1].crit_chance + x[2].crit_chance +
                                  x[3].crit_chance == 100)
        best = 0
        best_route = Route([0, 0, 0, 0, 0], 0)
        best_stats = [0, 0, 0]
        print('Main algorithm started for', self.uname)
        await self.user.send('Please wait. Your results will be sent shortly...')

        for x in all_routes_to_max_crit:
            stats = {
                'strength': base_str + x[0].strength + x[1].strength + x[2].strength + x[3].strength,
                'crit_damage': base_cd + x[0].crit_damage + x[1].crit_damage + x[2].crit_damage + x[3].crit_damage
            }
            for modifer in self.stat_modifiers():
                modifer(stats)
            strength, crit_damage = stats.values()
            d = (5 + weapon_damage + strength // 5) * (1 + strength / 100) * (1 + crit_damage / 100) * ench_modifier
            if d > best:
                best = d
                best_route = x
                best_stats = [
                    strength,
                    base_cc + x[0].crit_chance + x[1].crit_chance + x[2].crit_chance + x[3].crit_chance - self.potion_stats.get('crit chance', 0),
                    crit_damage
                ]

        embed = discord.Embed(
            title='Calculations Complete!',
            color=discord.Color.orange()
        )
        for rarity, route in zip(["Common", "Uncommon", "Rare", "Epic", "Legendary"], best_route):
            embed.add_field(name=rarity, value=route, inline=False)
        for name, stat in zip(['Strength', 'Crit Chance', 'Crit Damage'], best_stats):
            embed.add_field(name=name, value=stat)
        embed.add_field(name='\u200b', value=f'This setup should give {round(best)}')
        await self.user.send(embed=embed)

        """
        # Calculates the spread using the current meta
        u_needed = min(u, (100 - base_cc) // 2)
        c_needed = min(c, (100 - base_cc) - u_needed * 2)
        meta_route = (
            [0, c - c_needed, 0, c_needed],
            [0, u - u_needed, 0, u_needed],
            [0, r, 0, 0],
            [0, e, 0, 0],
            [0, l, 0, 0]
        )
        meta_stats = [base_str, base_cc, base_cd]
        for rarity, tali_numbers in enumerate(meta_route):
            for reforge, tali_number in enumerate(tali_numbers):
                for stat in range(3):
                    if talismans_raw[reforge][rarity]:
                        meta_stats[stat] += talismans_raw[reforge][rarity][stat] * tali_number
        """

        return None


class Bot(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.sessions = {}

    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        user = message.author
        if user.bot:
            return

        def start_session():
            print(f'Starting session with {user}')
            self.sessions[user] = Session(self, user)

        def end_session():
            print(f'Session ended with {user}')
            self.sessions.pop(user)

        async def reply():
            try:
                session = self.sessions[user]
                if await session.advance(message) is None:
                    await user.send('Session ended!')
                    end_session()
            except:
                await self.get_user(notnotmelon).send(traceback.format_exc())
                await user.send('ERROR: Session closed. Logs have been sent to the developer')
                traceback.print_exc()
                end_session()

        if message.channel == user.dm_channel:
            if user not in self.sessions.keys():
                start_session()
            elif message.content.lower() in ['exit', 'quit', 'stop', 'end']:
                end_session()
                return
            await reply()
        elif '<@652123305096249344>' in message.content:
            start_session()
            await reply()


client = Bot()
print('Attempting to connect to discord...')
client.run(os.getenv('DISCORD_TOKEN'))
