from statistics import median, mean
from math import factorial, floor

def part1():
    #small_input = [16,1,2,0,4,2,7,1,2,14]
    with open("day7.txt", "r") as tf:
        crab_subs = [int(i) for i in tf.read().split(",")]

    med = median(crab_subs)
    
    fuel = 0
    for crab  in crab_subs:
        fuel += abs(crab - med)
    print(fuel)

def part2():
    #crab_subs = [16,1,2,0,4,2,7,1,2,14]
    with open("day7.txt", "r") as tf:
        crab_subs = [int(i) for i in tf.read().split(",")]

    avg = floor(mean(crab_subs))
    
    print(avg)
    fuel = 0
    for crab  in crab_subs:
        fuel += sum(range(abs(crab - avg)+1))
    print(fuel)

#part1()
part2()