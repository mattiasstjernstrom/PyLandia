## Entities
Common for all enemies are basic attributes such as hit points and attack values. Depending on how the combat methods shake out we might also want to have defensive values, resource points (ex: stamina, mana) to limit ability use, speed / initiative value to determine order during combat.

### Player
The player entity should be more complex than other entities to allow for player costumization if we can afford it. An inventory could be used if we implement weapons, armour, and other equipment mechanics.

We could track progression through use of experience points or something similar to allow from stat increases.

Abilities might be general, unlocked from a shared 'skill-tree', or tied to particular classes chosen during character creation or during progression.

### Enemies
We won't have to make enemies as complex as the player entity since they won't be tracked throughout the game or progress, with possible exception if we make a reccuring villain that shows up several times throughout the game.

If we implement a progress system we might want to track how much each defeated enemy adds to the player's progression and vary it depending on difficulty. If we add equipment / inventories we can have each enemy carry a table of possible loot drops.