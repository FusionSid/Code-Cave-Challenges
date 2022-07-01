use std::io;

fn main() {
    println!("Enter text: ");
    let mut input_text = String::new();

    io::stdin()
        .read_line(&mut input_text)
        .expect("Failed lmao get good");

    let text = input_text.chars().rev().collect::<String>();
    let mut new_text = String::new();

    for i in text.chars() {
        if i.is_uppercase() {
            let c = i.to_ascii_lowercase();
            new_text.push(c);
        } else {
            let c = i.to_ascii_uppercase();
            new_text.push(c);
        }
    }

    println!("{}", new_text);
}