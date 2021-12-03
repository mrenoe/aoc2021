


def get_input():
    with open("day3.txt", "r") as tf:
        lines = tf.read().split("\n")
    return lines

def part1():
    input = get_input()
    bit_lengths = len(input[0])
    gamma = ""
    for bit in range(bit_lengths):
        ones_cnt = 0
        zeros_cnt = 0
        for line in input:
            if line[bit] == '0':
                zeros_cnt += 1
            else:
                ones_cnt += 1
        if ones_cnt > zeros_cnt:
            gamma += "1"
        else:
            gamma += "0"
    gamma_dec = int(gamma, 2)
    epsilon = (1 << bit_lengths) - 1 - gamma_dec
    print(f"Power = {gamma_dec * epsilon}")


def part2():
    input = get_input()
    bit_lengths = len(input[0])
    o2_in = input
    
    offset = 0
    o2_val = 0
    bit = 0
    while bit+offset < bit_lengths:
        ones_list = []
        zeros_list = []
        for line in o2_in:
            if line[bit] == '0':
                zeros_list.append(line)
            else:
                ones_list.append(line)
        if len(ones_list) >= len(zeros_list):
            o2_in = ones_list
        else:
            o2_in = zeros_list
        if len(o2_in) == 1:
            o2_val = o2_in[0]         
            break;
        elif len(o2_in) == 0:
            offset = 1
        else:
            bit += 1
    co2_in = input
    co2_val = 0
    
    bit = 0
    while bit+offset < bit_lengths:
        ones_list = []
        zeros_list = []
        for line in co2_in:
            if line[bit] == '0':
                zeros_list.append(line)
            else:
                ones_list.append(line)
        if len(zeros_list) <= len(ones_list):
            co2_in = zeros_list
            
        else:
            co2_in = ones_list
        if len(co2_in) == 1:
            co2_val = co2_in[0]         
            break;
        elif len(co2_in) == 0:
            offset = 1
        else:
            bit += 1
    co2 = int(co2_val, 2)
    o2 = int(o2_val, 2)
    print(f"life support = {o2} * {co2} = {co2*o2}")

            

#part1()
part2()