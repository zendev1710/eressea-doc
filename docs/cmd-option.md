---
# cSpell:locale en
alias: cmd-option
---
<!-- disable MD052 because of mkdocs autorefs plugin usage -->
<!-- markdownlint-disable MD052 -->
# OPTION

**OPTION**&nbsp;ADDRESSES|COMPUTER|PLAINTEXT|SCORE|SHOWSKCHANGE|STATISTICS|TEMPLATE&nbsp;&#91;NOT&#93;  
**OPTION**&nbsp;ZIPPED|BZIP2  

<!-- TODO: check if the following options stay in german or not for english players -->

These options can be turned on and off (With the exception of the `ZIPPED` and `BZIP2` ones).
With them, you control exactly what the evaluation looks like.  

!!! info "Information"
    Les options et leur statut sont renseignés en allemand dans le rapport informatique (`.cr`) de l'évaluation :
    ```text
    OPTIONEN
    1;AUSWERTUNG
    1;COMPUTER
    1;ZUGVORLAGE
    1;STATISTIK
    1;ZIPPED
    1;ADRESSEN
    0;BZIP2
    1;PUNKTE
    0;SHOWSKCHANGE
    ```

The available options are described below.

## `OPTION ADDRESSES`

**OPTION**&nbsp;ADDRESSES &#91;NOT&#93;  

With this option enabled, the list of email addresses of the factions seen in the round wil be appended to the report.

## `OPTION COMPUTER`

**OPTION**&nbsp;COMPUTER &#91;NOT&#93;  

This evaluation is easier for programs to read.  
It can be used to power any kind of self-written programs, e.g. auxiliary tools or map drawers.  

## `OPTION PLAINTEXT`

**OPTION**&nbsp;PLAINTEXT &#91;NOT&#93;  

This is the normal evaluation (`.nr` file) in plain text.  
If you only use the computer evaluation (`.cr` file), the normal evaluation can be omitted.  

## `OPTION SCORE`

**OPTION**&nbsp;SCORE &#91;NOT&#93;  

With this option enabled, **from the 13th round at the earliest**, a score is issued that allows a small comparison with other factions.

## `OPTION SHOWSKCHANGE`

**OPTION**&nbsp;SHOWSKCHANGE &#91;NOT&#93;  

With this option enabled, a small display will be added in the NR.  
After the skill it is listed if the skill has changed in the round in question  

## `OPTION STATISTICS`

**OPTION**&nbsp;STATISTICS &#91;NOT&#93;  

With this option enabled, a small statistic is displayed after each region in the normal report (`.nr` file).

## `OPTION TEMPLATE`

**OPTION**&nbsp;TEMPLATE &#91;NOT&#93;  

With this option enabled, a separate file will contains a [[orders|template for the next round's orders]].  
If you don't need this, for example because you use a tool to edit orders, you should turn off the template option.  

## `OPTION ZIPPED|BZIP2`

**OPTION**&nbsp;ZIPPED  
**OPTION**&nbsp;BZIP2  

- `OPTION ZIPPED`: The evaluation will be packed with `zip` before shipping
- `OPTION BZIP2`: The evaluation is packed with `bzip2` before shipping

## Deprecated options

With evaluation number 559, the Material Pool and Silver Pool options were set as default.  
**Deactivation is no longer possible**.  

- `SILVERPOOL`: Typically, units pay expenses incurred “out of pocket.” This option can be used to ensure that necessary Silver is collected from all units in the region.
- `MATERIALPOOL`: If the [[items-pool|Material Pool]] is switched on, all required items in a unit are collected as needed, similar to Silver with the [Silver Pool].
  Units can use the [[cmd-reserve]] order to secure items, preventing other units from taking them and consuming them.
  This option should be used carefully, as you can quickly, for example, use all the wood in a region that you had planned for other purposes, just because you have forgot one `RESERVE`.

<!-- From [https://wiki.eressea.de/index.php?title=OPTION&oldid=16703] -->

[Silver Pool]: ./items-pool.md#the-silver-pool
