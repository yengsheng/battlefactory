from kivy.config import Config
#initializing and fixing window size
Config.set('graphics', 'width', '500')
Config.set('graphics', 'height', '700')
Config.set('graphics', 'resizable', False)
import random
from copy import deepcopy as dc
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.tabbedpanel import TabbedPanel, TabbedPanelItem
from kivy.app import App
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.behaviors.compoundselection import CompoundSelectionBehavior
from kivy.core.audio import SoundLoader

# Initializing all the possible moves in the game
moves = {'Hydro Pump': {'cPP': 5, 'PP': 5, 'Power': 110, 'Type': 'Water'},
         'Ice Beam': {'cPP': 10,'PP': 10, 'Power': 90, 'Type': 'Ice'},
         'Dragon Pulse': {'cPP': 10,'PP': 10, 'Power': 85, 'Type': 'Dragon'},
         'Hyper Beam': {'cPP': 5,'PP': 5, 'Power': 150, 'Type': 'Normal'},
         'Dark Pulse': {'cPP': 15,'PP': 15, 'Power': 80, 'Type': 'Dark'},
         'Focus Blast': {'cPP': 5, 'PP': 5, 'Power': 150, 'Type': 'Fighting'},
         'Thunderbolt': {'cPP': 15, 'PP': 15, 'Power': 90, 'Type': 'Electric'},
         'Thunder': {'cPP': 10, 'PP': 10, 'Power': 110, 'Type': 'Electric'},
         'Body Slam': {'cPP': 15, 'PP': 15, 'Power': 85, 'Type': 'Normal'},
         'Earthquake': {'cPP': 10, 'PP': 10, 'Power': 100, 'Type': 'Ground'},
         'Crunch': {'cPP': 15, 'PP': 15, 'Power': 80, 'Type': 'Dark'},
         'Dragon Claw': {'cPP': 15, 'PP': 15, 'Power': 80, 'Type': 'Dragon'},
         'Fire Punch': {'cPP': 15, 'PP': 15, 'Power': 75, 'Type': 'Fire'},
         'Psychic': {'cPP': 10, 'PP': 10, 'Power': 90, 'Type': 'Psychic'},
         'Moonblast': {'cPP': 15, 'PP': 15, 'Power': 95, 'Type': 'Fairy'},
         'Shadow Ball': {'cPP': 15, 'PP': 15, 'Power': 80, 'Type': 'Dark'},
         'Meteor Mash': {'cPP': 10, 'PP': 10, 'Power': 90, 'Type': 'Steel'},
         'Ice Punch': {'cPP': 15, 'PP': 15, 'Power': 75, 'Type': 'Ice'},
         'Thunder Punch': {'cPP': 15, 'PP': 15, 'Power': 75, 'Type': 'Electric'},
         'Psycho Boost': {'cPP': 5, 'PP': 5, 'Power': 140, 'Type': 'Psychic'},
         'Flash Cannon': {'cPP': 10, 'PP': 10, 'Power': 80, 'Type': 'Steel'},
         'Energy Ball': {'cPP': 10, 'PP': 10, 'Power': 90, 'Type': 'Grass'},
         'Draco Meteor': {'cPP': 5, 'PP': 5, 'Power': 130, 'Type': 'Dragon'},
         'Fire Blast': {'cPP': 5, 'PP': 5, 'Power': 110, 'Type': 'Fire'},
         'Krabby Patty': {'cPP': 10, 'PP': 10, 'Power': 100, 'Type': 'Normal'},
         'Gary': {'cPP': 40, 'PP': 40, 'Power': 250, 'Type': 'Normal'}
        }

# Initializing type effectiveness required
type_eff = {'Water': {'eff': ['Fire', 'Rock'], 'neff': ['Water', 'Grass', 'Dragon']},
         'Ice': {'eff': ['Ground', 'Grass', 'Dragon'], 'neff': ['Steel', 'Fire', 'Water', 'Ice']},
         'Dragon': {'eff': ['Dragon'], 'neff': ['Steel']},
         'Normal': {'eff': [], 'neff': ['Rock', 'Steel']},
         'Dark': {'eff': ['Ghost', 'Psychic'], 'neff': ['Fighting', 'Dark', 'Fairy']},
         'Fighting': {'eff': ['Normal', 'Rock', 'Steel', 'Ice', 'Dark'], 'neff': ['Flying', 'Poison', 'Bug', 'Psychic', 'Fairy']},
         'Electric': {'eff': ['Flying', 'Water'], 'neff': ['Electric', 'Grass', 'Dragon']},
         'Ground': {'eff': ['Fire', 'Rock', 'Poison', 'Steel', 'Electric'], 'neff': ['Bug', 'Grass']},
         'Fire': {'eff': ['Grass', 'Bug', 'Steel', 'Ice'], 'neff': ['Water', 'Rock', 'Fire', 'Dragon']},
         'Psychic': {'eff': ['Fighting', 'Poison'], 'neff': ['Steel', 'Psychic']},
         'Fairy': {'eff': ['Fighting', 'Dragon', 'Dark'], 'neff': ['Poison', 'Steel', 'Fire']},
         'Steel': {'eff': ['Ice', 'Fairy', 'Rock'], 'neff': ['Water', 'Steel', 'Fire', 'Electric']},
         'Grass': {'eff': ['Water', 'Rock', 'Ground'], 'neff': ['Flying', 'Poison', 'Bug', 'Steel', 'Fire', 'Grass', 'Dragon']}
        }

# Initializing all Pokemon in the game
pokemon_info = {'Milotic': {'moves': ['Hydro Pump', 'Ice Beam', 'Dragon Pulse', 'Hyper Beam'], 'type': ['Water'], 'name': 'Milotic', 'imgf': 'images/350.png', 'imgb': 'images/350b.png', 'ev': [252, 0, 252, 6], 'base': [95, 100, 125, 81]},
                 'Ampharos': {'moves': ['Dragon Pulse', 'Focus Blast', 'Thunderbolt', 'Thunder'], 'type': ['Electric'], 'name': 'Ampharos', 'imgf': 'images/181.png', 'imgb': 'images/181b.png', 'ev': [6, 252, 0, 252], 'base': [90, 115, 90, 55]},
                 'Suicune': {'moves': ['Hydro Pump', 'Ice Beam', 'Body Slam', 'Hyper Beam'], 'type': ['Water'], 'name': 'Suicune', 'imgf': 'images/245.png', 'imgb': 'images/245b.png', 'ev': [6, 252, 0, 252], 'base': [100, 90, 115, 85]},
                 'Tyranitar': {'moves': ['Earthquake', 'Crunch', 'Dragon Claw', 'Fire Punch'], 'type': ['Rock', 'Dark'], 'name': 'Tyranitar', 'imgf': 'images/248.png', 'imgb': 'images/248b.png', 'ev': [252, 252, 6, 0], 'base': [100, 134, 110, 64]},
                 'Gardevoir': {'moves': ['Psychic', 'Moonblast', 'Shadow Ball', 'Focus Blast'], 'type': ['Psychic', 'Fairy'], 'name': 'Gardevoir', 'imgf': 'images/282.png', 'imgb': 'images/282b.png', 'ev': [0, 252, 6, 252], 'base': [68, 125, 115, 80]},
                 'Metagross': {'moves': ['Meteor Mash', 'Ice Punch', 'Thunder Punch', 'Earthquake'], 'type': ['Steel', 'Psychic'], 'name': 'Metagross', 'imgf': 'images/376.png', 'imgb': 'images/376b.png', 'ev': [252, 6, 252, 0], 'base': [80, 135, 130, 70]},
                 'Deoxys': {'moves': ['Psycho Boost', 'Ice Beam', 'Flash Cannon', 'Energy Ball'], 'type': ['Psychic'], 'name': 'Deoxys', 'imgf': 'images/386.png', 'imgb': 'images/386b.png', 'ev': [6, 252, 0, 252], 'base': [50, 150, 50, 150]},
                 'Hydreigon': {'moves': ['Draco Meteor', 'Dark Pulse', 'Flash Cannon', 'Fire Blast'], 'type': ['Dragon', 'Dark'], 'name': 'Hydreigon', 'imgf': 'images/635.png', 'imgb': 'images/635b.png', 'ev': [6, 252, 0, 252], 'base': [92, 125, 90, 98]},
                 'Spongebob': {'moves': ['Hyper Beam', 'Draco Meteor', 'Krabby Patty', 'Gary'], 'type': ['Water'], 'name': 'Spongebob', 'imgf': 'images/sbsp.png', 'imgb': 'images/sbspb.png', 'ev': [6, 252, 0, 252], 'base': [90, 120, 70, 85]}
                }

# Subclass of the Popup Class in Kivy. Customized to show a message and an 'Okay' button to dismiss it, since there won't be any other ways the Popup Class will be used. Also, play a sound when a button is pressed. How neat.
class SimplePopup(Popup):
    def open(self, msg, btn_text='Okay'):
        self.btn = SoundLoader.load('assets/button.wav')
        self.dismiss_btn = Button(text=btn_text)
        self.popup = Popup(title=msg, content = self.dismiss_btn, size_hint = (1, 0.2))
        self.dismiss_btn.bind(on_press = self.popup.dismiss)
        self.popup.open()

# Creating the Pokemon Class     
class Pokemon:
    def __init__(self, name):
        global pokemon_info
        # Finding the dictionary corresponding to the Pokemon instance created, and giving it it's list of moves.
        this_pokemon = pokemon_info[name]
        moveset = this_pokemon['moves']
        # Setting the Pokemon's stats as per given evs and base state.
        self.maxhp = int(((2 * this_pokemon['base'][0] + 31 + (this_pokemon['ev'][0]/4)) * 0.5) + 60)
        self.attk = int(((2 * this_pokemon['base'][1] + 31 + (this_pokemon['ev'][1]/4)) * 0.5) + 5)
        self.defs = int(((2 * this_pokemon['base'][2] + 31 + (this_pokemon['ev'][2]/4)) * 0.5) + 5)
        self.spd = int(((2 * this_pokemon['base'][3] + 31 + (this_pokemon['ev'][3]/4)) * 0.5) + 5)
        # Make the current hp equal to the max hp.
        self.chp = self.maxhp
        # Extracting the required information we will need to display/use later on.
        self.imgf = this_pokemon['imgf']
        self.imgb = this_pokemon['imgb']
        self.typ = this_pokemon['type']
        self.name = this_pokemon['name']
        self.this_moveset = {}
        global moves
        # Creating a dictionary of moves for the Pokemon in the format of the global variable, moves. 
        for move in moveset:
            self.this_moveset[move] = dc(moves[move])
    # Most of the game is centered around actions by the player's Pokemon. This function is called from the GameScreen.
    
    def damage_calc(user, opp, move):
        global type_eff
        global moves
        # Look for the move type.
        move_type = moves[move]['Type']
        # Initialize return variables.
        txt = ''
        mod = 1
        # Iterate through the type of the targeted Pokemon.
        for i in opp.typ:
            # Multiplier increase if effective
            if i in type_eff[move_type]['eff']:
                mod *= 2
            # Multiplier decrease if not effective
            elif i in type_eff[move_type]['neff']: 
                mod *= 0.5
        # Check the current modifier and add text accordingly.
        if mod == 2 or mod == 4:
            txt += ' It was super effective!'
        elif mod == 0.5 or mod == 0.25:
            txt += ' It was not effective...'
        # STAB (Same Type Attack Bonus) calculations, ie. if user uses a move that is it's own type, then increase modifier.
        for i in user.typ:
            if user.typ == move_type:
                mod *= 1.5
        # Roll for critical, and increase multiplier if critical hit.
        if random.randint(1, 10) == 1:
            mod *= 2
            txt += ' It was a critical hit!'
        # Implementing randomness into damage dealt.
        mod = mod * random.uniform(0.85, 1)
        return mod, txt
    
    def use_move(self, other, move, gs):
        # self --> The Pokemon currently out in battle.
        # other --> The opposing Pokemon
        # move --> The move to be used
        # gs --> The GameScreen class
        # Check if the move has enough PP. If not, show a popup saying that it does not have enough PP.
        if self.this_moveset[move]['cPP'] >= 1:
            # Randomize a move that the opposing Pokemon will use. 
            move_to_use = random.choice(list(other.this_moveset.keys()))
            opponent_move = other.this_moveset[move_to_use]
            your_text = 'Your ' + self.name + ' used ' + move + '.'
            opponent_text = 'Foe ' + other.name + ' used ' + move_to_use + '.'
            # Speed check, the Pokemon with the higher speed will attack first!
            if self.spd > other.spd:
                # Calculate damage, inflict upon opposing Pokemon, and reduce the current PP by 1.
                mod, extra_text1 = self.damage_calc(other, move)
                dmg = int(((22 * self.this_moveset[move]['Power'] * (self.attk/other.defs))/50 + 2) * mod)
                other.chp -= dmg
                print(dmg)
                self.this_moveset[move]['cPP'] -= 1
                # If the damage dealt will cause the opposing Pokemon to have negative health, set it to 0 instead. Also, change the textbox so that it reflects the used move, and the fainted opponent.
                if other.chp <= 0:
                    other.chp = 0
                    gs.textbox.text = your_text + extra_text1 + '\nFoe ' + other.name + ' fainted!'
                # If the attack does not faint the opponent, the opponent will use their move, deal its damage. The PP of the opposing enemy is not kept track to give the AI an advantage.
                else:
                    mod, extra_text2 = other.damage_calc(self, move_to_use)
                    dmg = int(((22 * opponent_move['Power'] * (other.attk/self.defs))/50 + 2) * mod)
                    self.chp -= dmg
                    print(dmg)
                    # If the damage dealt will cause your Pokemon to have negative health, set it to 0 instead. The textbox will reflect the moves used by both Pokemon, and the fainted Pokemon.
                    if self.chp <= 0:
                        self.chp = 0
                        gs.yours_beaten += 1
                        gs.textbox.text = your_text + extra_text1 + '\n' + opponent_text + extra_text2 + '\nYour ' + self.name + ' fainted!'
                    # If your Pokemon does not faint, the textbox will reflect the moves used by both Pokemon.
                    else:
                        gs.textbox.text = your_text + extra_text1 + '\n' + opponent_text + extra_text2
            # If opposing Pokemon is faster, the order of attacks are swapped. 
            else:
                mod, extra_text1 = other.damage_calc(self, move_to_use)
                dmg = int(((22 * opponent_move['Power'] * (other.attk/self.defs))/50 + 2) * mod)
                self.chp -= dmg
                print(dmg)
                if self.chp <= 0:
                    self.chp = 0
                    gs.yours_beaten += 1
                    gs.textbox.text = opponent_text + extra_text1 + '\nYour ' + self.name + ' fainted!'
                else:
                    mod, extra_text2 = self.damage_calc(other, move)
                    dmg = int(((22 * self.this_moveset[move]['Power'] * (self.attk/other.defs))/50 + 2) * mod)
                    other.chp -= dmg
                    print(dmg)
                    gs.textbox.text = opponent_text + extra_text1 + '\n' + your_text + extra_text2
                    if other.chp <= 0:
                        other.chp = 0
                        gs.textbox.text = opponent_text + extra_text1 + '\n' + your_text + extra_text2 + '\nFoe ' + other.name + ' fainted!'
                    self.this_moveset[move]['cPP'] -= 1
        # Popup to show that the selected move has ran out of PP.
        else:
            SimplePopup.open(self, 'This move has ran out of PP!')
            
# The SelectableGrid subclass is used for the player to select their choice of Pokemon for their run
class SelectableGrid(CompoundSelectionBehavior, GridLayout):
    # Initialize the selected list of Pokemon, in case the user decides to NOT choose any Pokemon to prevent crashing the game.
    selected = []
    
    # Override the add_widget so we can edit the button_touch_down function. 
    def add_widget(self, widget):
        widget.bind(on_touch_down=self.button_touch_down)
        return super(SelectableGrid, self).add_widget(widget)
    # Check if the buttons are touched
    def button_touch_down(self, button, touch):
        btn = SoundLoader.load('assets/button.wav')
        btn.play()
        if button.collide_point(*touch.pos):
            self.select_with_touch(button, touch)
    # When a button is selected, change its background color to reflect so., and reflect that the button has been selected.       
    def select_node(self, node):
        node.background_color = (1, 0, 0, 1)
        return super(SelectableGrid, self).select_node(node)
    # When a button is deselected, change its background color to reflect so and reflect that the button has been deselected.  
    def deselect_node(self, node):
        node.background_color = (1, 1, 1, 1)
        super(SelectableGrid, self).deselect_node(node)
    # If more than three are selected, do not allow the selection of the new Pokemon. Then, change SelectableGrid.selected to the objects selected.    
    def on_selected_nodes(self, grid, nodes):
        if len(nodes) > 3:
            nodes[-1].background_color = (1, 1, 1, 1)
            super(SelectableGrid,self).deselect_node(nodes[-1])
        SelectableGrid.selected = nodes    

# The screen which the user will see when they first enter the game, the selection screen for their Pokemon.
class SelectionScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Take the global variable pokemon_info.
        global pokemon_info
        # Create the grid for both the selection grid and the button.
        self.selection = GridLayout(cols=1, rows=3)
        # Create and add the game logo.
        self.logo = Image(source = 'images/Pokemon.png', size_hint=(0.7, 0.7))
        self.selection.add_widget(self.logo)
        # Create the selection grid
        self.grid = SelectableGrid(cols=3, touch_multiselect=True,
                              multiselect=True)
        # Create a button for each Pokemon in the pool of available Pokemon
        for i in pokemon_info:
            self.grid.add_widget(Button(text=i))
        # Add the selection grid into the main layout
        self.selection.add_widget(self.grid)
        # Create and add the button into the main layout.
        self.okay_btn = Button(text = 'Okay', on_press=self.done, size_hint_y = 0.3)
        self.selection.add_widget(self.okay_btn)
        # Add the main layout into the SelectionScreen class.
        self.add_widget(self.selection)
        try:
            # Loading epic Pokemon game music, with loop.
            self.music = SoundLoader.load('assets/music.wav')
            self.music.loop = True
            self.music.play()
        except:
            pass
        
    def done(self, value):
        # Check if less than three Pokemon have been selection. If so, do not allow the player to continue, and show a prompt asking them to pick three Pokemon.
        if len(self.grid.selected) < 3:
            SimplePopup.open(self, 'You need THREE Pokemon!')
        else:
            # Create a list of name of the selected Pokemon to be used in the GameScreen.
            x = []
            for i in SelectableGrid.selected:
                x.append(i.text)
            SelectableGrid.chosen = x
            # Transition over to the GameScreen.
            self.manager.transition = NoTransition()
            self.manager.current = 'game'            
            
class GameScreen(Screen):
    # on_enter is used instead of __init__ as we require SelectableGrid.chosen to be not empty and contain the names of the three Pokemon selected by the player. 
    def on_enter(self):
        # Start by bringing in the global dictionary pokemon_info
        global pokemon_info
        # Initiate variables for the Pokemon chosen by the player, number of Pokemon beaten, number of trainers beaten, and possible Pokemon that can be generated.
        player_pokemon = SelectableGrid.chosen
        self.btn = SoundLoader.load('assets/button.wav')
        self.pkm_beaten = 0
        self.yours_beaten = 0
        self.trainers_beaten = 0
        self.pbl_images = ['assets/threeballs.png', 'assets/twoballs.png', 'assets/oneball.png']
        self.possible_pokemon = list(pokemon_info.keys())
        # Create three variables, each one an instance of the Pokemon class, as well as randomize an opposing Pokemon from the pool of Pokemon as an instance of the Pokemon class.
        self.pkm1, self.pkm2, self.pkm3 = Pokemon(player_pokemon[0]), Pokemon(player_pokemon[1]), Pokemon(player_pokemon[2])
        self.opkm = Pokemon(random.choice(self.possible_pokemon))
        # Simulating a DS, our layout will start with the BoxLayout in vertical form.
        self.layout = BoxLayout(orientation = 'vertical')
        # self.top_screen displays the information for the player, including the current and max HP of both Pokemon, their levels, names, sprites.
        self.top_screen = GridLayout(cols = 2, rows = 2, size_hint=(1, 0.7))
        # Sets up and displays the opposing Pokemon's name, health, and level.
        self.opponent_info = GridLayout(cols = 1, rows = 3, size_hint=(1, 0.5))
        self.opponent_name_level = Label(text = self.opkm.name + '   Lv50', font_size = 18, valign = 'middle', halign = 'left') 
        self.opponent_info.add_widget(self.opponent_name_level)
        self.opponent_hp = Label(text = str(self.opkm.chp) + '/' + str(self.opkm.maxhp), font_size = 16, valign = 'top')
        self.opponent_info.add_widget(self.opponent_hp)
        self.opponent_pkm_left = Image(source = self.pbl_images[self.pkm_beaten])
        self.opponent_info.add_widget(self.opponent_pkm_left)
        self.top_screen.add_widget(self.opponent_info)
        # Displays the image for both Pokemon.
        self.oimg = Image(source=self.opkm.imgf)
        self.top_screen.add_widget(self.oimg)
        self.mimg = Image(source=self.pkm1.imgb)
        self.top_screen.add_widget(self.mimg)
        # Sets up and displays my Pokemon's name, health, and level.
        self.my_info = GridLayout(cols = 1, rows = 3, size_hint=(1, 0.5))
        self.my_name_level = Label(text = self.pkm1.name+'   Lv50', font_size = 18, valign = 'middle', halign = 'left')
        self.my_info.add_widget(self.my_name_level)
        self.my_hp = Label(text = str(self.pkm1.chp) + '/' + str(self.pkm1.maxhp), font_size = 16, valign = 'top')
        self.my_info.add_widget(self.my_hp)
        self.my_pkm_left = Image(source = self.pbl_images[self.yours_beaten])
        self.my_info.add_widget(self.my_pkm_left)
        # Add the whole of the top screen into the main layout.
        self.top_screen.add_widget(self.my_info)        
        self.layout.add_widget(self.top_screen)
        # Create and add a label that shows the progress of the battle, which will be constantly updated as the user takes action.
        self.textbox = Label(text='Battle progress shows up here!', font_size=14, valign = 'top', halign = 'center', size_hint=(1, 0.3))
        self.layout.add_widget(self.textbox) 
        # The bottom screen will allow the user to put in their actions. In our case, we do not need the 'Bag' and 'Run' tab from the original Pokemon game, so a TabbedPanel spanning two tab items would suffice.
        self.btm_screen = TabbedPanel(do_default_tab = False, tab_width = 250)
        # Add in our tabs, either to fight or to switch out.
        self.fight_tab = TabbedPanelItem(text = 'Fight')
        self.switch_tab = TabbedPanelItem(text = 'Pokemon')
        # Creating the page for using a move, which is selected initially
        self.fight_page = GridLayout(cols = 2, col_default_width = 250, col_force_default = True, row_default_height = 150, row_force_default = True)
        # Initializing the moves for all three Pokemon.
        self.pkm1_moves = pokemon_info[self.pkm1.name]['moves']
        self.pkm2_moves = pokemon_info[self.pkm2.name]['moves']
        self.pkm3_moves = pokemon_info[self.pkm3.name]['moves']
        # Adding buttons for each move the Pokemon has.
        self.move1_btn = Button(text = self.pkm1_moves[0] + '\n' + 'PP: ' + str(self.pkm1.this_moveset[self.pkm1_moves[0]]['cPP']) + '/' + str(self.pkm1.this_moveset[self.pkm1_moves[0]]['PP']) + '\n' + 'Type: ' + str(self.pkm1.this_moveset[self.pkm1_moves[0]]['Type']), font_size = 16, halign = 'center', on_press = self.use_attack)
        self.move2_btn = Button(text = self.pkm1_moves[1] + '\n' + 'PP: ' + str(self.pkm1.this_moveset[self.pkm1_moves[1]]['cPP']) + '/' + str(self.pkm1.this_moveset[self.pkm1_moves[1]]['PP']) + '\n' + 'Type: ' + str(self.pkm1.this_moveset[self.pkm1_moves[1]]['Type']), font_size = 16, halign = 'center', on_press = self.use_attack)
        self.move3_btn = Button(text = self.pkm1_moves[2] + '\n' + 'PP: ' + str(self.pkm1.this_moveset[self.pkm1_moves[2]]['cPP']) + '/' + str(self.pkm1.this_moveset[self.pkm1_moves[2]]['PP']) + '\n' + 'Type: ' + str(self.pkm1.this_moveset[self.pkm1_moves[2]]['Type']), font_size = 16, halign = 'center', on_press = self.use_attack)
        self.move4_btn = Button(text = self.pkm1_moves[3] + '\n' + 'PP: ' + str(self.pkm1.this_moveset[self.pkm1_moves[3]]['cPP']) + '/' + str(self.pkm1.this_moveset[self.pkm1_moves[3]]['PP']) + '\n' + 'Type: ' + str(self.pkm1.this_moveset[self.pkm1_moves[3]]['Type']), font_size = 16, halign = 'center', on_press = self.use_attack)
        self.fight_page.add_widget(self.move1_btn)
        self.fight_page.add_widget(self.move2_btn)
        self.fight_page.add_widget(self.move3_btn)
        self.fight_page.add_widget(self.move4_btn)
        self.fight_tab.add_widget(self.fight_page)
        # Creating the page to switch out.
        self.switch_page = BoxLayout(orientation='horizontal')
        # Display the names of the other two Pokemon as well as their HP.
        self.pkm1_btn = Button(text = self.pkm2.name + '\n' + str(self.pkm2.chp) +'/' + str(self.pkm2.maxhp), font_size = 16, halign = 'center', on_press = self.switch1)
        self.pkm2_btn = Button(text = self.pkm3.name + '\n' + str(self.pkm3.chp) +'/' + str(self.pkm3.maxhp), font_size = 16, halign = 'center', on_press = self.switch2)
        self.switch_page.add_widget(self.pkm1_btn)
        self.switch_page.add_widget(self.pkm2_btn)
        self.switch_tab.add_widget(self.switch_page)
        self.btm_screen.add_widget(self.fight_tab)
        self.btm_screen.add_widget(self.switch_tab)
        # Add the bottom screen into the layout, and add the layout into the screen.
        self.layout.add_widget(self.btm_screen)
        self.add_widget(self.layout)
        
    # When a transition happens from this screen to the selection screen, remove all widgets so that on_enter does not create a second layer of widgets.
    def on_leave(self):
        self.clear_widgets()
    
    # The switch function for both Pokemon slots. Checks if the current HP of Pokemon to switch to is 0, if so, do not allow the switch.
    def switch1(self, instance):
        self.btn.play()
        if self.pkm2.chp == 0:
            SimplePopup.open(self, 'This Pokemon has fainted!')
        else:
            self.pkm1, self.pkm2 = self.pkm2, self.pkm1
            self.update()
            self.btm_screen.switch_to(self.fight_tab)
            
    def switch2(self, instance):
        self.btn.play()
        if self.pkm3.chp == 0:
            SimplePopup.open(self, 'This Pokemon has fainted!')
        else:
            self.pkm1, self.pkm3 = self.pkm3, self.pkm1
            self.update()
            self.btm_screen.switch_to(self.fight_tab)
    # Binded to each button with a move, this function is called whenever an attack is used.
    def use_attack(self, instance):
        # Check if the using Pokemon is fainted first, and prompt the user to switch out of it is.
        self.btn.play()
        if self.pkm1.chp == 0:
            SimplePopup.open(self, 'Your current Pokemon has fainted, please switch out!')
        else:
            # Take the text in the button and split it so we can take the first word, the name of the move.
            move = instance.text.split('\n')[0]
            # Call use_move from the Pokemon class to execute the move.
            self.pkm1.use_move(self.opkm, move, self)
            # If the opposing Pokemon faints, increase pkm_beaten by 1.
            if self.opkm.chp == 0:
                self.pkm_beaten += 1
                # If three consecutive defeats have happened, change pkm_beaten to 0, and add 1 to trainer beaten. Restore health and PP to all the player's Pokemon, and display a prompt that tells the player that their Pokemon are restored, as well as the number of trainers beaten.
                if self.pkm_beaten == 3:
                    self.yours_beaten = 0
                    self.pkm_beaten = 0
                    self.trainers_beaten += 1
                    self.pkm1.chp = self.pkm1.maxhp
                    self.pkm2.chp = self.pkm2.maxhp
                    self.pkm3.chp = self.pkm3.maxhp
                    for i in range(4):
                        self.pkm1.this_moveset[self.pkm1_moves[i]]['cPP'] = self.pkm1.this_moveset[self.pkm1_moves[i]]['PP']
                        self.pkm2.this_moveset[self.pkm2_moves[i]]['cPP'] = self.pkm2.this_moveset[self.pkm2_moves[i]]['PP']
                        self.pkm3.this_moveset[self.pkm3_moves[i]]['cPP'] = self.pkm3.this_moveset[self.pkm3_moves[i]]['PP']
                    SimplePopup.open(self, 'You\'ve beaten a trainer!\nYour Pokemon will now be fully healed.\n' + 'Trainers Beaten: ' + str(self.trainers_beaten))
                # Randomize a new Pokemon for the opponent, and also preventing it from being the last Pokemon to prevent duplicates.
                self.opkm = Pokemon(random.choice([x for x in self.possible_pokemon if x != self.opkm.name]))
            # Call the update function.
            self.update()
            
    # The update function updates the game state. After each move or switchout, it will change everything as necessary, be it the health of both Pokemon, the sprites displayed, the moves available for your Pokemon, and PP of the moves, etc.
    def update(self):
        # If all the player's Pokemon are fainted, that means the player loses, sadly. Allow the player to restart their run with new Pokemon by bringing them back to the selection screen. Note that the on_leave function is also called to clear all the widgets.
        if self.yours_beaten == 3:
            self.yours_beaten = 0
            SimplePopup.open(self, 'All your Pokemon have fainted!\nYou will be brought to the selection screen to restart your run.')
            self.manager.transition = NoTransition()
            self.manager.current = 'selection'
        self.opponent_name_level.text = self.opkm.name+'   Lv50'
        self.opponent_hp.text = str(self.opkm.chp) + '/' + str(self.opkm.maxhp)
        self.oimg.source = self.opkm.imgf
        self.mimg.source = self.pkm1.imgb
        self.my_name_level.text = self.pkm1.name+'   Lv50'
        self.my_hp.text = str(self.pkm1.chp) + '/' + str(self.pkm1.maxhp)
        self.pkm1_moves = pokemon_info[self.pkm1.name]['moves']
        self.move1_btn.text = self.pkm1_moves[0] + '\n' + 'PP: ' + str(self.pkm1.this_moveset[self.pkm1_moves[0]]['cPP']) + '/' + str(self.pkm1.this_moveset[self.pkm1_moves[0]]['PP']) + '\n' + 'Type: ' + str(self.pkm1.this_moveset[self.pkm1_moves[0]]['Type'])
        self.move2_btn.text = self.pkm1_moves[1] + '\n' + 'PP: ' + str(self.pkm1.this_moveset[self.pkm1_moves[1]]['cPP']) + '/' + str(self.pkm1.this_moveset[self.pkm1_moves[1]]['PP']) + '\n' + 'Type: ' + str(self.pkm1.this_moveset[self.pkm1_moves[1]]['Type'])
        self.move3_btn.text = self.pkm1_moves[2] + '\n' + 'PP: ' + str(self.pkm1.this_moveset[self.pkm1_moves[2]]['cPP']) + '/' + str(self.pkm1.this_moveset[self.pkm1_moves[2]]['PP']) + '\n' + 'Type: ' + str(self.pkm1.this_moveset[self.pkm1_moves[2]]['Type'])
        self.move4_btn.text = self.pkm1_moves[3] + '\n' + 'PP: ' + str(self.pkm1.this_moveset[self.pkm1_moves[3]]['cPP']) + '/' + str(self.pkm1.this_moveset[self.pkm1_moves[3]]['PP']) + '\n' + 'Type: ' + str(self.pkm1.this_moveset[self.pkm1_moves[3]]['Type'])
        self.pkm1_btn.text = self.pkm2.name + '\n' + str(self.pkm2.chp) +'/' + str(self.pkm2.maxhp)
        self.pkm2_btn.text = self.pkm3.name + '\n' + str(self.pkm3.chp) +'/' + str(self.pkm3.maxhp)
        self.pkm1_moves = pokemon_info[self.pkm1.name]['moves']
        self.pkm2_moves = pokemon_info[self.pkm2.name]['moves']
        self.pkm3_moves = pokemon_info[self.pkm3.name]['moves']
        self.opponent_pkm_left.source = self.pbl_images[self.pkm_beaten]
        self.my_pkm_left.source = self.pbl_images[self.yours_beaten]
        if self.pkm1.chp == 0:
            self.btm_screen.switch_to(self.switch_tab)
        
        

# Initializing the Game class, with both the Screens added into the ScreenManager.               
class Game(App):
    def build(self):
        sm = ScreenManager()
        ss = SelectionScreen(name='selection')
        gs = GameScreen(name='game')
        sm.add_widget(ss)
        sm.add_widget(gs)
        sm.current='selection'
        return sm
    
# Let the game begin!
Game().run()