## What is this project?
iLodestone is not lodestone, at least right now. It has a simple syntax with built ins. built ins are llvmlite methods. This simplifies over writing rust. 
iLodestone will interpret a file and if it will run iLodestone methods. As part of these methods it will generate llvm ir.

Once the ir is generated it can be combined with Rust code to get system call bindings.

The build.rs file in the rust directory will do some magic to create lodestone.

Diagram:
```
 -> lodestone.ldst -> iLodestone -> output object + rust code -> rust compiler -> lodestone
```

## iLodestone example

 - `println(1 + 2)`