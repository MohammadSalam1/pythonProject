import os

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

class player():
    def __init__(self):
        self.name = ""
        self.symbol = ""

    def choose_name(self):
        while True:
            name = input("Enter your name: ")
            if name.isalpha():
                self.name = name
                break
            print("Invalid name. Please use letters only.")

    def choose_symbol(self):
        while True:
            symbol = input(f"{self.name}, choose a symbol (X or O): ").upper()
            if symbol in ["X", "O"]:
                self.symbol = symbol
                break
            print("Invalid symbol. Please choose X or O.")

class menu():
    def startmenu(self):
        print("Welcome to Tic Tac Toe game")
        print("1. Start game")
        print("2. Quit")
        while True:
            choice = input("Enter your choice (1 or 2): ")
            if choice in ["1", "2"]:
                return choice
            print("Invalid choice. Please enter 1 or 2.")

    def endgame_menu(self):
        menu_text = """
        Game Over
        1. Restart game
        2. Quit game
        Enter your choice (1 or 2): """
        while True:
            choice = input(menu_text)
            if choice in ["1", "2"]:
                return choice
            print("Invalid choice. Please enter 1 or 2.")

class board():
    def __init__(self):
        self.board = [str(i) for i in range(1, 10)]

    def display_board(self):
        for i in range(0, 9, 3):
            print("|".join(self.board[i:i+3]))
            if i < 6:
                print("-" * 5)

    def update_board(self, choice, symbol):
        if self.is_valid_move(choice):
            self.board[choice - 1] = symbol
            return True
        return False

    def is_valid_move(self, choice):
        return self.board[choice - 1].isdigit()

    def reset_board(self):
        self.board = [str(i) for i in range(1, 10)]

class game():
    def __init__(self):
        self.players = [player(), player()]
        self.gameboard = board()
        self.gamemenu = menu()
        self.current_player_index = 0

    def start_game(self):
        choice = self.gamemenu.startmenu()
        if choice == "1":
            self.setup_players()
            self.play_game()
        else:
            self.quit_game()

    def setup_players(self):
        for number, player in enumerate(self.players, start=1):
            print(f"Player {number}, enter your details:")
            player.choose_name()
            player.choose_symbol()
            clear_screen()

    def play_game(self):
        while True:
            self.play_turn()
            if self.check_win():
                self.gameboard.display_board()
                print(f"Congratulations {self.players[self.current_player_index].name}, you win!")
                if self.handle_endgame():
                    break
            elif self.check_draw():
                self.gameboard.display_board()
                print("It's a draw!")
                if self.handle_endgame():
                    break

    def handle_endgame(self):
        choice = self.gamemenu.endgame_menu()
        if choice == "1":
            self.restart_game()
        elif choice == "2":
            self.quit_game()
            return True
        return False

    def restart_game(self):
        self.gameboard.reset_board()
        self.current_player_index = 0
        self.play_game()

    def check_win(self):
        win_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
            [0, 4, 8], [2, 4, 6]              # diagonals
        ]
        for combo in win_combinations:
            if (self.gameboard.board[combo[0]] == self.gameboard.board[combo[1]] ==
                self.gameboard.board[combo[2]]):
                return True
        return False

    def check_draw(self):
        return all(not cell.isdigit() for cell in self.gameboard.board)

    def play_turn(self):
        player = self.players[self.current_player_index]
        self.gameboard.display_board()
        print(f"{player.name}'s turn ({player.symbol})")
        while True:
            try:
                cell_choice = int(input("Choose a cell (1 - 9): "))
                if 1 <= cell_choice <= 9 and self.gameboard.update_board(cell_choice, player.symbol):
                    break
                else:
                    print("Invalid move, try again.")
            except ValueError:
                print("Please enter a number between 1 and 9.")
        self.switch_player()

    def switch_player(self):
        self.current_player_index = 1 - self.current_player_index

    def quit_game(self):
        print("Thank you for playing!")

# Create a new game instance and start it
newgame = game()
newgame.start_game()
