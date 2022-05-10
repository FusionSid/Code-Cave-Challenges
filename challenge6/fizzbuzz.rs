fn main() {
    for n in 1..101 {
        fizzbuzz(n);
    }
}

fn fizzbuzz(n:i32) {
    if n % 3 == 0 && n % 5 == 0 {
        println!("FizzBuzz");
    } else if n % 3 == 0 {
        println!("Fizz");
    } else if n % 5 == 0 {
        println!("Buzz");
    } else {
        println!("{}", n);
    }
}