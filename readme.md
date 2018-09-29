# How does this work?

## Let's start with bloxlang
bloxlang is not lodestone, at least right now. It has a simple syntax with built ins. built ins are llvmlite methods. This simplifies over writing rust. 
bloxlang will interpret a file and if it will run llvmlite methods. As part of these methods it will generate llvm ir.

Once the ir is generated it can be combined with Rust code to get system call bindings.

Steps to compile the compiler then compile the language:
 - `python main.py my_compiler.blox > build/bloxlang.ll`
    - In this example we'll output ir to stdout 
 - `llc -filetype=obj build/bloxlang.ll -o build/bloxlang.o`
 - `cargo build`
    - cargo will build the ext object file. This will contain a `print` method.
 - `gcc -o build/compiler build/lib/ext.o build/bloxlang.o` 

The python projects interpret bloxlang and creates ir code. This ir code does not need to be bloxlang just a 
simple ir application.  