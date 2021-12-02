

def get_input():
  with open("day1.txt", "r") as tf:
    lines = [int(x) for x in tf.read().split()]
  return lines

def part1():
  lines = get_input()
  last = lines[0]
  increases = 0
  for depth in lines:
    if depth > last:
      increases = increases + 1
    last = depth
  #print(increases)

def part2():
  lines = get_input()
  one = [lines[0], lines[1], lines[2]]
  two = [lines[1], lines[2], lines[3]]
  three = [lines[2], lines[3]]
  four = [lines[3]]
  lines = lines[4:]
  current_depth = sum(two)
  new_depth = sum(one)
  one.clear()
  increases = 0
  for depth in lines:
    
    if len(one) == 3:
      new_depth = sum(one)
      one.clear()
    else:
      one.append(depth)
    if len(two) == 3:
      new_depth = sum(two)
      two.clear()
    else:
      two.append(depth)
    if len(three) == 3:
      new_depth = sum(three)
      three.clear()
    else:
      three.append(depth)
    if len(four) == 3:
      new_depth = sum(four)
      four.clear()
    else:
      four.append(depth)
    if new_depth > current_depth:
      increases = increases + 1
    current_depth = new_depth


  if len(one) == 3:
    new_depth = sum(one)
  if len(two) == 3:
    new_depth = sum(two)
  if len(three) == 3:
    new_depth = sum(three)
  if len(four) == 3:
    new_depth = sum(four)
  if current_depth < new_depth:
      increases = increases + 1
  print(increases)


#part1()
part2()