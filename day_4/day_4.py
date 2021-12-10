def get_mock_bingo_info():
  with open('mock_input.txt') as file:
    info = file.read().strip().split("\n\n")
    number_draws = [int(num) for num in info[0].split(",")]
    bingo_boards = [[[int(col) for col in row.split()] for row in board.split("\n")] for board in info[1:]]
    return (number_draws, bingo_boards)

def get_bingo_info():
  with open('input.txt') as file:
    info = file.read().strip().split("\n\n")
    number_draws = [int(num) for num in info[0].split(",")]
    bingo_boards = [[[int(col) for col in row.split()] for row in board.split("\n")] for board in info[1:]]
    return (number_draws, bingo_boards)

# part 1

(number_draws, bingo_boards) = get_bingo_info()

def mark_board(board, number):
  for row in board:
    row[:] = [None if col == number else col for col in row]

def check_board(board):
  for row in board:
    if row.count(None) == len(row):
      return True
  for col in zip(*board):
    if col.count(None) == len(col):
      return True
  return False

def get_winning_board_and_number():
  # draw numbers
  for number in number_draws:
    # for each board
    for board in bingo_boards:
      # mark drawn number on board
      mark_board(board, number)
      # check if board is a winner
      is_winner = check_board(board)
      if is_winner:
        return (board, number)

def get_winning_score():
  winning_board, winning_number = get_winning_board_and_number()
  unmarked_sum = 0
  for row in winning_board:
    unmarked_sum += sum(filter(None, row))
  return unmarked_sum * winning_number

#print(get_winning_score())

# part 2

def get_last_winning_board_and_number():
  winning_board_and_number = (None, None)
  # draw numbers
  for number in number_draws:
    # for each board
    for board in bingo_boards:
      is_already_winner = check_board(board)

      if not is_already_winner:
        # mark drawn number on board
        mark_board(board, number)
        # check if board is a winner
        is_winner = check_board(board)
        if is_winner:
          winning_board_and_number = (board, number)
  return winning_board_and_number

def get_last_winning_score():
  winning_board, winning_number = get_last_winning_board_and_number()
  unmarked_sum = 0
  for row in winning_board:
    unmarked_sum += sum(filter(None, row))
  return unmarked_sum * winning_number

print(get_last_winning_score())