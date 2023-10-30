### Basic combat loop

1. Initialise combat class with player and enemy entity
2. Player chooses action through input
3. Run function based on player input
4. If enemy is still alive it attacks players, else player wins and combat ends.
5. If player is still alive go to step 2, else enemy loses and combat ends (and game?).

![picture](/Resources/basic_combat_loop.png)

### Possible additions to mechanics
* Abilities use coding puzzles to determine effectiveness.
* Enemies have abilities and make choices.
* Adding usable items to player choices.
* Multiple combatants to either side.
    * Friendly entities controlled by player or autopilot?
* Incorporating rudimentary positioning by way of 'state' attributes (areas, distances, safety)?
    * Would require maneuvers among choices.
    * ex: You can only use a ranged ability while 'safe' or 'far'.
    * ex: You can only hit multiple targets if they share an area.
    * ex: Melee weapons may only be used against targets in the same area as attacker, or in 'near' distance.