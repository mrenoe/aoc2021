
from typing import Counter


def part1():
    #todays_fish = [3,4,3,1,2]
    with open("day6.txt", "r") as tf:
        todays_fish = [int(i) for i in tf.read().split(",")]
    tomorrows_fish = []
    days = 80

    for i in range(days):
        for fish in todays_fish:
            if fish == 0:
                tomorrows_fish.append(6)
                tomorrows_fish.append(8)
            else:
                tomorrows_fish.append(fish-1)
        todays_fish = tomorrows_fish.copy()
        tomorrows_fish.clear()
        print(f"day: {i}, fish = {len(todays_fish)}")
    #print(todays_fish)

def part2():
    #todays_fish = [3,4,3,1,2]
    with open("day6.txt", "r") as tf:
        fish = Counter([int(i) for i in tf.read().split(",")])
    print(fish)
    
    days = 256
    tomorrows_fish = {}
    for i in range(days):
        
        tomorrows_fish[8] = fish[0]
        tomorrows_fish[7] = fish[8]
        tomorrows_fish[6] = fish[0] + fish[7]
        tomorrows_fish[5] = fish[6]
        tomorrows_fish[4] = fish[5]
        tomorrows_fish[3] = fish[4]
        tomorrows_fish[2] = fish[3]
        tomorrows_fish[1] = fish[2]
        tomorrows_fish[0] = fish[1]
            

        fish = tomorrows_fish.copy()
        tomorrows_fish.clear()
    
    fish_cnt = fish[8]+ fish[7]+ fish[6]+ fish[5]+ fish[4]+ fish[3]+ fish[2]+ fish[1]+ fish[0]
    print(f"fish = {fish_cnt}")
    #print(todays_fish)

part2()
part1()