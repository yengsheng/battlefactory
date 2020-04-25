# Pokémon: Battle Factory

The game takes inspiration from the Battle Factory, which is an installation of the Battle Frontier in the Gameboy Advanced game, Pokémon Emerald. In Pokémon Emerald, the Battle Factory allows the player to loan Pokémon to battle, instead of using their own Pokémon. Just like in the Battle Tower formats of the previous game, one run of the Battle Factory in the original game lasts for eight consecutive battles, with three Pokémon per trainer faced. However, in this implementation of the Battle Factory, the player gets to battle forever!

## How to Play

<img src="https://i.ibb.co/mNz1QLV/Selection-Screen.png" alt="drawing" width="250" height="375"/>  <img src="https://i.ibb.co/LnFsSKN/Selected-Screen.png" alt="drawing" width="250" height="375"/>

Upon running the game, the player will see the Pokémon selection screen, depicted on the left, where they are prompted to select three Pokémon. Once selected, the button indicating the Pokémon would become red, as depicted on the image on the right. Once the player has selected three Pokémon, they can confirm their choice by clicking the Okay button, and are moved to the next screen.

<img src="https://i.ibb.co/prvHgW7/Fight-Page.png" alt="drawing" width="250" height="375"/>  <img src="https://i.ibb.co/4p3wwJB/Switch-Page.png" alt="drawing" width="250" height="375"/>

The game screen takes inspiration from the DS versions of the Pokémon games. For the top half of the screen, information is displayed to the player. This information includes the names, levels, health remaining, max health, and images for both the player's Pokémon and the opposing Pokémon. The number of Pokémon left for the player and the opposing trainer are also displayed via the number of Pokéballs. Right underneath that is the Battle Progress, which shows the player what has transpired the previous turn.

The bottom half of the screen consists of two sets of actions the player can take, separated by two tabs. The first tab, on the left, allows the player to perform actions against the opposing Pokémon. For each move the Pokémon possesses, the name, Power Points (PP) remaining, and the type of the move are displayed. Once a move runs out of PP, the move will not be available until the battle is over. The second tab, on the right, allows the player to switch out to another available Pokémon. As long as the Pokémon is not fainted, ie. does not have 0 health, the player is able to switch out freely.

<img src="https://i.ibb.co/FYvBQxv/After-Attack-Page.png" alt="drawing" width="250" height="375"/>  

Upon using an attack, the battle progress will update with the faster Pokémon's move on the first row, followed by the next Pokémon's move on the second row. Additional information may also appear, such as any type effectiveness or noneffectiveness, critical hits, or if the Pokémon faints.

<img src="https://i.ibb.co/s1w4Kr1/After-Beat-Trainer-Page.png" alt="drawing" width="250" height="375"/>  <img src="https://i.ibb.co/yBS7xBV/LosePage.png" alt="drawing" width="250" height="375"/>

Once the player defeats three Pokémon in a row, as depicted on the left, ie. has beaten a trainer, the player's Pokémon will be restored to full health, with their PP restored. The trainer-beaten count will increment by one, and the next trainer will be generated. On the other hand, if all three of the player's Pokémon has been fainted, the game will reset and prompt the player to pick three new Pokémon to start a new run.

# Code

**THREE** modules were used for the creation of this game. This game will use a GUI built using **KIVY** to display information to the player, and allow the player to execute commands using buttons laid across the screen. To add randomness to some of the numbers in this game, the **random** module is also imported for this purpose. Finally, there are nested dictionaries and lists which we need to create copies of, for this purpose, the **deepcopy** function from the copy library is imported.

### Initialization
There are a few initialization dictionaries that have to be made as soon as the game is fired up. First of all, we set the window size to 500x700 pixels, and makes the window unresizeable. Also, all the required modules are imported.

The moves dictionary contains keys that map to another dictionary. The key points to a string indicating the name of the move, while the dictionary this points to includes the information about the move that we would need. This includes the current PP, maximum PP, power, and type of the move. 

The type_eff dictionary indicates how each type is effective against other types. Each type will map to another dictionary which has two more dictionaries, indicating what type it is super effective against, and what type it is not effective against.

The pokemon_info dictionary consists of information required to create each Pokémon. This includes their moveset, their type, name, images of their front and back sprites, EV and base stat values. The EV and base stat values are needed to calculate the actual stat of each Pokémon.

# Classes Used
There are a total of **SIX** classes created for this game. Five of them subclasses from the kivy classes, while the last one is a class that stores information for each Pokémon.

# SimplePopup class
SimplePopup subclasses from the Popup class in kivy. This class simply functions as a Popup with a button that has text, 'Okay', and text which is displayed to the user based on what is passed into the instance called. This class was created to prevent repeating of the five-line code that the Popup requires whenever a Popup is required.

# Pokemon class
This class contains information regarding the Pokémon instance created and the functions required for it to work. There will be four instances of this class active at any time. Three of the player's Pokémon, and one for the active opposing Pokémon. For each instance of this class, there will be the Pokémon's max health (maxhp), attack (attk), defense (defs), speed (spd), current hp (chp), front image sprite path (imgf), back image sprite path (imgb), type (typ), name (name), and moveset (this_moveset). 

There are also two important functions under this class. First, the damage_calc function, which calculates the amount of damage that should be dealt to the opponent based on the Pokémon using the move, the Pokémon receiving the move, and the move itself. This function will then return the damage dealt, as well as the additional text, such as if the move was super effective, not effective, whether it dealt a critical hit, and if the move fainted the Pokémon receiving the move. 

The next function is the use_move function. This takes in the user, the opposing Pokémon, the move used, and the GameScreen instance, which we need to change the label that displays the battle progress. This function is run when the player presses one of the buttons that commands the Pokémon to use a move in the GameScreen instance. First, the function checks whether there is sufficient PP for the move the player selected, and if it has 0 PP, it will prompt the user to select another move, via a SimplePopup. It then does a speed check and allows the Pokémon with higher speed to move first. If there is a tie, then the opposing Pokémon will move first. It will then randomize a move for the opposing Pokémon to use, and will perform damage calculations and inflict damage based on the calculated damage, as well as updating a label in the GameScreen instance to reflect the moves used and the additional text returned from the damage_calc function.

# SelectableGrid class

The SelectableGrid class subclasses from FocusBehavior, CompoundSelectionBehavior, and GridLayout. It modifies some of the functions these classes to create a customized Pokémon selection page for the player. There are functions that change the color of the button is they are selected or if they are not, and disallows the user from selecting more than three Pokémon. A function that plays a sound when is also added.

# SelectionScreen class

The SelectionScreen class is the screen that the player will first see when they load up the game. It consists of a GridLayout which consists of an instance of the SelectableGrid and a Button. The SelectableGrid displays a Button for each Pokémon the player can select, and the Button allows the player to confirm their selection of Pokémon. Upon clicking this confirmation button, it will check whether three buttons are selected, and will move on to the next screen if it is.

# GameScreen class

The GameScreen is where the player will play the game, proper. Instead of an \_\_init__, function, an on_enter function is used instead since it will take in a list based on the selected Pokémon from the SelectionScreen instance. This Screen consists of a BoxLayout oriented vertically, and this BoxLayout consists of three widgets. 

### Information Screen
The first will be the top half of the screen which displays information, including the healths, levels, names, and sprites for both Pokémon. In addition, the Pokémon remaining for each trainer is also indicated by the number of Pokéballs that remain, located below their Pokémon's healths. 

### Battle Progress
Between the top and bottom screen, there is a label which displays the battle progress, ie. the moves used, their effectiveness, and if any Pokémon fainted. This label is constantly modified by the use_move function that resides in the Pokémon class.

### Command Screen
The bottom half of the screen consists of a TabbedPanel which allows the player to execute a move, or to switch out to another Pokémon. The move execution buttons are binded to a function, use_attack, which first, checks whether is Pokémon is alive, and then calls the use_move function from the Pokemon class. If the opposing Pokémon has their health reduced to zero, a new Pokémon is generated for the opposing trainer, and the number of Pokémon beaten is incremented by 1. If the player's Pokémon has their health reduced to zero, then the number of Pokémon beaten for the trainer is incremented by 1. Then, it checks whether 3 Pokémon have been beaten by the player, and restores the health and PP of all the player's Pokémon to full, and increments the number of trainers defeated by 1, while resetting the number of Pokémon beaten by the trainer and the trainer's fainted Pokémon to zero. A SimplePopup will then be displayed to show how many trainers the player has defeated. 

The second tab allows the player to switch out to another Pokémon. First, it checks whether the Pokémon to switch out to has any health, and then switches the information from the active Pokémon to the waiting Pokémon, and vice versa. 

Everytime the player executes an action, the update function is also called. First, it checks whether the player has three fainted Pokémon. If yes, then it will show a SimplePopup that tells the player that they have lost this run, and brings them back to the SelectionScreen. This is also when the on_leave function is called for the GameScreen, which removes all the widgets in the GameScreen, leaving a blank slate for the next on_enter function to create all and display all the widgets again. If the player has not lost, it will update the opponent's information, the active Pokémon's information, and the buttons will be updated based on the active Pokémon. 

# Game class

The Game class subclasses from App, and consists of the build function which creates the ScreenManager instance and adds the SelectionScreen and GameScreen instances into the ScreenManager instance, which is returned when the function is run. 

### Acknowledgements
Pokémon sprites - https://veekun.com/dex/downloads

Pokémon BGM - https://www.youtube.com/watch?v=TNZ7gllxeZs

Pokémon Button SFX - https://www.youtube.com/watch?v=88qRmxhqoBA

Spongebob sprites - https://www.spriters-resource.com/pc_computer/monopolyspongebobsquarepantsedition/sheet/124323/

Logo made with - https://textcraft.net/style/Textcraft/pokemon
