---
# cSpell:locale en
alias: quickstart
---

[](){ #quickstart-id }

# Quick start

This page gives you the minimum to play your first weeks in Eressea.  
For a complete guided example with a real report and orders file, see [The first round][first-round].  
For general advice, see [Beginner tips][beginner-tips].

## 1. Subscribe

Send an email to [eressea-server@kn-bremen.de](mailto:eressea-server@kn-bremen.de) with the subject `ERESSEA SUB` and your desired race (see [Races][races]).  
You will receive your first report with your [faction][factions] number, password and your starting unit.

## 2. Read your report

Every week you receive two reports with the same data:

- the **normal report** (NR) — a text file readable with any editor;
- the **computer report** (CR) — a file understood by tools like [Magellan][magellan-id] and [CSMap][csmap-id].

Beginners should use the normal report and a text editor: the first orders are rarely more than a dozen lines.

## 3. Write your orders

Answer to the server with the subject `ERESSEA <faction> ORDERS`, containing:

```text
ERESSEA 37wj "your-password"
REGION 0,0
UNIT vdko
    NAME FACTION "The Dragon Clan"
    PASSWORD "a-new-password"
    LEARN Forestry
    WORK
```

A unit can only perform **one long order** per week, but any number of short ones.  
See [Long and short orders][short-and-long-orders] and the [orders list][commands-list].

!!! warning "Danger"
    [Combat][combat-id] can be a long action, even if you haven't attacked yourself: a battle in a region you don't [guard][cmd-guard] blocks the long order of **all** attacked units. Guard your regions from the first week you can be attacked.

## 4. Survive

- **Hunger kills**: each person needs 10 silver maintenance per week. Avoid [starvation][starvation] at all costs.
- **Earn silver**: [`ENTERTAIN`][cmd-entertain] and [`TAX`][cmd-tax] are the quickest income; use [`WORK`][cmd-work] only in an emergency.
- **Recruit and learn**: create units with [`MAKE TEMP`][cmd-make] + [`RECRUIT`][cmd-recruit] + [`LEARN`][cmd-learn].
- **Explore**: send single-person units to discover mountain and forest regions (ore and wood).

## 5. Use the tools

- [Magellan][magellan-id] reads the CR, displays it clearly and helps create orders.
- [ECheck][echeck-id] checks the spelling and parameter order of your orders; the server runs it automatically on incoming moves.

## Next steps

- [The first round][first-round] — a complete example with a real report and orders file.
- [Beginner tips][beginner-tips] — what to do (and avoid) in the first weeks.
- [Orders sequence][orders-sequence] — the fixed order in which the server evaluates your orders.
- [Skills][skills] — how learning and teaching work.

[races]: races.md "Races"
[factions]: factions.md "Factions and units"
[first-round]: first-round.md "The first round"
[beginner-tips]: tips.md "Beginner tips"
[magellan-id]: ../tools/desktop/magellan.md "Magellan"
[csmap-id]: ../tools/desktop/csmapfx.md "CSMap"
[short-and-long-orders]: ../combat/armed.md "Long and short orders"
[combat-id]: ../combat/war.md "Combat"
[cmd-guard]: ../orders/guard.md "GUARD"
[starvation]: factions.md "Starvation"
[cmd-entertain]: ../orders/entertain.md "ENTERTAIN"
[cmd-tax]: ../orders/tax.md "TAX"
[cmd-work]: ../orders/work.md "WORK"
[cmd-make]: ../orders/make.md "MAKE TEMP"
[cmd-recruit]: ../orders/recruit.md "RECRUIT"
[cmd-learn]: ../orders/learn.md "LEARN"
[commands-list]: ../orders/list.md "Orders list"
[orders-sequence]: ../orders/sequence.md "Orders sequence"
[skills]: ../skills/skills.md "Skills"
[echeck-id]: ../tools/cli/echeck.md "ECheck"
