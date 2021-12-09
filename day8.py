def part1(lines):

  numbers = {
    2: 1,
    3: 7,
    4: 4,
    7: 8,
  }
  sum = 0
  for line in lines:
    input = line.split("|")
    nums = input[1].split()
    for num in nums:
      if len(num) in numbers:
        print(num)
        sum += 1

  print(sum)

def part2(lines):
  numbers = {
    2: 1,
    3: 7,
    4: 4,
    7: 8,
  }
  
  total = 0
  for line in lines:
    decoder = {}
    input = line.split("|")
    known = input[0].split()
    i = 0
    
    while len(decoder) < 4:
      idx = i%len(known)
      if len(known[idx]) in numbers:
        decoder[numbers[len(known[idx])]] = set(known[idx])
        known.pop(idx)
      i+=1
    i = 0
  
    while len(decoder) < 10:
      idx = i%len(known)
      if not 9 in decoder:
        maybe_nine = set(known[idx])
        if decoder[4].issubset(maybe_nine):
          diff = maybe_nine.difference(decoder[4])
          if len(diff) == 2:
            decoder[9] = maybe_nine
            known.pop(idx)
            continue
      elif not 2 in decoder and 9 in decoder and len(known[idx]) == 5:
        maybe_two = set(known[idx])
        if not maybe_two.issubset(decoder[9]):
          decoder[2] = maybe_two
          known.pop(idx)
          continue
      elif not 3 in decoder:
        maybe_three = set(known[idx])
        if decoder[1].issubset(maybe_three):
          diff = maybe_three.difference(decoder[1])
          if len(diff) == 3:
            decoder[3] = maybe_three
            known.pop(idx)
            continue
      elif not 0 in decoder:
        maybe_zero = set(known[idx])
        if decoder[1].issubset(maybe_zero):
          decoder[0] = maybe_zero
          known.pop(idx)
          continue
      elif not 6 in decoder:
        maybe_six = set(known[idx])
        left_line = decoder[8].difference(decoder[3])
        if left_line.issubset(maybe_six):
          decoder[6] = maybe_six
          known.pop(idx)
          continue
      else:
        decoder[5] = set(known[idx])
     

      i+=1
    result = ""
    for number in input[1].split():
      for k, v in decoder.items():
        if v == set(number):
          result += str(k)
    print(f"this result: {result}")
    total += int(result)

  print(total)
    


with open("day8.txt", "r") as tf:
      lines = tf.read().split("\n")
part1(lines)
part2(lines)