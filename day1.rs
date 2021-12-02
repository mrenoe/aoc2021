
use std::fs;

fn main(){
  println!("{}", day1());
  println!("{}", day2());
}

fn day1() -> i32 {
  let depths = get_input();
  let mut prev = depths[0];
  let mut cnt = 0;
  for depth in depths {
    if depth > prev{
      cnt += 1;
    }
    prev = depth;
  }
  return cnt
}

fn day2() -> usize {
  let depths = &get_input();
  depths.windows(4).filter(|w| w.first() < w.last()).count() 
}


fn get_input() -> Vec<i32> {
  let contents = fs::read_to_string("day1.txt")
    .expect("Something went wrong reading file");
  let numbers: Vec<i32> = contents.split("\n")
    .map(|s| s.parse().unwrap())
    .collect();
  return numbers;
}
