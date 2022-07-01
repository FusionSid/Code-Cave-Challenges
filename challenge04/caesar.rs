use std::io;

// i am a begginer with this language so there is definitly a more faster and efficent way to do this
// but it works so im not complain 

fn main() {
    println!("Enter text: ");
    let mut input_text = String::new();
    io::stdin()
    .read_line(&mut input_text)
    .expect("Failed lmao get good");

    let mut shift = String::new();
    println!("Enter amount to shift: ");
    io::stdin()
        .read_line(&mut shift)
        .expect("Failed lmao get good");
    let shift = shift.trim().parse::<usize>().unwrap();

    let mut text = String::new();
    let alphabet = "abcdefghijklmnopqrstuvwxyz";
    
    for i in input_text.chars() {
        if i.is_alphabetic() {
            let mut index = 0;
            for x in alphabet.chars() {
                if x == i {
                    break;
                }
                index = index + 1;
            }
            let aindex = (index + shift) % 26;
            let alpha_char = alphabet.as_bytes()[aindex];
            text.push(alpha_char as char);
        } else {
            text.push(i);
        }

        
    }
    println!("{}", text);
}