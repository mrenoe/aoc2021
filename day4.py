from collections import OrderedDict


test_moves = [67,3,19,4,64,39,85,14,84,93,79,26,61,24,65,63,15,69,48,8,82,75,36,96,16,49,28,40,97,38,76,91,83,7,62,94,21,95,6,10,43,17,31,34,81,23,52,60,54,29,70,12,35,0,57,45,20,71,78,44,90,2,33,68,53,92,50,73,88,47,58,5,9,87,22,13,18,30,59,56,99,11,77,55,72,32,37,89,42,27,66,41,86,51,74,1,46,25,98,80]

def check_for_winner(boards):
  for board in range(len(boards)):
    if boards[board] is None:
      continue
    b = list(boards[board].items())
    
    if (b[0][1] and b[1][1] and b[2][1] and b[3][1] and b[4][1]) or \
        (b[5][1] and b[6][1] and b[7][1] and b[8][1] and b[9][1]) or \
        (b[10][1] and b[11][1] and b[12][1] and b[13][1] and b[14][1]) or \
        (b[15][1] and b[16][1] and b[17][1] and b[18][1] and b[19][1]) or \
        (b[20][1] and b[21][1] and b[22][1] and b[23][1] and b[24][1]):

          return board
      
    if (b[0][1] and b[5][1] and b[10][1] and b[15][1] and b[20][1]) or \
        (b[1][1] and b[6][1] and b[11][1] and b[16][1] and b[21][1]) or \
        (b[2][1] and b[7][1] and b[12][1] and b[17][1] and b[22][1]) or \
        (b[3][1] and b[8][1] and b[13][1] and b[18][1] and b[23][1]) or \
        (b[4][1] and b[9][1] and b[14][1] and b[19][1] and b[24][1]):

          return board
  return -1


def part1():
  with open("day4.txt", "r") as tf:
    lines = tf.read().split("\n")

  boards = {}
  board_count = 0
  boards[board_count] = OrderedDict()
  for line in lines:
    if not line:
      board_count += 1
      boards[board_count] = OrderedDict()
      continue
    else: 
      nums = line.split()
      for char in nums:
        boards[board_count][int(char)] = 0
  winning_move = -1
  winner = -1
  for move in test_moves:
    for board_num in range(len(boards)):
      boards[board_num][move] = 1
    winner = check_for_winner(boards)
    if winner > -1:
      winning_move = move
      break

  unmarked_sum = 0
  for (k, v) in boards[winner].items():
    if v == 0:
      unmarked_sum += k

  print(f"final score: {unmarked_sum * winning_move}")

def part2():
  
  with open("day4.txt", "r") as tf:
    lines = tf.read().split("\n")

  boards = {}
  board_count = 0
  boards[board_count] = OrderedDict()
  for line in lines:
    if not line:
      board_count += 1
      boards[board_count] = OrderedDict()
      continue
    else: 
      nums = line.split()
      for char in nums:
        boards[board_count][int(char)] = 0

  winning_move = -1
  winner = -2
  board_count = len(boards) +1
  winning_board = {}
  for i in range(len(test_moves)):
    for board_num in range(len(boards)):
      if boards[board_num] is not None:
        boards[board_num][test_moves[i]] = 1
    while winner != -1:
      winner = check_for_winner(boards)
      
      if winner > -1:  
        winning_board = boards[winner]
        boards[winner] = None   
        winning_move = test_moves[i]
        board_count -= 1
    winner = -2
  unmarked_sum = 0
  
  for (k, v) in winning_board.items():
    if v == 0:
      unmarked_sum += k

  print(f"final score: {unmarked_sum * winning_move}")

part1()
part2()

    