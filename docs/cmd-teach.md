---
# cSpell:locale en
alias: cmd-teach
---
# TEACH

**`TEACH`**[<sup>`L`</sup>]` `*`unit-id`*`[`*`unit-id`*`]...`  

To reduce the time it takes for another unit to learn a skill, you can teach them the skill.
To do this, the teaching unit must be at least 2 levels better than the learning unit in the skill in question.
This means that the learning unit learns twice as quickly as if it tried to improve its skill on its own.

This order teaches all listed units the skill they are currently learning.
So the students have to learn while the teacher teaches.
More than one entity can be listed. However, a teacher unit can only allow 10 students per person and round to benefit from their knowledge.
Several teachers can also teach a large group of students.

The skill to be taught must **not** be specified - the skill that the learning unit learns is automatically taught.
These can also be different skills, provided the teacher has mastered these skills sufficiently better than the students.

If you want to teach units from other factions, you must have received the [[cmd-help|`HELP GUARD`]] order from that faction or the unit to be taught must contact the teacher with [[cmd-contact]].

**Example**:

```text
TEACH xxxx yyyy TEMP 2 zzzz
```

Through the [[cmd-learn-auto]] order, the server attempts to automate learning and teaching in a region within a faction.
A mixture of `TEACH` and `LEARN AUTO`, however, is not possible.

<!-- From [https://wiki.eressea.de/index.php?title=TEACH&oldid=16726] -->

[<sup>`L`</sup>]: ./commands.md#short-and-long-orders
