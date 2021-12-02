use std::fs;

fn main(){
    part1()
}

fn part1() {
    let actions = get_input();
    let mut distance = 0;
    let mut depth = 0;
    for line in actions {
        println!("{}",line)
    }
}



fn get_input() -> Vec<Vec<&str>> {
    let contents = fs::read_to_string("day2.txt")
      .expect("Something went wrong reading file");
    let numbers: Vec<Vec<&str>> = contents
        .split("\n")
        .map(|s| s.split(" ")
        .collect::<Vec<&str>>())
        .collect();
    return numbers;
  }