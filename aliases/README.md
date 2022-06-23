# Mudlet Aliases
Collection of useful, non-trivial aliases.

### bk.xml
Drow only: Casts the `bleakness` spell on a target, but only in keeps,
dungeons, and underground areas. without this alias, the game will waste time
and spellpower casting the spell, yet it has no effect. when outside of the
aforementioned areas, this alias prints a message indicating that `bleakness`
cannot be cast in the current area.

In keep/dungeon/underground:
```
<3985hp 3645sp 2939st>bk guard
cast bleakness guard
You begin to speak the words of the spell...
You have completed your casting.
You invade an alert castle guard's mind, filling him with misery and loathing.
```

Anywhere else:
```
<3985hp 3645sp 2940st>bk

<<< NO BLEAKNESS OR 45% SP-REGEN BONUS HERE: Alyria >>>
```

### cn.xml
Psionic only: Casts the `cancellation` spell for a given school of magic, but
does so using a clickable menu. because the school names are complex and
difficult to remember, the alias prints out all available schools, and the
user can select the correct choice.
```
<3984hp 3645sp 2940st>cn
Aeromancy, Anthropomancy, Aquamancy, Artemancy, Arthropomancy, Astromancy, Bestiamancy, Chaosmancy
Chromatomancy, Chronomancy, Coromancy, Cruciomancy, Destructomancy, Diamancy, Dreadmancy, Electromancy
Ferromancy, Geomancy, Glaciomancy, Hematomancy, Hydromancy, Lavamancy, Lutomancy, Magmamancy
Metamancy, Morphomancy, Negamancy, Neuromancy, Noxomancy, Papyrimancy, Pyromancy, Retromancy
Sanctomancy, Stupomancy, Terramancy, Umbramancy, Unimancy, Velocimancy, Veritamancy, Vivomancy
```

### frp.xml
Formation member only: similar to the in game `report` command, this alias
reports current and maximum hp/sp/st onto the formation talk channel. These
values are colored red, cyan, and green, respectively. The announcement can be
made to other channels with a minor code modification.
```
<3927hp 3466sp 2740st>frp
You tell the formation '3927/3985hp 3466/3645sp 2740/2941st'
```

### hw.xml
Displays a menu of weapons and a brief description of each. Each weapon is a
clickable link that swaps the current weapon for the selected weapon, putting
the just removed weapon into your first trunk. consumers of this alias should
hand edit the file to describe their own weapons. Though is that lack of trunk
should specify a different container keyword within the code.
```
<3934hp 3506sp 2777st>hw
manrikigusari: exotic bash, -ar scripts, echoing strike
otherwhat:     exotic bash, attack script, echoing strike
elements:      mace bash, battering
cacti:         dart pierce, deliberately untrained and weak
guillotine:    yo-yo bash, lightning-skill-res, parry magic
parasol:       exotic corruption, extra dmg, overloading
decara:        lance pierce, align +350, no decay
heavenfire:    dagger holy, remove-in-safe, flaming
weeping:       sword slash, no decay, frost
malicious:     lance sunlight, align -350, vampiric
ardor:         sword mental, vorpal
tourmaline:    lance earth, no decay, vorpal
manari:        lance pierce, balrog script, serrated
pilum:         spear air, extra dmg, vorpal
boulders:      dagger pierce, conjure boulder
tusk:          exotic pain, piercing, serrated
```

### rlt.xml
Converts Alyrian time to real time. Does not interact with the game; local only.
```
rlt 60 -> 60 AL min = 15 RL min
rlt 75 -> 75 AL min = 18.75 RL min
```

### rm.xml
Announces the current room on the specified (preceding) talk
channel. This includes the room name, coordinates, and room ID when indoors.
When outdoors, the output includes all of the indoor information, plus the
iconography of the outdoor room, which is properly colored.

Indoors:
```
<3985hp 3645sp 2929st>ft rm;
You tell the formation 'Maldra Keep (1304, 1092) - Entrance to Maldra Keep R#67835'
```

Outdoors:
```
<3985hp 3645sp 2929st>ft rm;
You tell the formation 'Alyria (1304, 1092) - Lord Maldra's Road R#3573738 as #'
```

### warp.xml
Archon only: casts the `warp` spell to a given destination, but does so using
a clickable menu. Like the `cancellation` alias just described, warp locations
are tedious to type and remember, so clicking a target destination improves
quality of life.
```
<3985hp 3645sp 2941st>warp
Arcane Archipelago, Ariendyth, Atlantis, Genauras, Hellbent Mountain, Lowangen, Magencia, Ogre Village
Muldar Lohk Mulvar, Naulitas, New Kolvir, New Rigel, Palace of Diocletian, Pirate's Cove, Rune, Rune Forest
Sigil, Tellerium, Templeton, Vir, Vospire, Winterborn Mansion, Wreck of the Feisty Wench, Xaventry
Catacombs of Shame, Hotel Hello, Inconvenience, Kessarian, Maldra, Sea Hag, (only use with warp skp)
```

### wor.xml
Casts the `word of recall` spell, but only in rooms not marked as `no-recall`.
if the room is marked as `no-recall`, the user is notified that the spell
cannot be cast here, much like `bleakness`.

In `no-recall` rooms:
```
<3985hp 3645sp 2916st>lua gmcp.room.info.flags
"indoors, no-recall"

<3985hp 3645sp 2916st>wor

<<< NO RECALLING HERE >>>
```

Anywhere else:
```
<3985hp 3645sp 2917st>lua gmcp.room.info.flags
"indoors"

<3985hp 3645sp 2917st>wor
You begin to speak the words of the spell...
You have completed your casting.
You feel a rushing sense of motion...
```

### xnum.xml
Runs the following command the specified number of times. this is useful when
a player needs to collect many items from a container, but not all of them. It
can also be used for navigation.
```
> x3 get fish blue
You take a shimmering white fish scale from a blue silk bag.
You take a shimmering white fish scale from a blue silk bag.
You take a shimmering white fish scale from a blue silk bag.
```
