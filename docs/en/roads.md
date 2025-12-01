# Road

**Roads** increase the travelling speed over land. To achieve this, there must be inclusive roads from the start to the destination region. These roads allow easy progress as they do not become boggy when it rains, are not overgrown by forest and rivers and ravines are spanned by bridges.

In each region, you can build a road to the six cardinal directions. For a road to be complete, there must be a road in the region of the corresponding direction in the opposite direction. To build roads, you need a minimum level of 1 in roadwork, and you can add 1 stone per level (and per person in the unit).

The following table states how many stones per direction are needed. Furthermore, some regions are so inhospitable that a [building] is required before building a road. It must function while building it, that is, it must be completed and the maintenance costs must be paid. Once completed, the road works without paying the building maintenance.

|     |     |     |
| --- | --- | --- |Building Roads
| Terrain | Stones | Building |
| Plain/Forest | 50  | \-  |
| Highland | 100 | \-  |
| Mountain | 250 | \-  |
| Volcano | 250 | \-  |
| Swamp | 75  | [Dam] |
| Desert | 100 | [Caravanserai] |
| Glacier | 250 | [Tunnel] |

[Dam]: ./buildings-others.md#Damm "Andere Gebäude"
[Caravanserai]: ./buildings-others.md#Karawanserei "Andere Gebäude"
[Tunnel]: ./buildings-others.md#Tunnel "Andere Gebäude"

**Example:** For building a road from the plain at (0,0) through the swamp at (1,0) to the mountain at (1,1) you need

- 50 stones for `MAKE Road E` in (0,0)
- a dam in (1,0) that functions during construction costing 1000 silver and 3 wood per round
- 75 stones for `MAKE Road W` in (1,0)
- 75 stones for `MAKE Road NE` in (1,0)
- 250 stones for `MAKE Road SW` in (1,1)

After completion a unit can travel on foot with `MOVE E NE` from (0,0) to (1,1) in one round.

|     |     |
| --- | --- |
| Continue reading: | [Ships] |

[Ships]: ./ships.md "Schiff"

<!-- From [https://wiki.eressea.de/index.php?title=Straße/en&oldid=15936] -->

[building]: ./buildings-others.md "Andere Gebäude"
