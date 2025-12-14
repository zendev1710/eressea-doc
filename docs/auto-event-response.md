---
alias:
    name: auto-event-response
    text: Automated event response
---
# Automated event response

Many events in Eressea are random or influenced by other players.
To avoid missing such events, or better yet, to react appropriately to them, you first need to decide which events you want to discover and how to do so.

## Messages

Many events can be easily identified by checking the messages – triggered magical effects, appearing monsters, battles, hunger, etc.

In most cases, it's sufficient to search for the message type and use the message's attributes.

## Comparison

Unfortunately, everything else can usually only be verified by comparing the current state with the event condition.
This includes the presence of certain units or races, the passage of unknown units or ships, etc.

## Priority

In principle, it is advisable to assign a priority to events and then process them according to that priority.

## Reaction

Once the events have been prioritized, the next step is to identify the affected units so they can potentially react to the event.
Despite prioritization, reacting to multiple events is difficult, as secondary events may also influence a unit's commands.

<!-- TODO: replace outdaed example, the current remains here until a suitable alternative example is created -->
***outdated example***: starvation no longer prevents long commands.
Example: a unit is starving and undead appear. Starvation should have higher priority here, as it forces the long WORK command.
This naturally limits the possible reactions to the undead event.
Moving to the adjacent region is no longer possible.

However, it is possible to set the combat status.
Depending on whether you have the upper hand or the lower hand, different reactions are necessary.

<!-- From [https://wiki.eressea.de/index.php?title=Automatisierung\_Ereignissreaktion&oldid=6434] -->
