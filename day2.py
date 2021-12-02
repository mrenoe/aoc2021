def get_input():
  with open("day2.txt", "r") as tf:
    lines = tf.read().split("\n")
  return lines

def part1():
    actions = get_input()
    depth = 0
    distance = 0
    for action in actions:
        (depth, distance, _) = navigate(depth, distance, action)
        

    print(f"Part 1: final position - distance {distance}, depth {depth} ")

def part2():
    actions = get_input()
    depth = 0
    distance = 0
    aim = 0
    for action in actions:
        (depth, distance, aim) = navigate(depth, distance, action, aim=aim)
    
    print(f"Part 2: final position - distance {distance}, depth {depth} ")

def navigate(depth, distance, action, aim=None):
    (keyword, increment) = action.split()
    if keyword == "forward":
        distance += int(increment)
        if aim is not None:
            depth = depth + (aim * int(increment))
    if keyword == "down":
        if aim is not None:
            aim += int(increment)
        else:
            depth += int(increment)
    if keyword == "up":
        if aim is not None:
            aim -= int(increment)
        else:
            depth -= int(increment)            

    return (depth, distance, aim)
    

part1()
part2()