# Mudlet Triggers
Collection of useful, non-trivial triggers.

### aff_clear.xml
Click the left-justified red `[x]` to rapidly clear a given beneficial affect.
```
<3990hp 3645sp 2904st>affects
You are affected by the following:
[x] Spell:      haste                       - Level 208, modifies attack-speed         by   15.
[x] Spell:      improved invisibility       - Level  30, modifies none                 by    0.
[x] Spell:      bless                       - Level 241, modifies saving-spell         by    4 for 304 minutes.
[x] Spell:      protection from evil        - Level 241, modifies none                 by    0 for 304 minutes.
[x] Spell:      armor                       - Level 241, modifies ar                   by    3 for 304 minutes.
[x] Spell:      pense                       - Level 241, modifies none                 by    0 for 305 minutes.
[x] Spell:      fireshield                  - Level 105, modifies none                 by    0.[  -5 sp        ]
[x] Affect:     cover of darkness           - Level 241, modifies mental-skill-dam     by    3 for 305 minutes.
[x] Spell:      levitation                  - Level 241, modifies none                 by    0 for 305 minutes.
[x] Spell:      enhanced strength           - Level 400, modifies strength             by    5 for 463 minutes.
[x] Spell:      rime of the glacierbreaker  - Level 241, modifies drowning-melee-dam   by    9 for 131 minutes.
[x] Spell:      force field                 - Level 241, modifies ar                   by    9 for 603 minutes.
```

### average_ar.xml
Displays overall average AR across all categories. Can be easily extended to
races with wings, tails, or both.
```
<3990hp 3645sp 2926st>eq
Current Armor Resistance (AR):
(Head    ) Pierce: 121  Bash: 118  Slash: 120  Exotic: 119
(Torso   ) Pierce: 120  Bash: 117  Slash: 121  Exotic: 117
(Arms    ) Pierce: 108  Bash: 104  Slash: 107  Exotic: 105
(Legs    ) Pierce: 108  Bash: 104  Slash: 107  Exotic: 105  avg ar: 112
```

### check_eq.xml
Creates a clickable `[STUDY]` link for EQDB UUIDs, making referencing easier.
```
[STUDY]Vierna tells you: 'check equipment scrying 123d24d7bace468dece0412ae02af8ea048df1ca92078e104e6b54d0fcb025a9'
```

### combat_trim_in.xml
Shortens combat text to damage sustained as shown below. Colors are retained with
additional highlights for weaknesses (red) or resistances (cyan).
```
< minimal slash to head
< slight flames to arm
```

### combat_trim_out.xml
Shortens combat text to damage dealt as shown below. Colors are retained and
fireshield can optionally be enabled/disabled to reduce clutter.
```
> trifling bash to torso
> paltry pain to arm
```

### aff_hide_racial.xml
Hides persistent racial affects that players don't need to see constantly. As a Drow, for example, these affects are hidden:
```
Racial:     wily                        - Level 241, modifies charm-skill-res      by   25.
Racial:     wily                        - Level 241, modifies charm-melee-res      by   25.
Racial:     urged                       - Level 241, modifies necromantic-skill-re by   25.
Racial:     urged                       - Level 241, modifies necromantic-melee-re by   25.
Racial:     fractured                   - Level 241, modifies holy-skill-res       by  -25.
Racial:     fractured                   - Level 241, modifies holy-melee-res       by  -25.
```

### ship_winds.xml
Compares the direction of a ship with the direction of the wind, and makes
recommendations regarding whether to sail or steam. Also, displays the number
of rooms traversed at each screen refresh.

```
You spin the steering wheel until the ship is facing northwest.
(260hull NWdir STOP NWwind 100%shld 1540, 506) moved=0 / head wind; use steam

You spin the steering wheel until the ship is facing north.
(260hull Ndir STOP NWwind 100%shld 1540, 506) moved=0 / bow wind; use steam

You spin the steering wheel until the ship is facing northeast.
(260hull NEdir STOP NWwind 100%shld 1540, 506) moved=0 / beam wind; use sail or steam

You spin the steering wheel until the ship is facing east.
(260hull Edir STOP NWwind 100%shld 1540, 506) moved=0 / quarter wind; use sail

You spin the steering wheel until the ship is facing southeast.
(260hull SEdir STOP NWwind 100%shld 1540, 506) moved=0 / tail wind; use sail

You spin the steering wheel until the ship is facing south.
(260hull Sdir STOP NWwind 100%shld 1540, 506) moved=0 / quarter wind; use sail

You spin the steering wheel until the ship is facing southwest.
(260hull SWdir STOP NWwind 100%shld 1540, 506) moved=0 / beam wind; use sail or steam

You spin the steering wheel until the ship is facing west.
(260hull Wdir STOP NWwind 100%shld 1540, 506) moved=0 / bow wind; use steam
```

The `moved` value shows the number of rooms traversed.
```
Ship speed has been set to FLANK.
Musaqala's Corsair sails east.
(260hull Edir FLANK NWwind 100%shld 1551, 503) moved=13 / quarter wind; use sail
```

Based on testing in a velocity-boosted corsair, these are the approximate
`moved` values based on wind direction, assuming sails are in use.

```
tailwind: 15
quarter: 13
beam: 9
bow: 6
headwind: 3
```

### spell_efficiency1.xml
Computes sp:dmg ratio, scaled by 1000, using non-parenthetical `base` text.
```
<3973hp 3645sp 2896st>help channel faith
[1955 ] CHANNEL FAITH
(snip)
*Spell Points Required: 89
*Default affect modifier: There is a (caster's level / 350)% chance to shoot two projectiles instead of one.
*Has a base multiplier of 4.0. sp to dmg efficiency (higher is better): 44.94
```

### spell_efficiency2.xml
Computes sp:dmg ratio, scaled by 1000, using parenthetical `base` text.
```
<3973hp 3645sp 2896st>help telekinetic punch
[1582 ] TELEKINETIC PUNCH
(snip)
*Spell Points Required: 65
*Default affect modifier: There is a (caster's level / 350)% chance to shoot two projectiles instead of one.
*Deals emotional/surprise (2.2 base) damage. sp to dmg efficiency (higher is better): 33.85
```

### unlock_door.xml
Creates clickable, color-coded links to make opening locked doors easier.
Green text is clickable, red text is not; this differentiates viable options.

```
<3990hp 3591sp 2811st>look west
The door is closed. Options for west door: pick pass bash magic-unlock knock
Judging by the lock, the door could be opened by an enchanted ash key.
```

### who_links.xml
Creates quick links for `cast teleview`, `check who`, and `check religion` for
all players displayed by `who`.
```
<3990hp 3645sp 2941st>who
[Tview][Class][Relig] [119:241   Archon   ] Musaqala [*Oracle*][Duelist]
[Tview][Class][Relig] [168:241   Chrono   ] Vierna [EuphoriA][Duelist]
```

### lunar_sp.xml
Estimates the lunar impact on spellpoint (sp) regeneration and appends
the result after the moon phases.

```
<3000hp 3350sp 2850st>time
It is 10:47 am on Monday, September the 29th, year 1502.
The twin moons, Trigael and Marabah are in the phases:
Trigael: (half waning)  Marabah: (gibbous waning)  SP regen: 101%
```
