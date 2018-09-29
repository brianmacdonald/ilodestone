use std::process::Command;

extern crate cc;

fn main() {
    let output = Command::new("ilodestone")
            .arg("--input_file")
            .arg("lodestone.ldst")
            .output()
            .expect("failed to execute process")
    let mut file = File::create("../build/lodestone.ll")?;
    file.write_all(output.as_bytes());
    drop(file)
    Command::new("llc")
            .arg("-filetype=obj")
            .arg("../build/lodestone.ll")
            .arg("../build/lodestone.o")
            .output()
            .expect("failed to execute process")
    cc::Build::new()
        .object("../build/lodestone.o")
        .shared_flag(true)
        .cpp_link_stdlib("stdc++")
        .pic(true)
        .compiler("gcc-7")
        .compile("lodestone.so");
}