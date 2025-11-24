# Pokémon Terminal Edition

## Overview
This Python project implements a terminal-based Pokémon battle game with basic mechanics. It involves classes for Pokémon and trainers, battle simulation, saving/loading game states, and a command-line user interface.

## Classes

### Pokemon
Represents a Pokémon with key stats and methods.

**Attributes:**
- n (str): Pokémon name.
- mh (int): Maximum health points.
- ch (int): Current health points.
- a (int): Attack stat.
- d (int): Defense stat.

**Methods:**
- __init__(self, name, maxhp, atk, defense): Initializes attributes.
- dead(self): Returns boolean indicating if Pokémon is fainted (HP ≤ 0).
- fullheal(self): Restores ch to mh.
- __repr__(self): Returns string showing Pokémon's current status and condition (Healthy, Hurt, Critical).

**Static Method:**
- wild(): Returns a randomly chosen wild Pokémon instance from predefined options.

### Trainer
Represents a Pokémon trainer with a chosen Pokémon.

**Attributes:**
- name (str): Trainer's name formatted with title case.
- p (Pokemon): The trainer’s current Pokémon instance.

**Methods:**
- __init__(self, name, skip=False): Initializes trainer name; if skip is False, prompts to choose a starter Pokémon.
- choose(self): Presents user with starter Pokémon choices and returns selected Pokémon instance.

## Functions

### dmg(att, defe)
Calculates damage dealt during battle with random variation.

**Parameters:**
- att (Pokemon): Attacking Pokémon.
- defe (Pokemon): Defending Pokémon.

**Returns:** Integer damage value, minimum of 1.

### battle(me, wild)
Simulates a turn-based battle between player's Pokémon (me) and a wild Pokémon (wild).

- Alternates attack turns using random chance (50/50).
- Prints battle rounds, attack damage, and Pokémon status.
- Ends when one Pokémon's HP reaches zero or below.
- Heals player's Pokémon fully if the player wins.

### save(trainer)
Saves the current trainer's state and Pokémon stats to a JSON file pokegame.json. Handles exceptions if file writing fails. Stores trainer name and Pokémon attributes (name, current HP, max HP, attack, defense).

### load()
Loads saved game state from pokegame.json if it exists. Returns a Trainer instance with restored Pokémon status. Handles exceptions if file reading or JSON parsing fails. Returns None if no save file exists or on failure.

### cls()
Clears the terminal screen for Windows (cls) or Unix-like systems (clear) to maintain a clean UI.

### main()
Main game loop handling:
- Trainer name input and Pokémon selection.
- Menu with options to initiate wild battles, view status, save progress, and quit.
- Handles invalid inputs and keyboard interrupts gracefully.
- Displays Pokémon and battle information in the console.

## Constants
- SAVE = "pokegame.json": Filename for storing game state.

## Dependencies
- os: To clear console and check file existence.
- json: For saving and loading game data.
- random: To add randomness in damage and wild Pokémon selection.
- time: To add delays for better user experience.

## Code Structure & Modularity
The code follows a modular approach by clearly separating concerns: Pokémon and Trainer classes encapsulate attributes and behavior related to game entities, while battle simulation and persistence are managed by dedicated functions. Keeping classes focused on their domain helps maintain the code and extend features like adding new Pokémon moves or trainers seamlessly.

## Input Validation & Error Handling
Robust input validation is used in the choose method to ensure only valid starter selections are accepted, improving user experience. Exception handling during save/load ensures the game can recover gracefully without crashing, making it resilient to file I/O errors.

## Randomness and Game Mechanics
The dmg function incorporates controlled randomness in damage calculations to simulate battle unpredictability while guaranteeing a minimum damage value. Turn order in the battle function is randomized each round, adding variability to encounters.

## User Experience Enhancements
Screen clearing (cls) maintains a clean console interface, avoiding clutter after each action. Delays (time.sleep) provide a paced, readable interaction flow during battles and menus.

## Persistence and Save System
The game state is persisted using JSON serialization of trainer and Pokémon stats in pokegame.json, allowing users to save and resume progress easily. Saving compactly stores only essential details, ensuring quick read/write and file size efficiency.

## Design Considerations for Extensibility
Static method Pokemon.wild centralizes wild Pokémon generation, making it straightforward to add or update wild Pokémon pool. The Trainer constructor supports a skip parameter to facilitate loading previously saved games without forcing starter selection.

## Documentation & Maintainability
Docstrings would further improve comprehension by explicitly describing method inputs, outputs, and side effects. Adding type hints can help catch errors early and improve editor tooling support.

## Potential Enhancements
- Integration of additional Pokémon stats like speed, special attack, or status effects for richer battles.
- A move/attack system allowing multiple moves per Pokémon and strategic choice during battles.
- Implementing a graphical or text-based map system to explore and encounter wild Pokémon rather than instant battles.aa
- 
