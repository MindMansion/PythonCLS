from random import randrange
from time import sleep
from Helpers.logger import Logger


class Game:
    """
        Simple number guessing
        game in python
    """

    def __init__(self):
        Logger.Title("Welcome to Number Guessing Game")
        self.__number = randrange(0, 21)
        self.__currentGuess = None
        self.__name = str
        self.__maxTries = 10
        self.__currentTry = 0
        self.__point = 1000

        self.__initGame()

    def __initGame(self):
        while self.__name is not 'q':
            try:
                self.__name = input("\tEnter your name q to quit: ")
            except ValueError:
                Logger.PrintTab("Error reading name from console!")

            if len(self.__name.strip()) == 0:
                Logger.PrintTab("Name cannot be blank")
                continue
            break

        Logger.SubTitle("Objectives", align='right')
        Logger.PrintTab(f"""
        Welcome {self.__name}, my name is Magic 
        Roller, in this game I will be giving you
        a chance to guess the number i'm thinking.
        
        Rules: 
        --------------------------------------------
            -> You will have 10 tries each roll. 
            -> you guess wrong you will get a 10% 
               point deduction from your total point.
            -> When you guess it right you will get 
               your total point multiplied my 10% of it, 
               added to your current point.
        """, level=0)
        Logger.PrintTab("Good luck!")

        print("\tInitializing Game", end="")
        for _ in range(20):
            sleep(0.1)
            print(".", end="")
        print()

        Logger.Space()
        Logger.PrintTab("Game Initialized")
        Logger.Divider()
        self.__play()

    def __play(self):

        while self.__currentTry < self.__maxTries:
            try:
                self.__currentGuess = input("Enter your guess: ")
                self.__currentGuess = int(self.__currentGuess)
            except ValueError as e:
                Logger.PrintTab(e)
                Logger.PrintTab("Please enter a valid number without spaces:")
                continue

            self.__currentTry += 1
            if self.__currentGuess == self.__number:
                self.__point += (self.__point * 0.10)
                self.__gameOver()
                return
            else:
                self.__point -= (self.__point * 0.10)
                self.__update()
                continue
        self.__gameOver()

    def __update(self):
        if int(self.__currentGuess) < self.__number:
            Logger.PrintTab(f"Too low")
            Logger.PrintTab(f"Enter a guess between {self.__currentGuess} and {20}")
            Logger.PrintTab(f"{self.__maxTries - self.__currentTry} chance left")
        else:
            Logger.PrintTab(f"Too high")
            Logger.PrintTab(f"Enter a guess between {0} and {self.__currentGuess}")
            Logger.PrintTab(f"{self.__maxTries - self.__currentTry} chance left")

    def __gameOver(self):
        Logger.Space()
        if self.__currentTry < self.__maxTries:
            Logger.PrintTab(f"Hurray!! You Guessed it")
            Logger.PrintTab(f"The number is: {self.__currentGuess}")
            Logger.Space()

        Logger.PrintTab("Summary")
        Logger.PrintTab("=" * 20)
        Logger.PrintTab(f"Player: {self.__name}")
        Logger.PrintTab(f"Tries used: {self.__currentTry}")
        Logger.PrintTab(f"Point: {self.__point}")

        if self.__currentTry == self.__maxTries:
            Logger.Space()
            Logger.PrintTab(f"You failed to guess the correct number {self.__number}")
        Logger.SubTitle("Game Over!")


# Run Example
# ===========
"""
    =========[ Welcome to Number Guessing Game ]=========
        Enter your name q to quit: kelvin
    
                                           ( Objectives )
    *****************************************************
    
            Welcome kelvin, my name is Magic 
            Roller, in this game I will be giving you
            a chance to guess the number i'm thinking.
            
            Rules: 
            --------------------------------------------
                -> You will have 10 tries each roll. 
                -> you guess wrong you will get a 10% 
                   point deduction from your total point.
                -> When you guess it right you will get 
                   your total point multiplied my 10% of it, 
                   added to your current point.
            
        Good luck!
        Initializing Game....................
    
        - - - - - - - - - - - - - - - - - - - - - - - - - 
        Game Initialized
    
    -----------------------------------------------------
    Enter your guess: kelvin
        invalid literal for int() with base 10: 'kelvin'
        Please enter a valid number without spaces:
    Enter your guess: 10
        Too high
        Enter a guess between 0 and 10
        9 chance left
    Enter your guess: 5
        Too low
        Enter a guess between 5 and 20
        8 chance left
    Enter your guess: 3
        Too low
        Enter a guess between 3 and 20
        7 chance left
    Enter your guess: 4
        Too low
        Enter a guess between 4 and 20
        6 chance left
    Enter your guess: 7
    
        - - - - - - - - - - - - - - - - - - - - - - - - - 
        Hurray!! You Guessed it
        The number is: 7
    
        - - - - - - - - - - - - - - - - - - - - - - - - - 
        Summary
        ====================
        Player: kelvin
        Tries used: 5
        Point: 721.71
    
                        ( Game Over! )                    
    *****************************************************
    
    Process finished with exit code 0
"""
