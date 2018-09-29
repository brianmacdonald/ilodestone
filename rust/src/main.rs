use std::fs::File;

extern {
    fn lodestone_main();
}

#[no_mangle]
pub extern fn fopen(filename: String) -> String {
    unsafe {
        let mut f = File::open(filename).expect("file not found");
        let mut contents = String::new();
        f.read_to_string(&mut contents)
            .expect("something went wrong reading the file");
        return contents;
    }
}

#[no_mangle]
pub extern fn fprint(message: &str) -> String {
    unsafe {
        println!("{}", &str);
    }
}

fn main() {
    println!("Calling lodestone from rust...");
    unsafe { lodestone_main() }
}