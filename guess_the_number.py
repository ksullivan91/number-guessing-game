import random

class Game:
    """
    A game of 'Guess the Number' where a player attempts to guess a randomly
    generated number between 1 and 10 within the fewest possible attempts.

    Attributes:
        hidden_number (int): The number the player is trying to guess.
        guesses (int): The count of guesses made by the player.
    """

    def __init__(self):
        """Initialize the game by selecting a random number between 1 and 10."""
        self.hidden_number = random.randint(1, 10)
        self.guesses = 0

    def play(self):
        """
        Starts a new game session, prompting the user to guess the hidden number.
        Provides feedback based on the user's input and terminates when the user
        guesses correctly or chooses to exit the game.
        """
        print("\nHmm... I'm thinking of a number between 1 and 10.")

        while True:
            user_input = input("\nEnter your guess: ")
            
            # Allow the user to exit the game voluntarily
            if user_input.lower() == 'exit':
                print("\nHope to see you soon!")
                break
            
            try:
                guess = int(user_input)
                
                # Validate the guess is within the expected range
                if guess < 1 or guess > 10:
                    print("Whoops! That guess isn't within the range of 1 to 10. Try again!")
                    continue

                self.guesses += 1
                
                # Provide feedback based on the guess
                if guess < self.hidden_number:
                    print("\nA bit too low. Keep guessing!")
                elif guess > self.hidden_number:
                    print("\nA little too high. Try a smaller number!")
                else:
                    print(f"\nWell done! You guessed it in {self.guesses} {'attempt' if self.guesses == 1 else 'attempts'}. The hidden number was {self.hidden_number}.")
                    break
                
            except ValueError:
                print("\nPlease input a number between 1 and 10.")

def display_title():
    """
    Displays the welcome message and game instructions to the player.
    """
    print("*********************")
    print("\nWelcome to the Guess the Number Game!\n")
    print("*********************")
    print("\nTry to find my number. It's between 1 and 10. Good luck!")

def main():
    """
    The main function that orchestrates the flow of the game. It displays the game title,
    initiates game sessions, and handles the user's choice to play again or exit.
    It also provides a summary of gameplay statistics at the end.
    """
    display_title()
    games_played = []

    while True:
        game = Game()
        game.play()
        
        # Record only games where at least one guess was made
        if game.guesses > 0:  
            games_played.append(game)

        play_again = input("\nWould you like to play another round? (y/n): ").lower()
        
        # Summarize the game statistics and exit
        if play_again == 'n':
            total_attempts = sum(g.guesses for g in games_played)
            average_attempts = total_attempts / len(games_played) if games_played else 0
            print("\nSummary of your games:")
            for i, g in enumerate(games_played, 1):
                print(f"Game {i}: It took {g.guesses} {'attempt' if g.guesses == 1 else 'attempts'} to find the hidden number {g.hidden_number}.")
            print(f"\nAverage guesses per game: {average_attempts:.2f}")
            print("\nThank you for playing. See you next time!")
            break
        elif play_again != 'y':
            print("Oops! Please enter 'y' to continue or 'n' to exit.")

    print("\nUntil next time!")

if __name__ == "__main__":
    main()
