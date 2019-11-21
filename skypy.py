#######################################
#									  #
#			  SkyPy v0.2			  #
#									  #
#	by: Jordan Baron Copyright 2019	  #
#	extended by: Zachary Picco 2019	  #
#									  #
#######################################

# API Calls
import requests, json
from datetime import datetime
# --------

# Inventory parsing
from base64 import b64decode as one
from gzip import decompress as two
from io import BytesIO as three
from struct import unpack
# -----------------

import re


# ---------------- EXCEPTIONS ----------------


class InvalidUsernameError(Exception):
    pass


class InvalidUUIDError(Exception):
    pass


class InvalidAPIKeyError(Exception):
    pass


class EmptyAPIKeyError(Exception):
    pass


class APIDisabledError(Exception):
    pass


class UndefinedUnameOrUUIDError(Exception):
    pass


class UndefinedProfileError(Exception):
    pass


# --------------------------------------------

skill_exp_requirements = [50, 125, 200, 300, 500, 750, 1000, 1500, 2000, 3500, 5000,
                          7500, 10000, 15000, 20000, 30000, 50000, 75000, 100000, 200000, 300000,
                          400000, 500000, 600000, 700000, 800000, 900000, 1000000, 1100000, 1200000, 1300000,
                          1400000, 1500000, 1600000, 1700000, 1800000, 1900000, 2000000, 2100000, 2200000, 2300000,
                          2400000, 2500000, 2600000, 2700000, 2800000, 3100000, 3400000, 3700000, 4000000]

runecrafting_exp_requirements = [50, 100, 125, 160, 200, 250, 315, 400, 500, 625, 785, 1000,
                                 1250, 1600, 2000, 2465, 3125, 4000, 5000, 6200, 7800, 9800, 12200,
                                 15300]  # Shamelessly stolen from sky.lea.moe


def skill_exp_to_skill_level(exp, runecrafting=False):
    """Takes an integer that repersents any skill's current experience. Returns a dictionary with three values; your
    current skill level, the remaining experience to the next level, and the percent progress to the next level. Set
    runecrafting = True in order to use runecrafting's unique level scaling. """
    total = exp
    if exp == 0:
        return {'level': 0, 'remainder': 0, 'progress': 0, 'total_exp': 0}
    for lvl, requirement in enumerate(runecrafting_exp_requirements if runecrafting else skill_exp_requirements):
        if exp > requirement:
            exp -= requirement
        else:
            return {'level': lvl, 'remainder': exp, 'progress': exp / requirement, 'total_exp': total}
    return {'level': lvl, 'remainder': exp, 'progress': 1.0, 'total_exp': total}


tiered_talismen = [  # Helps me filter useless talismen
    ('POTION_AFFINITY_TALISMAN', 'RING_POTION_AFFINITY', 'ARTIFACT_POTION_AFFINITY'),
    ('FEATHER_TALISMAN', 'FEATHER_RING', 'FEATHER_ARTIFACT'),
    ('SEA_CREATURE_TALISMAN', 'SEA_CREATURE_RING', 'SEA_CREATURE_ARTIFACT'),
    ('HEALING_TALISMAN', 'HEALING_RING'),
    ('CANDY_TALISMAN', 'CANDY_RING', 'CANDY_ARTIFACT'),
    ('INTIMIDATION_TALISMAN', 'INTIMIDATION_RING', 'INTIMIDATION_ARTIFACT'),
    ('SPIDER_TALISMAN', 'SPIDER_RING', 'SPIDER_ARTIFACT'),
    ('RED_CLAW_TALISMAN', 'RED_CLAW_ARTIFACT', 'RED_CLAW_RING'),
    ('HUNTER_TALISMAN', 'HUNTER_RING'),
    ('ZOMBIE_TALISMAN', 'ZOMBIE_RING', 'ZOMBIE_ARTIFACT'),
    ('BAT_TALISMAN', 'BAT_RING', 'BAT_ARTIFACT')
]


def make_item(nbt, slot_number):
    classifier = re.search('\b(\w+)$', nbt['tag']['display']['lore'][-1])
    if classifier == 'ACCESSORY':
        return Talisman(nbt, slot_number)
    if classifier in ('SWORD', 'BOW', 'BOOTS', 'LEGGINGS', 'CHESTPLATE', 'HELMET'):
        return Equipment(nbt, slot_number)
    return Item(nbt, slot_number)

def decode_inventory_data(raw):
    """Takes a raw string repensenting inventory data.
    Returns a json object with the inventory's contents"""

    raw = three(two(one(raw)))  # Unzip raw string from the api

    def read(type, length):
        if type in 'chill':
            return int.from_bytes(raw.read(length), byteorder='big')
        if type == 's':  # I couldn't get unpack to work with a string for some reason :?
            return raw.read(length).decode("utf-8")
        return unpack('>' + type, raw.read(length))[0]

    def parse_list():
        subtype = read('c', 1)
        payload = []
        for _ in range(read('i', 4)):
            helper(payload, subtype)
        return payload

    def parse_compound():
        payload = {}
        while helper(payload) != 0:  # Parse tags until we find an endcap (type == 0)
            pass  # Nothing needs to happen here
        return payload

    payloads = {
        1: lambda: read('c', 1),  # Byte
        2: lambda: read('h', 2),  # Short
        3: lambda: read('i', 4),  # Int
        4: lambda: read('l', 8),  # Long
        5: lambda: read('f', 4),  # Float
        6: lambda: read('d', 8),  # Double
        7: lambda: raw.read(read('i', 4)),  # Byte Array
        8: lambda: read('s', read('h', 2)),  # String
        9: parse_list,  # List
        10: parse_compound,  # Compound
        11: lambda: [read('i', 4) for _ in range(read('i', 4))],  # Int Array
        12: lambda: [read('l', 8) for _ in range(read('i', 4))]  # Long Array
    }

    def helper(dictionary, tag_id=None):
        if tag_id is None:  # Are we inside a list?
            tag_id = read('c', 1)
            if tag_id == 0:  # Is this the end of a compound?
                return 0
            name = read('s', read('h', 2))

        payload = payloads[tag_id]()
        if isinstance(dictionary, dict):
            dictionary[name] = payload
        else:
            dictionary.append(payload)

    raw.read(3)  # Remove file header (we ingore footer)
    root = {}
    helper(root)
    return [make_item(x, i) for i, x in enumerate(root['i']) if x]


class Item:
    def __init__(self, nbt, slot_number):
        self.__nbt__ = nbt
        self.slot_number = slot_number

    def __getitem__(self, name):
        return self.__nbt__[name]

    def __str__(self):
        return str(self.__nbt__)

    def __repr__(self):
        return str(self.__nbt__)

    def name(self):
        return re.sub('.*' + self.reforge() + ' ?', '', self['tag']['display']['Name'], 1, flags=re.IGNORECASE)

    def internal_name(self):
        return self['tag']['ExtraAttributes']['id']

    def rarity(self):
        return re.search('COMMON|UNCOMMON|RARE|EPIC|LEGENDARY|SPECIAL', self.description()[-1]).lower()

    def reforge(self):
        try:
            return self['tag']['ExtraAttributes']['modifier']
        except KeyError:
            return None

    def description(self):
        return self['tag']['display']['Lore']


class Equipment(Item):
    # Why do we have to sift the lorestring for this?
    # Can't it just be in the nbt data?
    def stats(self):
        results = {}
        for line in self.description():
            for stat in ['damage', 'strength', 'crit chance', 'crit damage', 'attack speed', 'health', 'defense',
                         'speed', 'intelligence']:
                if re.search('\d' + stat + ':', line,
                             flags=re.IGNORECASE):  # If the lorestring contains our desired stat
                    results[stat] = int(
                        re.search('(?<=\+)\d+', line)[0])  # Add the value of that stat to the dictionary
        return results


class Talisman(Equipment):
    def __init__(self, nbt, slot_number):
        super().__init__(nbt, slot_number)
        self.__active__ = True

    def disable(self):
        self.__active__ = False

    def stats(self, use_reforge=True):
        if not self.__active__:  # If this talisman is nearby another talisman of the same family, ignore it
            return {'damage': 0, 'strength': 0, 'crit chance': 0, 'crit damage': 0, 'attack speed': 0, 'health': 0,
                    'defense': 0, 'speed': 0, 'intelligence': 0}
        if use_reforge:
            return super().stats()


# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


def get_uuid(uname):
    try:
        req = requests.get('https://api.mojang.com/users/profiles/minecraft/' + uname).content
        return json.loads(req)['id']
    except KeyError:
        raise InvalidUsernameError


def get_uname(uuid):
    try:
        req = requests.get('https://api.mojang.com/user/profiles/' + uuid + '/names').content
        return json.loads(req)[-1]['name']
    except KeyError:
        raise InvalidUUIDError


class Player:
    def __init__(self, key, uname=None, uuid=None):
        self.api_key = key
        if uname and uuid:
            self.uname = uname
            self.uuid = uuid
        elif uname:
            self.uname = uname
            self.uuid = get_uuid(uname)
        elif uuid:
            self.uuid = uuid
            self.uname = get_uname(uuid)

    def set_uname(self, uname):
        self.uname = uname
        self.uuid = get_uuid(uname)

    def set_uuid(self, uuid):
        self.uuid = uuid
        self.uname = get_uname(uuid)

    def __check_uname_uuid__(self):
        if not self.uname and not self.uuid:
            raise UndefinedUnameOrUUIDError

    def set_profile(self, profile):
        self.profile = profile

        try:
            v = self.__call_api__('/skyblock/profile?profile=' + self.profile)['profile']['members'][self.uuid]
            print(list(v.keys()))
            self.inventory = decode_inventory_data(v['inv_contents']['data'])
            self.echest = decode_inventory_data(v['ender_chest_contents']['data'])
            self.armor = decode_inventory_data(v['inv_armor']['data'])
            self.talisman_bag = decode_inventory_data(v['talisman_bag']['data'])
            self.potion_bag = decode_inventory_data(v['potion_bag']['data'])
            self.fish_bag = decode_inventory_data(v['fishing_bag']['data'])
            self.quiver = decode_inventory_data(v['quiver']['data'])
            self.candy_bag = decode_inventory_data(v['candy_inventory_contents']['data'])
        except KeyError:
            print('API setting disabled for user ' + self.uname)

    def __check_profile__(self):
        if not self.profile:
            raise UndefinedProfileError

    def __call_api__(self, endpoint):
        base_url = 'https://api.hypixel.net'
        if not self.api_key:
            raise InvalidAPIKeyError

        # build endpoint url
        endpoint_url = base_url

        if '?' in endpoint:
            endpoint_url += endpoint + '&key=' + self.api_key
        else:
            endpoint_url += endpoint + '?key=' + self.api_key

        # send request
        resp = requests.get(endpoint_url).content
        resp = json.loads(resp)

        # check if invalid api key
        if not resp['success'] and resp['cause'] == 'Invalid API key!':
            raise InvalidAPIKeyError

        return resp

    def is_player_online(self):
        self.__check_uname_uuid__()
        player_data = self.__call_api('/player?name=' + self.uname)['player']
        return player_data['lastLogout'] < player_data['lastLogin']

    def player_profiles(self):
        self.__check_uname_uuid__()
        profiles = {}
        player = self.__call_api__('/player?uuid=' + self.uuid)
        profile_ids = player['player']['stats']['SkyBlock']['profiles']

        for k, v in profile_ids.items():
            profiles[v['cute_name']] = k

        return profiles

    def player_levels(self):
        self.__check_uname_uuid__()
        self.__check_profile__()

        player_info = {}
        try:
            v = self.__call_api__('/skyblock/profile?profile=' + self.profile)['profile']['members'][self.uuid]

            # calc join date here so list isn't super messy
            player_join_date = datetime.fromtimestamp(v['first_join'] / 1000.0)
            player_join_date = str(player_join_date.month) + '/' + str(player_join_date.day) + '/' + str(
                player_join_date.year)

            player_info = {
                'join_date': player_join_date,
                'fairy_souls_collected': v['fairy_souls_collected'],
                'kills': int(v['stats']['kills'])
            }

            # skills
            def skill_to_exp(skill):
                return int(v['experience_skill_' + skill])

            player_info['skills'] = {
                name: skill_exp_to_skill_level(skill_to_exp(name), name == 'runecrafting')
                for name in ['farming', 'mining', 'foraging', 'combat', 'enchanting', 'alchemy', 'fishing', 'carpentry',
                             'runecrafting']
            }

            # slayer levels
            def parse_slayer_api(name):
                return int(list(v['slayer_bosses'][name]['claimed_levels'].keys())[-1].replace('level_', ''))

            player_info['slayer_levels'] = {
                'zombie_slayer_level': parse_slayer_api('zombie'),
                'spider_slayer_level': parse_slayer_api('spider'),
                'wolf_slayer_level': parse_slayer_api('wolf')
            }
        except KeyError:
            print('API setting disabled for user ' + self.uname)

        return player_info

    # Method is unfinished, only works for damage stats. feel free to send me a corrected version!
    def player_stats(self, include_talisman_reforges=True):
        self.__check_uname_uuid__()
        self.__check_profile__()

        stats = {'damage': 0, 'strength': 0, 'crit chance': 20, 'crit damage': 50, 'attack speed': 100, 'health': 100,
                 'defense': 0, 'speed': 100, 'intelligence': 0}  # Base stats on a new profile
        levels = self.player_levels()

        # Fairy Souls
        stats['health'] += 0
        stats['defense'] += levels['fairy_souls_collected'] // 5 + levels['fairy_souls_collected'] // 25
        stats['strength'] += levels['fairy_souls_collected'] // 5 + levels['fairy_souls_collected'] // 25
        stats['speed'] += levels['fairy_souls_collected'] // 50

        # Slayer Levels
        zombie = (('health', 2), ('health', 2), ('health', 3), ('health', 3), ('health', 4), ('health', 4),
                  ('health', 5), ('health', 5), ('health', 6))
        spider = (('crit damage', 1), ('crit damage', 1), ('crit damage', 1), ('crit damage', 1), ('crit damage', 2),
                  ('crit damage', 2), ('crit chance', 1), ('crit damage', 3), ('crit chance', 3))
        wolf = (('speed', 1), ('health', 2), ('speed', 1), ('health', 2), ('crit damage', 1), ('health', 3),
                ('crit damage', 2), ('speed', 1), ('', 0))
        for rewards, level in zip([zombie, spider, wolf], list(levels['slayer_levels'].values())):
            for i, (reward, amount) in enumerate(rewards):
                if level > i and reward:
                    stats[reward] += amount

        # Skill Levels
        stats['crit chance'] += levels['skills']['combat']['level']
        stats['strength'] += levels['skills']['foraging']['level'] + min(0, levels['skills']['foraging']['level'] - 15)

        # Talismans
        for i in self.talisman_bag:
            for stat, amount in i.stats().items():
                stats[stat] += amount

        # Armor
        superior = True
        for i in self.player_armor():
            if 'SUPERIOR' not in i.internal_name():
                superior = False
            for stat, amount in i.stats().items():
                stats[stat] += amount
        if superior:
            stats = {stat: round(amount * 1.05) for stat, amount in stats.items()}

        return stats

    def player_auctions(self):
        self.__check_uname_uuid__()
        self.__check_profile()

        resp = self.__call_api('/skyblock/auction?uuid=' + self.uuid + '&profile=' + self.profile)

        player_auctions = []
        for i in range(len(resp['auctions'])):
            curr_auction = resp['auctions'][i]

        if not curr_auction['claimed']:
            player_auctions.append(
                {
                    'item_name': curr_auction['item_name'], 'starting_bid': curr_auction['starting_bid'],
                    'highest_bid': curr_auction['highest_bid_amount'],
                    'highest_bidder': curr_auction['claimed_bidders'] if len(
                        curr_auction['claimed_bidders']) > 0 else None,
                    'end': curr_auction['end']
                })

    def dump_all_player_data(self):
        self.__check_profile__()

        return self.__call_api('/skyblock/profile?profile=' + self.profile)['profile']['members']
