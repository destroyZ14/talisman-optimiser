'''
What's new in version 5?
Skyblock API support :o
Talisman optimizer is now a Discord bot :o
Tarantula helmet support :o
Potion support :o
Superior support
Mastiff support
Fishing rod support
Major speed and memory improvements
'''

import os
import discord
import skypy
from skypy import SkyblockError
import traceback
from itertools import product

if os.environ.get('API_KEY') is None:
    import dotenv

    dotenv.load_dotenv()

print(os.getenv('API_KEY'))
api_key = os.getenv('API_KEY')

notnotmelon = 270352691924959243

damaging_potions = [
    {'name': 'critical', 'stats': {'crit chance': [0, 10, 15, 20, 25], 'crit damage': [0, 10, 20, 30, 40]}},
    {'name': 'strength', 'stats': {'strength': [0, 5.25, 13.125, 21, 31.5, 42, 52.5, 63, 78.75]}},  # Assume cola
    {'name': 'spirit', 'stats': {'crit damage': [0, 10, 20, 30, 40]}}
    # 'archery': irrelevant since it multiplies afterwards everything else # not true this is actually a bug
]

# list of all enchantment powers per level. can be a function or a number
enchantment_values = {
    # sword always
    'sharpness': 5,
    'giant_killer': lambda level: 25 if level > 0 else 0,
    # sword sometimes
    'smite': 8,
    'bane_of_arthropods': 8,
    'first_strike': 25,
    'ender_slayer': 12,
    'cubism': 10,
    'execute': 10,
    'impaling': 12.5,
    # bow always
    'power': 8,
    # bow sometimes
    'dragon_hunter': 8,
    'snipe': 5,  # Would be lower except I only use this for drags and magma bosses
    # rod always
    'spiked_hook': 5
}

# list of relevant enchants for common mobs
activities = {
    'Slayer Bosses': [
        'giant_killer',
        'sharpness',
        'power',
        'spiked_hook',
        'smite',
        'bane_of_arthropods',
        'execute'
    ],
    'Dragons': [
        'giant_killer',
        'sharpness',
        'power',
        'spiked_hook',
        'ender_slayer',
        'execute',
        'dragon_hunter',
        'snipe'
    ],
    'Zealots': [
        'giant_killer',
        'sharpness',
        'power',
        'spiked_hook',
        'ender_slayer',
        'first_strike'
    ],
    'Sea Creatures': [
        'giant_killer',
        'sharpness',
        'power',
        'spiked_hook',
        'first_strike',
        'impaling'
    ],
    'Players': [
        'giant_killer',
        'sharpness',
        'power',
        'spiked_hook',
        'execute',
        'snipe'
    ],
    'Magma Boss': [
        'giant_killer',
        'sharpness',
        'power',
        'spiked_hook',
        'cubism',
        'execute',
        'snipe'
    ],
    'Horseman': [
        'giant_killer',
        'sharpness',
        'power',
        'spiked_hook',
        'execute',
        'snipe'
    ],
    'Other': [
        'giant_killer',
        'sharpness',
        'power',
        'spiked_hook',
        'smite',
        'bane_of_arthropods',
        'first_strike'
    ]
}

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
        self.strength, self.crit_chance, self.crit_damage = [
            sum(reforges_list[y][rarity][x] * talismans[y]
            for y in range(len(reforges_list)) if reforges_list[y][rarity])
            for x in range(3)
        ]
        self.counts = talismans
        self.rarity = rarity
        self.rarity_str = ["common", "uncommon", "rare", "epic", "legendary"][self.rarity]

    def __repr__(self):
        return ', '.join([f'{c} '
                          f'{"godly/zealous" if self.rarity < 2 and name == "godly" else name} '
                          f'{rarity_grammar(self.rarity_str, c)}'
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
            'Put all your talismen in your inventory or talisman bag',
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
            print(f'{self.user} linked to {message.content}')
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
            if await self.try_profile(message, list(self.profiles.values())[0]):
                return await self.display_talisman_warnings(message)
            else:
                return await self.ask_uname(message)
        else:
            embed = discord.Embed(
                title='Which profile do you want to use?',

                description='(Sorted by date created)',
                color=discord.Color.gold()
            )
            embed.add_field(name='\u200b', value='\n\n'.join(self.profiles.keys()))
            await self.user.send(embed=embed)
            return self.collect_profile

    async def try_profile(self, message, profile):
        try:
            self.set_profile(profile)
            return True
        except SkyblockError:
            await self.user.send(
                embed=discord.Embed(
                    title='Your API settings are (probably) disabled!',
                    description='Re-enable them with [skyblock menu > settings > api settings]'
                ).set_footer(
                    text='Sometimes this message appears even if your API settings are enabled. If so, exit Hypixel '
                         'and try again'
                )
            )
            return False

    async def collect_profile(self, message):
        try:
            if await self.try_profile(message, self.profiles[message.content.capitalize()]):
                return await self.display_talisman_warnings(message)
            else:
                return await self.ask_profile(message)
        except KeyError:
            await self.user.send('Choose one of the listed profiles')
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
            embed=discord.Embed(
                title='Which weapon do you want to use?',
                color=discord.Color.gold()
            ).set_footer(
                text='Enter the weapon name or the weapon number'
            )
            for i, weapon in enumerate(self.weapons):
                embed.add_field(
                    name = f'{i + 1} >',
                    value = weapon.name(),
                    inline=False
                )
            await self.user.send(embed=embed)
            return self.collect_weapon

    async def collect_weapon(self, message):
        names = [weapon.name().lower() for weapon in self.weapons]
        content = message.content.lower()
        if content in names:
            self.weapon = self.weapons[names.index(content)]
            return await self.test_profile(message)
        elif content.isnumeric():
            self.weapon = self.weapons[int(content) - 1]
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
                return await self.ask_enchantment_modifier(message)
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
                print(f'Potion stats for {self.user}: {self.potion_stats}')
                return await self.ask_enchantment_modifier(message)
            else:
                return await self.ask_potion(message)
        except (KeyError, ValueError):
            await self.user.send('Invalid response! Enter a number')
            return await self.ask_potion_level(message)

    async def ask_enchantment_modifier(self, message):
        if self.weapon.internal_name() == 'SCORPION_BOW':  # thanks hypixel
            self.enchantment_modifier = 0
            return self.calculate_optimal_talismans
        await self.user.send(embed=discord.Embed(
            title='Which mob will you target with this setup?',
            color=discord.Color.dark_orange()
        ).add_field(
            name='\u200b',
            value='\n'.join(k for k, _ in activities.items()),
        ))
        return self.collect_enchantment_modifier

    async def collect_enchantment_modifier(self, message):
        enchantments = self.weapon.enchantments()
        self.enchantment_modifier = self.skills['combat'] * 4

        if message.content.title() not in activities:
            await self.user.send('Invalid response! Pick one of the activities')
            return await self.ask_enchantment_modifier(message)

        for enchantment in activities[message.content.title()]:
            ench_strength = enchantment_values[enchantment]
            if callable(ench_strength):
                self.enchantment_modifier += ench_strength(enchantments.get(enchantment, 0))
            else:
                self.enchantment_modifier += ench_strength * enchantments.get(enchantment, 0)

        print(f'Enchantment modifier for {self.user}: {self.enchantment_modifier}')
        self.enchantment_modifier = (1 + self.enchantment_modifier / 100)
        return await self.calculate_optimal_talismans(message)

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

        counts = self.talisman_counts()
        
        print('Main algorithm started for', self.uname)
        await self.user.send('Please wait. Your results will be sent shortly...')
        
        best = 0
        best_route = Route([0, 0, 0, 0, 0], 0)
        best_stats = [0, 0, 0]
        
        goal = 100 - base_cc
        for c, u, r, e, l in product(*[routes(counts[key], 4, rarity_num) for rarity_num, key in enumerate(counts.keys())]):
            cc = c.crit_chance + u.crit_chance + r.crit_chance + e.crit_chance + l.crit_chance
            if cc == goal:
                stats = {
                    'strength': base_str + c.strength + u.strength + r.strength + e.strength + l.strength,
                    'crit chance': 100,
                    'crit damage': base_cd + c.crit_damage + u.crit_damage + r.crit_damage + e.crit_damage + l.crit_damage
                }
                
                for modifer in self.stat_modifiers():
                    modifer(stats)
                    
                d = skypy.damage(weapon_damage, stats['strength'], stats['crit damage'], self.enchantment_modifier)
                    
                if d > best:
                    best = d
                    best_route = [c, u, r, e, l]
                    best_stats = stats

        await self.user.send('Calculations complete!')

        async def display_result(title, routes, stats, damage):
            embed = discord.Embed(
                title=title,
                color=discord.Color.orange(),
            ).set_footer(
                text='Damage multipliers from weapons such as\n'
                'scorpion foil or reaper falichion are not included.\n'
                'Talisman results should still be correct.'
            )
            if routes:
                for route in routes:
                    if str(route):
                        embed.add_field(name=route.rarity_str.title(), value=route, inline=False)
            for name, stat in stats.items():
                embed.add_field(name=name.title(), value=stat)
            embed.add_field(name='\u200b', value=f'This setup should deal {round(damage)} damage')
            await self.user.send(embed=embed)

        embeds = []

        await display_result('Best Route', best_route, best_stats, best)

        # Calculates the spread using the current meta
        c, u, r, e, l = [v for k, v in counts.items()]
        u_needed = min(u, (100 - base_cc) // 2)
        c_needed = min(c, (100 - base_cc) - u_needed * 2)
        
        meta_route = (
            Route([0, c - c_needed, 0, c_needed], 0),
            Route([0, u - u_needed, 0, u_needed], 1),
            Route([0, r, 0, 0], 2),
            Route([0, e, 0, 0], 3),
            Route([0, l, 0, 0], 4)
        )
        
        meta_stats = {
            'strength': base_str + sum(route.strength for route in meta_route),
            'crit chance': base_cc + sum(route.crit_chance for route in meta_route),
            'crit damage': base_cd + sum(route.crit_damage for route in meta_route)
        }
        
        for modifer in self.stat_modifiers():
            modifer(meta_stats)
            
        meta_damage = skypy.damage(weapon_damage, meta_stats['strength'], meta_stats['crit damage'], self.enchantment_modifier)

        await display_result('Current Meta', meta_route, meta_stats, meta_damage)
        
        '''
        for modifier in self.stat_modifiers():
            modifier(stats)
        
        await display_result('Without Talismans', None, stats, skypy.damage(
            weapon_damage, stats['strength'], stats['crit damage'], self.enchantment_modifier)
        )
        '''


class Bot(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.sessions = {}

    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        user = message.author
        if user.bot:
            return

        async def plug_patreon():
            await user.send(embed=discord.Embed(
                title='Like what you see?',
                color=discord.Color.gold()
            ).add_field(
                name='\u200b',
                value='\n'.join([
                    'Consider a donation via patreon',
                    'Donations help support server costs, and you can suggest new features for the bot',
                    '',
                    'https://www.patreon.com/user?u=28018797'
                ])
            ))#.set_image(url='https://cdn.dribbble.com/users/407429/screenshots/2817437/patreon_1-01.png'))

        def updates():
            return os.getenv('ENV') != 'server' and user != self.get_user(notnotmelon)

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
                    await plug_patreon()
                    end_session()
            except:
                await self.get_user(notnotmelon).send(f'{user}\n{traceback.format_exc()}')
                await user.send('ERROR: Session closed. Logs have been sent to the developer')
                print(user)
                traceback.print_exc()
                end_session()

        if message.channel == user.dm_channel:
            if updates():
                await message.channel.send('The bot is currently down for updates, please check back later')
                return
            if user not in self.sessions.keys():
                start_session()
                await reply()
            elif message.content.lower() in ['exit', 'quit', 'stop', 'end']:
                end_session()
            else:
                await reply()
        elif self.user in message.mentions:
            if updates():
                await message.channel.send('The bot is currently down for updates, please check back later')
                return
            start_session()
            await reply()


client = Bot()
print('Attempting to connect to discord...')
client.run(os.getenv('DISCORD_TOKEN'))
