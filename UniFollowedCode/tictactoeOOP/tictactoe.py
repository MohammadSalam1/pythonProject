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
      
      if name.isalpha() == True:
        self.name = name
        break
      print("invalid name, please use letters only")


  def choose_symbol(self):
    while True:
      symbol = input(f"{self.name}choose a symbol X or O: ").lower()
      
      if symbol.isalpha() == True and len(symbol) == 1:
        self.symbol = symbol
        break
      print("invalid symbol, choose a single letter")

class menu():
  def startmenu(self):
    print("Welcom to tic tac toe game")
    print("1. Start game")
    print("2. Quit")

    choice = input("Enter your choice(1 or 2): ")
    return choice

  def endgame_menu(self):
    menu_text = """
    Game Over
    1. Restart game
    2. Quit game
    Enter your choice (1 or 2): """

    choice = input(menu_text)
    return choice

class board():
  def __init__(self):
    self.board = []
    for i in range(1, 10):
      self.board.append(str(i))        

  def display_board(self):
    for i in range(0, 9, 3):
      print("|".join(self.board[i:i+3]))
      if i < 6:
        print("-"*5)

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
    

  def setup_player(self):
    for number, player in enumerate(self.players, start= 1):
      print(f"player {number}, enter your details: ")
      player.choose_name()
      player.choose_symbol()
      clear_screen()
  
  def play_game(self):
    while True:
      self.play_turn():
      if self.check_win() or self.check_draw():
        self.menu.endgame_menu()
        if choice == "1":
          self.restart_game()
        else:
          self.quit_game()
          break


  def restart_game(self):
    self.gameboard.reset_board()

  def check_win(self):
    win_combinations = [
      [0, 1, 2], [3, 4, 5], [6, 7, 8], #rows
      [0, 3, 6], [1, 4, 7], [2, 5, 8], #columns
      [0, 4, 8], [2, 4, 6]
    ]
    for combo in win_combinations:
      if (self.gameboard.board[combo[0]] == self.gameboard.board[combo[1]] == self.gameboard.board[combo[2]]):
        return True
      return False
  
  def check_draw(self):
    return all (not cell.isdigit() for cell in self.gameboard.board)

  def play_turn(self):
    player = self.players[self.current_player_index]
    self.gameboard.display_board()
    print(f"{player.name}'s turn ({player.symbol})")

    while True:
      try:
        cell_choice = int(input("chose a cell (1 - 9): "))
        if 1 <= cell_choice <=9 and self.board.updateboard(cell_choice, player.symbol):
          break
        else:
          print("invalid move, try again")
      except ValueError:
        print("Please enter a number between 1 and 9")

    self.switch_player()

  def switch_player(self):
    self.current_player_index = 1 - self.current_player_index



  def quit_game(self):
    print("Thank you for playing")

newgame = game()
game.start_game()