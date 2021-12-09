def part1(lines):
    map = []
    i = 0
    for line in lines:
        map.append([])
        for num in list(line):
            map[i].append(int(num))
        
    i+=1
    risk =0
    for i, row in enumerate(map):
        for j, v in enumerate(row):
            
            if i > 0:
                if v >= map[i-1][j]:
                    continue
            if i < len(map)-1:
                if v >= map[i+1][j]:
                    continue
            if j > 0:
                if v >= map[i][j-1]:
                    continue
            if j < len(row)-1:
                if v >= map[i][j+1]:
                    continue
            #print(f"lowpoint: {v} at i: {i}, j: {j}")
            risk += v+1
    print(risk)

def part2(lines):
    map = {}
    for i, line in enumerate(lines):
        for j, num in enumerate(line):
            map[i,j] = int(num)
    
    def search(x,y, seen):
        if (x,y) in seen:
            return
        seen[x,y] = 0
        h  = map.get((x,y), 9)
        if h == 9:
            return
        yield x,y
        yield from search(x+1, y, seen)
        yield from search(x-1, y, seen)
        yield from search(x, y+1, seen)
        yield from search(x, y-1, seen)
    
    sizes = []
    for (x,y), h in map.items():
        #If height exists in map
        if h < map.get((x+1, y), 10) and \
        h < map.get((x-1, y), 10) and \
        h < map.get((x, y+1), 10) and \
        h < map.get((x, y-1), 10):
            sizes.append(len(set(search(x,y, {}))))
    sizes.sort()
    print(sizes[-1] * sizes[-2] * sizes[-3])

with open("day9.txt", "r") as tf:
      lines = tf.read().split("\n")



#part1(lines)
part2(lines)