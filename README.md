# # Pokémon: Battle Factory
**README.md (Use markdown syntax if you want), which is a text file that
describes the following:
Your game
How to play your game
Describe your code**
The game takes inspiration from the Battle Factory, which is an installation of the Battle Frontier in the Gameboy Advanced game, Pokémon Emerald. In Pokémon Emerald, the Battle Factory allows the player to loan Pokémon to battle, instead of using their own Pokémon. Just like in the Battle Tower formats of the previous game, one run of the Battle Factory in the original game lasts for eight consecutive battles, with three Pokémon per trainer faced. However, in this implementation of the Battle Factory, the player gets to battle forever!

# How to Play
<img src="https://i.ibb.co/mF1ThZt/Selection-Screen.png" alt="drawing" width="250" height="375"/>  <img src="https://i.ibb.co/822bbn9/Selected-Screen.png" alt="drawing" width="250" height="375"/>

Upon running the game, the player will see the Pokémon selection screen, depicted on the left, where they are prompted to select three Pokémon. Once selected, the button indicating the Pokémon would become red, as depicted on the image on the right. Once the player has selected three Pokémon, they can confirm their choice by clicking the Okay button, and are moved to the next screen.

<img src="https://i.ibb.co/prvHgW7/Fight-Page.png" alt="drawing" width="250" height="375"/>  <img src="https://i.ibb.co/4p3wwJB/Switch-Page.png" alt="drawing" width="250" height="375"/>

The game screen takes inspiration from the DS versions of the Pokémon games. For the top half of the screen, information is displayed to the player. This information includes the names, levels, health remaining, max health, and images for both the player's Pokémon and the opposing Pokémon. The number of Pokémon left for the player and the opposing trainer are also displayed via the number of Pokéballs. Right underneath that is the Battle Progress, which shows the player what has transpired the previous turn.

The bottom half of the screen consists of two sets of actions the player can take, separated by two tabs. The first tab, on the left, allows the player to perform actions against the opposing Pokémon. For each move the Pokémon possesses, the name, Power Points (PP) remaining, and the type of the move are displayed. Once a move runs out of PP, the move will not be available until the battle is over. The second tab, on the right, allows the player to switch out to another available Pokémon. As long as the Pokémon is not fainted, ie. does not have 0 health, the player is able to switch out freely.

<img src="https://i.ibb.co/FYvBQxv/After-Attack-Page.png" alt="drawing" width="250" height="375"/>  

Upon using an attack, the battle progress will update with the faster Pokémon's move on the first row, followed by the next Pokémon's move on the second row. Additional information may also appear, such as any type effectiveness or noneffectiveness, critical hits, or if the Pokémon faints.

<img src="https://i.ibb.co/s1w4Kr1/After-Beat-Trainer-Page.png" alt="drawing" width="250" height="375"/>  <img src="https://i.ibb.co/yBS7xBV/LosePage.png" alt="drawing" width="250" height="375"/>

Once the player defeats three Pokémon in a row, as depicted on the left, ie. has beaten a trainer, the player's Pokémon will be restored to full health, with their PP restored. The trainer-beaten count will increment by one, and the next trainer will be generated. On the other hand, if all three of the player's Pokémon has been fainted, the game will reset and prompt the player to pick three new Pokémon to start a new run.
