def day1():
  with open("day5.txt", "r") as tf:
      lines = tf.read().split("\n")

  coordinates = {}
  for line in lines:
    coords = line.split(" -> ")
    (x_1, y_1) = [int(p) for p in coords[0].split(",")]
    (x_2, y_2) = [int(p) for p in coords[1].split(",")]

    range_start = 0
    range_end = 0
    static = 0
    if x_1 == x_2:
      static = x_1    
      if y_1 > y_2:
        range_start = y_2
        range_end = y_1
      else:
        range_start = y_1
        range_end = y_2
      
      for coord in range(range_start, range_end +1):
        if (static, coord) in coordinates:
          coordinates[(static, coord)] += 1
        else:
          coordinates[(static, coord)] = 1
    elif y_1 == y_2:
      static = y_1
      if x_1 > x_2:
        range_start = x_2
        range_end = x_1
      else:
        range_start = x_1
        range_end = x_2

      for coord in range(range_start, range_end +1):
        if (coord, static) in coordinates:
          coordinates[(coord, static)] += 1
        else:
          coordinates[(coord, static)] = 1


  cnt = 0
  for (k,v) in coordinates.items():
    if v > 1:
      cnt += 1
  print(cnt)

def day2():
  with open("day5.txt", "r") as tf:
      lines = tf.read().split("\n")

  coordinates = {}
  for line in lines:
    coords = line.split(" -> ")
    (x_1, y_1) = [int(p) for p in coords[0].split(",")]
    (x_2, y_2) = [int(p) for p in coords[1].split(",")]
    range_start = 0
    range_end = 0
    static = 0
    if x_1 == x_2:
      static = x_1    
      if y_1 > y_2:
        range_start = y_2
        range_end = y_1
      else:
        range_start = y_1
        range_end = y_2
      
      for coord in range(range_start, range_end +1):
        if (static, coord) in coordinates:
          coordinates[(static, coord)] += 1
        else:
          coordinates[(static, coord)] = 1
    elif y_1 == y_2:
      static = y_1
      if x_1 > x_2:
        range_start = x_2
        range_end = x_1
      else:
        range_start = x_1
        range_end = x_2

      for coord in range(range_start, range_end +1):
        if (coord, static) in coordinates:
          coordinates[(coord, static)] += 1
        else:
          coordinates[(coord, static)] = 1
    else:
      direction_1 = 1
      direction_2 = 1
      if x_1 > x_2:
        direction_1 = -1
      if y_1 > y_2:
        direction_2 = -1
      for (x, y) in zip(range(x_1, x_2 + direction_1, direction_1), range(y_1, y_2 + direction_2, direction_2)):

        if (x, y) in coordinates:
          coordinates[(x, y)] += 1
        else:
          coordinates[(x, y)] = 1


  cnt = 0
  for (k,v) in coordinates.items():
    if v > 1:
      cnt += 1
  print(cnt)

day2()