---
# cSpell:locale fr, en
alias: cmd-option-fr
---
# OPTION

**`OPTION`**` `*`option`*`[NOT]`  

<!-- TODO: check if the following options stay in german or not for english players -->

These options can be turned on and off. You control exactly what the evaluation looks like.

- `AUSWERTUNG`: This is the normal evaluation in plain text. If you only use the computer evaluation, the normal evaluation can be omitted
- `COMPUTER`: This evaluation is easier for programs to read. It can be used to power any kind of self-written programs, e.g. auxiliary tools or map drawers
- `ZIPPED`: The evaluation will be packed with zip before shipping
- `BZIP2`: The evaluation is packed with bzip2 before shipping
- `STATISTIK`: With this option, a small statistic is displayed after each region in the normal analysis
- `PUNKTE`: With this option, from the 13th round at the earliest, a score is issued that allows a small comparison with other factions
- `ZUGVORLAGE`: A separate file contains a [[orders|Template for the next round's orders]]. This can be turned off and on again. If you don't need this, for example because you use a tool to create a move, you should turn off the move template
- `TALENTVERSCHIEBUNG`: This allows you to switch on a small display in the NR. After the skill it is listed if the skill has changed in the round in question
- `ADRESSEN`: This appends the address list of the factions seen in the group to the report

## Anciennes options

With evaluation number 559, the Material Pool and Silver Pool options were set as default. Deactivation is no longer possible.

`SILVERPOOL`: Typically, units pay expenses incurred “out of pocket.” This option can be used to ensure that necessary Silver is collected from all units in the region.

`MATERIALPOOL`: If the [[items-pool|Material Pool]] is switched on, all required items in a unit are collected as needed, similar to Silver with the [Silver Pool]. Units can use the [[cmd-reserve]] command to secure items, preventing other units from taking them and consuming them. This option should be used carefully, as you can quickly, for example, use all the wood in a region that you had planned for other purposes, just because you have one`RESERVE`forgot.

<!-- From [https://wiki.eressea.de/index.php?title=OPTION&oldid=16703] -->

[Silver Pool]: ./items-pool.md#reserve-dargent
