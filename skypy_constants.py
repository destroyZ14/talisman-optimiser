skill_rewards = {
    'foraging': {
        0: {
            'strength': 1
        },
        15: {
            'strength': 2
        }
    },
    'combat': {
        0: {
            'crit chance': 1,
            'ench modifer': 4
        }
    }
}

talismen = [
    'CANDY_ARTIFACT'
]

slayer_rewards = {
    'zombie': (('health', 2), ('health', 2), ('health', 3), ('health', 3), ('health', 4), ('health', 4),
               ('health', 5), ('health', 5), ('health', 6)),
    'spider': (('crit damage', 1), ('crit damage', 1), ('crit damage', 1), ('crit damage', 1), ('crit damage', 2),
               ('crit damage', 2), ('crit chance', 1), ('crit damage', 3), ('crit chance', 3)),
    'wolf': (('speed', 1), ('health', 2), ('speed', 1), ('health', 2), ('crit damage', 1), ('health', 3),
             ('crit damage', 2), ('speed', 1), ('', 0))
}

fairy_soul_hp_bonus = [3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15, 15, 16, 16,
                       17, 17, 18, 18, 19, 19, 20, 20, 21]

skill_exp_requirements = [50, 125, 200, 300, 500, 750, 1000, 1500, 2000, 3500, 5000,
                          7500, 10000, 15000, 20000, 30000, 50000, 75000, 100000, 200000, 300000,
                          400000, 500000, 600000, 700000, 800000, 900000, 1000000, 1100000, 1200000, 1300000,
                          1400000, 1500000, 1600000, 1700000, 1800000, 1900000, 2000000, 2100000, 2200000, 2300000,
                          2400000, 2500000, 2600000, 2700000, 2800000, 3100000, 3400000, 3700000, 4000000]

runecrafting_exp_requirements = [50, 100, 125, 160, 200, 250, 315, 400, 500, 625, 785, 1000,
                                 1250, 1600, 2000, 2465, 3125, 4000, 5000, 6200, 7800, 9800, 12200,
                                 15300]  # Shamelessly stolen from sky.lea.moe

tiered_talismen = (  # Helps me filter useless talismen
    ('POTION_AFFINITY_TALISMAN', 'RING_POTION_AFFINITY', 'ARTIFACT_POTION_AFFINITY'),
    ('FEATHER_TALISMAN', 'FEATHER_RING', 'FEATHER_ARTIFACT'),
    ('SEA_CREATURE_TALISMAN', 'SEA_CREATURE_RING', 'SEA_CREATURE_ARTIFACT'),
    ('HEALING_TALISMAN', 'HEALING_RING'),
    ('CANDY_TALISMAN', 'CANDY_RING', 'CANDY_ARTIFACT'),
    ('INTIMIDATION_TALISMAN', 'INTIMIDATION_RING', 'INTIMIDATION_ARTIFACT'),
    ('SPIDER_TALISMAN', 'SPIDER_RING', 'SPIDER_ARTIFACT'),
    ('RED_CLAW_TALISMAN', 'RED_CLAW_RING', 'RED_CLAW_ARTIFACT'),
    ('HUNTER_TALISMAN', 'HUNTER_RING'),
    ('ZOMBIE_TALISMAN', 'ZOMBIE_RING', 'ZOMBIE_ARTIFACT'),
    ('BAT_TALISMAN', 'BAT_RING', 'BAT_ARTIFACT')
)

reforges = {
    'clean': (
        {'strength': 0, 'crit chance': 0, 'crit damage': 0, 'attack speed': 1, 'health': 1, 'defense': 1, 'speed': 1,
         'intelligence': 0},
        {'strength': 0, 'crit chance': 0, 'crit damage': 0, 'attack speed': 1, 'health': 1, 'defense': 2, 'speed': 1,
         'intelligence': 0},
        {'strength': 0, 'crit chance': 0, 'crit damage': 0, 'attack speed': 2, 'health': 2, 'defense': 4, 'speed': 1,
         'intelligence': 0},
        {'strength': 0, 'crit chance': 0, 'crit damage': 0, 'attack speed': 2, 'health': 2, 'defense': 7, 'speed': 1,
         'intelligence': 0},
        {'strength': 0, 'crit chance': 0, 'crit damage': 0, 'attack speed': 2, 'health': 2, 'defense': 10, 'speed': 1,
         'intelligence': 0}
    ),
    'demonic': (
        {'strength': 1, 'crit chance': 0, 'crit damage': 0, 'attack speed': 0, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': 3},
        {'strength': 2, 'crit chance': 0, 'crit damage': 0, 'attack speed': 0, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': 6},
        {'strength': 2, 'crit chance': 0, 'crit damage': 0, 'attack speed': 0, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': 10},
        {'strength': 3, 'crit chance': 0, 'crit damage': 0, 'attack speed': 0, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': 15},
        {'strength': 5, 'crit chance': 0, 'crit damage': 0, 'attack speed': 0, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': 20}
    ),
    'fierce': (
        {'strength': 1, 'crit chance': 1, 'crit damage': 1, 'attack speed': 0, 'health': 0, 'defense': 1, 'speed': 0,
         'intelligence': 0},
        {'strength': 2, 'crit chance': 1, 'crit damage': 2, 'attack speed': 0, 'health': 0, 'defense': 2, 'speed': 0,
         'intelligence': 0},
        {'strength': 2, 'crit chance': 1, 'crit damage': 2, 'attack speed': 0, 'health': 0, 'defense': 2, 'speed': 0,
         'intelligence': 0},
        {'strength': 3, 'crit chance': 1, 'crit damage': 3, 'attack speed': 0, 'health': 0, 'defense': 3, 'speed': 0,
         'intelligence': 0},
        {'strength': 5, 'crit chance': 2, 'crit damage': 5, 'attack speed': 0, 'health': 0, 'defense': 5, 'speed': 0,
         'intelligence': 0}
    ),
    'forceful': (
        {'strength': 2, 'crit chance': 0, 'crit damage': 0, 'attack speed': 0, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': 0},
        {'strength': 4, 'crit chance': 0, 'crit damage': 0, 'attack speed': 0, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': 0},
        {'strength': 7, 'crit chance': 0, 'crit damage': 0, 'attack speed': 0, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': 0},
        {'strength': 10, 'crit chance': 0, 'crit damage': 0, 'attack speed': 0, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': 0},
        {'strength': 15, 'crit chance': 0, 'crit damage': 0, 'attack speed': 0, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': 0}
    ),
    'godly': (
        {'strength': 1, 'crit chance': 1, 'crit damage': 1, 'attack speed': 0, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': 1},
        {'strength': 2, 'crit chance': 2, 'crit damage': 2, 'attack speed': 0, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': 2},
        {'strength': 4, 'crit chance': 2, 'crit damage': 3, 'attack speed': 0, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': 2},
        {'strength': 7, 'crit chance': 3, 'crit damage': 6, 'attack speed': 0, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': 3},
        {'strength': 10, 'crit chance': 5, 'crit damage': 8, 'attack speed': 0, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': 5}
    ),
    'heavy': (
        {'strength': 0, 'crit chance': 0, 'crit damage': -1, 'attack speed': 0, 'health': 1, 'defense': 3, 'speed': 0,
         'intelligence': 0},
        {'strength': 0, 'crit chance': 0, 'crit damage': -2, 'attack speed': 0, 'health': 2, 'defense': 6, 'speed': 0,
         'intelligence': 0},
        {'strength': 0, 'crit chance': 0, 'crit damage': -2, 'attack speed': 0, 'health': 4, 'defense': 10, 'speed': 0,
         'intelligence': 0},
        {'strength': 0, 'crit chance': 0, 'crit damage': -3, 'attack speed': 0, 'health': 7, 'defense': 15, 'speed': 0,
         'intelligence': 0},
        {'strength': 0, 'crit chance': 0, 'crit damage': -5, 'attack speed': 0, 'health': 10, 'defense': 20, 'speed': 0,
         'intelligence': 0}
    ),
    'keen': (
        {'strength': 1, 'crit chance': 1, 'crit damage': 1, 'attack speed': 0, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': 0},
        {'strength': 2, 'crit chance': 1, 'crit damage': 1, 'attack speed': 0, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': 0},
        {'strength': 2, 'crit chance': 2, 'crit damage': 2, 'attack speed': 0, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': 0},
        {'strength': 3, 'crit chance': 2, 'crit damage': 2, 'attack speed': 0, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': 0},
        {'strength': 5, 'crit chance': 3, 'crit damage': 3, 'attack speed': 0, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': 0}
    ),
    'light': (
        {'strength': 0, 'crit chance': 0, 'crit damage': 1, 'attack speed': 1, 'health': 1, 'defense': 1, 'speed': 1,
         'intelligence': 0},
        {'strength': 0, 'crit chance': 0, 'crit damage': 2, 'attack speed': 2, 'health': 2, 'defense': 2, 'speed': 1,
         'intelligence': 0},
        {'strength': 0, 'crit chance': 0, 'crit damage': 2, 'attack speed': 2, 'health': 2, 'defense': 2, 'speed': 2,
         'intelligence': 0},
        {'strength': 0, 'crit chance': 0, 'crit damage': 3, 'attack speed': 3, 'health': 3, 'defense': 3, 'speed': 2,
         'intelligence': 0},
        {'strength': 0, 'crit chance': 0, 'crit damage': 5, 'attack speed': 5, 'health': 5, 'defense': 5, 'speed': 3,
         'intelligence': 0}
    ),
    'mythic': (
        {'strength': 1, 'crit chance': 0, 'crit damage': 0, 'attack speed': 0, 'health': 1, 'defense': 1, 'speed': 1,
         'intelligence': 3},
        {'strength': 2, 'crit chance': 0, 'crit damage': 0, 'attack speed': 0, 'health': 2, 'defense': 2, 'speed': 1,
         'intelligence': 7},
        {'strength': 2, 'crit chance': 0, 'crit damage': 0, 'attack speed': 0, 'health': 2, 'defense': 2, 'speed': 1,
         'intelligence': 12},
        {'strength': 3, 'crit chance': 0, 'crit damage': 0, 'attack speed': 0, 'health': 3, 'defense': 3, 'speed': 1,
         'intelligence': 18},
        {'strength': 5, 'crit chance': 0, 'crit damage': 0, 'attack speed': 0, 'health': 5, 'defense': 5, 'speed': 1,
         'intelligence': 25}
    ),
    'pure': (
        {'strength': 1, 'crit chance': 1, 'crit damage': 1, 'attack speed': 1, 'health': 1, 'defense': 1, 'speed': 1,
         'intelligence': 1},
        {'strength': 2, 'crit chance': 2, 'crit damage': 2, 'attack speed': 2, 'health': 2, 'defense': 2, 'speed': 1,
         'intelligence': 2},
        {'strength': 2, 'crit chance': 2, 'crit damage': 2, 'attack speed': 2, 'health': 2, 'defense': 2, 'speed': 1,
         'intelligence': 2},
        {'strength': 3, 'crit chance': 3, 'crit damage': 3, 'attack speed': 3, 'health': 3, 'defense': 3, 'speed': 1,
         'intelligence': 3},
        {'strength': 5, 'crit chance': 5, 'crit damage': 5, 'attack speed': 5, 'health': 5, 'defense': 5, 'speed': 1,
         'intelligence': 5}
    ),
    'smart': (
        {'strength': 0, 'crit chance': 0, 'crit damage': 0, 'attack speed': 0, 'health': 0, 'defense': 1, 'speed': 0,
         'intelligence': 5},
        {'strength': 0, 'crit chance': 0, 'crit damage': 0, 'attack speed': 0, 'health': 0, 'defense': 2, 'speed': 0,
         'intelligence': 10},
        {'strength': 0, 'crit chance': 0, 'crit damage': 0, 'attack speed': 0, 'health': 0, 'defense': 2, 'speed': 0,
         'intelligence': 18},
        {'strength': 0, 'crit chance': 0, 'crit damage': 0, 'attack speed': 0, 'health': 0, 'defense': 3, 'speed': 0,
         'intelligence': 32},
        {'strength': 0, 'crit chance': 0, 'crit damage': 0, 'attack speed': 0, 'health': 0, 'defense': 5, 'speed': 0,
         'intelligence': 50}
    ),
    'strong': (
        {'strength': 1, 'crit chance': 0, 'crit damage': 1, 'attack speed': 0, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': 0},
        {'strength': 2, 'crit chance': 0, 'crit damage': 2, 'attack speed': 0, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': 0},
        {'strength': 4, 'crit chance': 0, 'crit damage': 4, 'attack speed': 0, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': 0},
        {'strength': 7, 'crit chance': 0, 'crit damage': 7, 'attack speed': 0, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': 0},
        {'strength': 10, 'crit chance': 0, 'crit damage': 10, 'attack speed': 0, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': 0}
    ),
    'superior': (
        {'strength': 1, 'crit chance': 1, 'crit damage': 1, 'attack speed': 0, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': 0},
        {'strength': 2, 'crit chance': 1, 'crit damage': 1, 'attack speed': 0, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': 0},
        {'strength': 4, 'crit chance': 1, 'crit damage': 1, 'attack speed': 0, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': 0},
        {'strength': 7, 'crit chance': 1, 'crit damage': 1, 'attack speed': 0, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': 0},
        {'strength': 10, 'crit chance': 1, 'crit damage': 1, 'attack speed': 0, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': 0}
    ),
    'titanic': (
        {'strength': 0, 'crit chance': 0, 'crit damage': 0, 'attack speed': 0, 'health': 3, 'defense': 3, 'speed': 0,
         'intelligence': 0},
        {'strength': 0, 'crit chance': 0, 'crit damage': 0, 'attack speed': 0, 'health': 6, 'defense': 6, 'speed': 0,
         'intelligence': 0},
        {'strength': 0, 'crit chance': 0, 'crit damage': 0, 'attack speed': 0, 'health': 10, 'defense': 10, 'speed': 0,
         'intelligence': 0},
        {'strength': 0, 'crit chance': 0, 'crit damage': 0, 'attack speed': 0, 'health': 15, 'defense': 15, 'speed': 0,
         'intelligence': 0},
        {'strength': 0, 'crit chance': 0, 'crit damage': 0, 'attack speed': 0, 'health': 20, 'defense': 20, 'speed': 0,
         'intelligence': 0}
    ),
    'unpleasant': (
        {'strength': 0, 'crit chance': 1, 'crit damage': 1, 'attack speed': 0, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': 1},
        {'strength': 0, 'crit chance': 2, 'crit damage': 2, 'attack speed': 0, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': 1},
        {'strength': 0, 'crit chance': 3, 'crit damage': 3, 'attack speed': 0, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': 2},
        {'strength': 0, 'crit chance': 6, 'crit damage': 6, 'attack speed': 0, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': 3},
        {'strength': 0, 'crit chance': 8, 'crit damage': 8, 'attack speed': 0, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': 5}
    ),
    'wise': (
        {'strength': 0, 'crit chance': 0, 'crit damage': 0, 'attack speed': 0, 'health': 1, 'defense': 0, 'speed': 1,
         'intelligence': 10},
        {'strength': 0, 'crit chance': 0, 'crit damage': 0, 'attack speed': 0, 'health': 2, 'defense': 0, 'speed': 1,
         'intelligence': 20},
        {'strength': 0, 'crit chance': 0, 'crit damage': 0, 'attack speed': 0, 'health': 2, 'defense': 0, 'speed': 1,
         'intelligence': 35},
        {'strength': 0, 'crit chance': 0, 'crit damage': 0, 'attack speed': 0, 'health': 2, 'defense': 0, 'speed': 2,
         'intelligence': 65},
        {'strength': 0, 'crit chance': 0, 'crit damage': 0, 'attack speed': 0, 'health': 5, 'defense': 0, 'speed': 2,
         'intelligence': 100}
    ),
    'zealous': (
        {'strength': 1, 'crit chance': 1, 'crit damage': 1, 'attack speed': 0, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': 1},
        {'strength': 2, 'crit chance': 2, 'crit damage': 2, 'attack speed': 0, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': 2},
        {'strength': 2, 'crit chance': 2, 'crit damage': 2, 'attack speed': 0, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': 2},
        {'strength': 3, 'crit chance': 3, 'crit damage': 3, 'attack speed': 0, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': 3},
        {'strength': 5, 'crit chance': 5, 'crit damage': 5, 'attack speed': 0, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': 5}
    ),
    'epic': (
        {'strength': 2, 'crit chance': 0, 'crit damage': 1, 'attack speed': 1, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': 0},
        {'strength': 4, 'crit chance': 0, 'crit damage': 2, 'attack speed': 2, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': 0},
        {'strength': 7, 'crit chance': 0, 'crit damage': 4, 'attack speed': 2, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': 0},
        {'strength': 10, 'crit chance': 0, 'crit damage': 7, 'attack speed': 3, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': 0},
        {'strength': 15, 'crit chance': 0, 'crit damage': 10, 'attack speed': 5, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': 0}
    ),
    'fair': (
        {'strength': 1, 'crit chance': 1, 'crit damage': 1, 'attack speed': 1, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': 1},
        {'strength': 2, 'crit chance': 2, 'crit damage': 2, 'attack speed': 2, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': 2},
        {'strength': 2, 'crit chance': 2, 'crit damage': 2, 'attack speed': 2, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': 2},
        {'strength': 3, 'crit chance': 3, 'crit damage': 3, 'attack speed': 3, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': 3},
        {'strength': 5, 'crit chance': 5, 'crit damage': 5, 'attack speed': 5, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': 5}
    ),
    'fast': (
        {'strength': 1, 'crit chance': 0, 'crit damage': 0, 'attack speed': 2, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': 0},
        {'strength': 2, 'crit chance': 0, 'crit damage': 0, 'attack speed': 4, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': 0},
        {'strength': 4, 'crit chance': 0, 'crit damage': 0, 'attack speed': 7, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': 0},
        {'strength': 7, 'crit chance': 0, 'crit damage': 0, 'attack speed': 10, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': 0},
        {'strength': 10, 'crit chance': 0, 'crit damage': 0, 'attack speed': 15, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': 0}
    ),
    'gentle': (
        {'strength': 0, 'crit chance': 0, 'crit damage': 0, 'attack speed': 1, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': 0},
        {'strength': 0, 'crit chance': 0, 'crit damage': 0, 'attack speed': 2, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': 0},
        {'strength': 0, 'crit chance': 0, 'crit damage': 0, 'attack speed': 4, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': 0},
        {'strength': 0, 'crit chance': 0, 'crit damage': 0, 'attack speed': 7, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': 0},
        {'strength': 0, 'crit chance': 0, 'crit damage': 0, 'attack speed': 10, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': 0}
    ),
    'heroic': (
        {'strength': 3, 'crit chance': 0, 'crit damage': 0, 'attack speed': 1, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': 3},
        {'strength': 6, 'crit chance': 0, 'crit damage': 0, 'attack speed': 2, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': 6},
        {'strength': 10, 'crit chance': 0, 'crit damage': 0, 'attack speed': 2, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': 10},
        {'strength': 15, 'crit chance': 0, 'crit damage': 0, 'attack speed': 3, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': 15},
        {'strength': 20, 'crit chance': 0, 'crit damage': 0, 'attack speed': 5, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': 20}
    ),
    'hurtful': (
        {'strength': 1, 'crit chance': 1, 'crit damage': 1, 'attack speed': 0, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': 0},
        {'strength': 2, 'crit chance': 1, 'crit damage': 1, 'attack speed': 0, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': 0},
        {'strength': 2, 'crit chance': 2, 'crit damage': 2, 'attack speed': 0, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': 0},
        {'strength': 3, 'crit chance': 2, 'crit damage': 2, 'attack speed': 0, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': 0},
        {'strength': 5, 'crit chance': 3, 'crit damage': 3, 'attack speed': 0, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': 0}
    ),
    'legendary': (
        {'strength': 2, 'crit chance': 1, 'crit damage': 1, 'attack speed': 2, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': 3},
        {'strength': 4, 'crit chance': 2, 'crit damage': 2, 'attack speed': 4, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': 7},
        {'strength': 7, 'crit chance': 4, 'crit damage': 4, 'attack speed': 7, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': 12},
        {'strength': 10, 'crit chance': 7, 'crit damage': 7, 'attack speed': 10, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': 18},
        {'strength': 15, 'crit chance': 10, 'crit damage': 10, 'attack speed': 15, 'health': 0, 'defense': 0,
         'speed': 0, 'intelligence': 25}
    ),
    'neat': (
        {'strength': 0, 'crit chance': 1, 'crit damage': 2, 'attack speed': 0, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': 0},
        {'strength': 0, 'crit chance': 2, 'crit damage': 4, 'attack speed': 0, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': 0},
        {'strength': 0, 'crit chance': 4, 'crit damage': 7, 'attack speed': 0, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': 0},
        {'strength': 0, 'crit chance': 7, 'crit damage': 10, 'attack speed': 0, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': 0},
        {'strength': 0, 'crit chance': 10, 'crit damage': 15, 'attack speed': 0, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': 0}
    ),
    'odd': (
        {'strength': 0, 'crit chance': 1, 'crit damage': 1, 'attack speed': 0, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': -5},
        {'strength': 0, 'crit chance': 2, 'crit damage': 2, 'attack speed': 0, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': -10},
        {'strength': 0, 'crit chance': 4, 'crit damage': 4, 'attack speed': 0, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': -18},
        {'strength': 0, 'crit chance': 7, 'crit damage': 7, 'attack speed': 0, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': -32},
        {'strength': 0, 'crit chance': 10, 'crit damage': 10, 'attack speed': 0, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': -50}
    ),
    'rich': (
        {'strength': 0, 'crit chance': 1, 'crit damage': 2, 'attack speed': 0, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': 3},
        {'strength': 0, 'crit chance': 2, 'crit damage': 2, 'attack speed': 0, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': 6},
        {'strength': 0, 'crit chance': 4, 'crit damage': 4, 'attack speed': 0, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': 10},
        {'strength': 0, 'crit chance': 7, 'crit damage': 7, 'attack speed': 0, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': 15},
        {'strength': 0, 'crit chance': 10, 'crit damage': 15, 'attack speed': 0, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': 20}
    ),
    'spicy': (
        {'strength': 1, 'crit chance': 1, 'crit damage': 5, 'attack speed': 1, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': 0},
        {'strength': 2, 'crit chance': 1, 'crit damage': 10, 'attack speed': 2, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': 0},
        {'strength': 2, 'crit chance': 1, 'crit damage': 18, 'attack speed': 4, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': 0},
        {'strength': 3, 'crit chance': 1, 'crit damage': 32, 'attack speed': 7, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': 0},
        {'strength': 5, 'crit chance': 1, 'crit damage': 50, 'attack speed': 10, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': 0}
    ),
    'deadly': (
        {'strength': 1, 'crit chance': 1, 'crit damage': 1, 'attack speed': 0, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': 1},
        {'strength': 2, 'crit chance': 2, 'crit damage': 2, 'attack speed': 0, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': 2},
        {'strength': 4, 'crit chance': 4, 'crit damage': 4, 'attack speed': 0, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': 4},
        {'strength': 7, 'crit chance': 7, 'crit damage': 7, 'attack speed': 0, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': 7},
        {'strength': 10, 'crit chance': 10, 'crit damage': 10, 'attack speed': 0, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': 10}
    ),
    'fine': (
        {'strength': 1, 'crit chance': 1, 'crit damage': 1, 'attack speed': 0, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': 0},
        {'strength': 2, 'crit chance': 2, 'crit damage': 2, 'attack speed': 0, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': 0},
        {'strength': 4, 'crit chance': 2, 'crit damage': 2, 'attack speed': 0, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': 0},
        {'strength': 7, 'crit chance': 3, 'crit damage': 3, 'attack speed': 0, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': 0},
        {'strength': 10, 'crit chance': 5, 'crit damage': 5, 'attack speed': 0, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': 0}
    ),
    'grand': (
        {'strength': 3, 'crit chance': 0, 'crit damage': 0, 'attack speed': 0, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': 0},
        {'strength': 7, 'crit chance': 0, 'crit damage': 0, 'attack speed': 0, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': 0},
        {'strength': 12, 'crit chance': 0, 'crit damage': 0, 'attack speed': 0, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': 0},
        {'strength': 17, 'crit chance': 0, 'crit damage': 0, 'attack speed': 0, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': 0},
        {'strength': 25, 'crit chance': 0, 'crit damage': 0, 'attack speed': 0, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': 0}
    ),
    'hasty': (
        {'strength': 1, 'crit chance': 3, 'crit damage': 0, 'attack speed': 0, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': 0},
        {'strength': 2, 'crit chance': 7, 'crit damage': 0, 'attack speed': 0, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': 0},
        {'strength': 2, 'crit chance': 12, 'crit damage': 0, 'attack speed': 0, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': 0},
        {'strength': 3, 'crit chance': 18, 'crit damage': 0, 'attack speed': 0, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': 0},
        {'strength': 5, 'crit chance': 25, 'crit damage': 0, 'attack speed': 0, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': 0}
    ),
    'rapid': (
        {'strength': 1, 'crit chance': 0, 'crit damage': 5, 'attack speed': 0, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': 0},
        {'strength': 2, 'crit chance': 0, 'crit damage': 10, 'attack speed': 0, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': 0},
        {'strength': 4, 'crit chance': 0, 'crit damage': 18, 'attack speed': 0, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': 0},
        {'strength': 7, 'crit chance': 0, 'crit damage': 32, 'attack speed': 0, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': 0},
        {'strength': 10, 'crit chance': 0, 'crit damage': 50, 'attack speed': 0, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': 0}
    ),
    'unreal': (
        {'strength': 2, 'crit chance': 2, 'crit damage': 2, 'attack speed': 0, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': 0},
        {'strength': 4, 'crit chance': 4, 'crit damage': 4, 'attack speed': 0, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': 0},
        {'strength': 7, 'crit chance': 7, 'crit damage': 7, 'attack speed': 0, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': 0},
        {'strength': 10, 'crit chance': 10, 'crit damage': 10, 'attack speed': 0, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': 0},
        {'strength': 15, 'crit chance': 15, 'crit damage': 15, 'attack speed': 0, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': 0}
    ),
    'bizarre': (
        {'strength': 1, 'crit chance': -1, 'crit damage': -1, 'attack speed': 0, 'health': 1, 'defense': 0, 'speed': 0,
         'intelligence': 3},
        {'strength': 2, 'crit chance': -2, 'crit damage': -2, 'attack speed': 0, 'health': 1, 'defense': 0, 'speed': 0,
         'intelligence': 6},
        {'strength': 2, 'crit chance': -2, 'crit damage': -2, 'attack speed': 0, 'health': 1, 'defense': 0, 'speed': 0,
         'intelligence': 10},
        {'strength': 3, 'crit chance': -3, 'crit damage': -3, 'attack speed': 0, 'health': 1, 'defense': 0, 'speed': 0,
         'intelligence': 15},
        {'strength': 5, 'crit chance': -5, 'crit damage': -5, 'attack speed': 0, 'health': 1, 'defense': 0, 'speed': 0,
         'intelligence': 20}
    ),
    'itchy': (
        {'strength': 1, 'crit chance': 0, 'crit damage': 3, 'attack speed': 1, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': 0},
        {'strength': 2, 'crit chance': 0, 'crit damage': 5, 'attack speed': 2, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': 0},
        {'strength': 2, 'crit chance': 0, 'crit damage': 8, 'attack speed': 2, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': 0},
        {'strength': 3, 'crit chance': 0, 'crit damage': 12, 'attack speed': 3, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': 0},
        {'strength': 5, 'crit chance': 0, 'crit damage': 0, 'attack speed': 5, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': 0}  # !!!
    ),
    'ominous': (
        {'strength': 1, 'crit chance': 0, 'crit damage': 1, 'attack speed': 0, 'health': 1, 'defense': 1, 'speed': 0,
         'intelligence': 1},
        {'strength': 2, 'crit chance': 0, 'crit damage': 2, 'attack speed': 0, 'health': 2, 'defense': 2, 'speed': 0,
         'intelligence': 2},
        {'strength': 2, 'crit chance': 0, 'crit damage': 2, 'attack speed': 0, 'health': 2, 'defense': 2, 'speed': 0,
         'intelligence': 2},
        {'strength': 3, 'crit chance': 0, 'crit damage': 3, 'attack speed': 0, 'health': 3, 'defense': 3, 'speed': 0,
         'intelligence': 3},
        {'strength': 5, 'crit chance': 0, 'crit damage': 5, 'attack speed': 0, 'health': 5, 'defense': 5, 'speed': 0,
         'intelligence': 5}
    ),
    'pleasant': (
        {'strength': 0, 'crit chance': 0, 'crit damage': 1, 'attack speed': 1, 'health': 1, 'defense': 1, 'speed': 0,
         'intelligence': 1},
        {'strength': 0, 'crit chance': 0, 'crit damage': 2, 'attack speed': 1, 'health': 1, 'defense': 2, 'speed': 0,
         'intelligence': 2},
        {'strength': 0, 'crit chance': 0, 'crit damage': 2, 'attack speed': 1, 'health': 2, 'defense': 2, 'speed': 0,
         'intelligence': 2},
        {'strength': 0, 'crit chance': 0, 'crit damage': 3, 'attack speed': 1, 'health': 2, 'defense': 3, 'speed': 1,
         'intelligence': 3},
        {'strength': 0, 'crit chance': 0, 'crit damage': 5, 'attack speed': 1, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': 0}  # !!!
    ),
    'pretty': (
        {'strength': 0, 'crit chance': 0, 'crit damage': 0, 'attack speed': 1, 'health': 1, 'defense': 0, 'speed': 0,
         'intelligence': 3},
        {'strength': 0, 'crit chance': 0, 'crit damage': 0, 'attack speed': 2, 'health': 2, 'defense': 0, 'speed': 0,
         'intelligence': 6},
        {'strength': 0, 'crit chance': 0, 'crit damage': 0, 'attack speed': 2, 'health': 2, 'defense': 0, 'speed': 1,
         'intelligence': 10},
        {'strength': 0, 'crit chance': 0, 'crit damage': 0, 'attack speed': 3, 'health': 3, 'defense': 0, 'speed': 1,
         'intelligence': 15},
        {'strength': 0, 'crit chance': 0, 'crit damage': 0, 'attack speed': 5, 'health': 5, 'defense': 0, 'speed': 0,
         'intelligence': 20}  # !!!
    ),
    'shiny': (
        {'strength': 0, 'crit chance': 0, 'crit damage': 0, 'attack speed': 0, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': 0},
        {'strength': 0, 'crit chance': 0, 'crit damage': 0, 'attack speed': 0, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': 0},
        {'strength': 0, 'crit chance': 0, 'crit damage': 0, 'attack speed': 0, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': 0},
        {'strength': 0, 'crit chance': 0, 'crit damage': 0, 'attack speed': 0, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': 0},
        {'strength': 0, 'crit chance': 0, 'crit damage': 0, 'attack speed': 0, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': 0}  # !!!
    ),
    'simple': (
        {'strength': 1, 'crit chance': 0, 'crit damage': 0, 'attack speed': 0, 'health': 1, 'defense': 1, 'speed': 0,
         'intelligence': 0},
        {'strength': 1, 'crit chance': 0, 'crit damage': 0, 'attack speed': 0, 'health': 1, 'defense': 1, 'speed': 0,
         'intelligence': 0},
        {'strength': 1, 'crit chance': 0, 'crit damage': 0, 'attack speed': 0, 'health': 1, 'defense': 1, 'speed': 0,
         'intelligence': 0},
        {'strength': 1, 'crit chance': 0, 'crit damage': 0, 'attack speed': 0, 'health': 1, 'defense': 1, 'speed': 0,
         'intelligence': 0},
        {'strength': 1, 'crit chance': 0, 'crit damage': 0, 'attack speed': 0, 'health': 1, 'defense': 1, 'speed': 0,
         'intelligence': 0}
    ),
    'strange': (
        {'strength': 1, 'crit chance': 1, 'crit damage': 1, 'attack speed': 1, 'health': 0, 'defense': 1, 'speed': 0,
         'intelligence': -5},
        {'strength': 2, 'crit chance': 2, 'crit damage': 2, 'attack speed': 2, 'health': 0, 'defense': 1, 'speed': 0,
         'intelligence': -10},
        {'strength': 1, 'crit chance': 1, 'crit damage': 1, 'attack speed': 1, 'health': 0, 'defense': 1, 'speed': 0,
         'intelligence': -18},
        {'strength': 1, 'crit chance': 1, 'crit damage': 1, 'attack speed': 1, 'health': 0, 'defense': 1, 'speed': 0,
         'intelligence': -32},
        {'strength': 0, 'crit chance': 0, 'crit damage': 0, 'attack speed': 0, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': 0}  # !!!
    ),
    'vivid': (
        {'strength': 1, 'crit chance': 0, 'crit damage': 0, 'attack speed': 0, 'health': 1, 'defense': 1, 'speed': 0,
         'intelligence': 0},
        {'strength': 1, 'crit chance': 0, 'crit damage': 0, 'attack speed': 0, 'health': 2, 'defense': 1, 'speed': 0,
         'intelligence': 0},
        {'strength': 1, 'crit chance': 0, 'crit damage': 0, 'attack speed': 0, 'health': 2, 'defense': 1, 'speed': 1,
         'intelligence': 0},
        {'strength': 2, 'crit chance': 0, 'crit damage': 0, 'attack speed': 0, 'health': 2, 'defense': 1, 'speed': 1,
         'intelligence': 0},
        {'strength': 0, 'crit chance': 0, 'crit damage': 0, 'attack speed': 0, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': 0}  # !!!
    )
}
