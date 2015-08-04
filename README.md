Fun with FFI
------------

It's pretty awesome that we now have the option to do FFI things in languages
saner than C. An area where this would come in handy is doing concurrent/parallel
tasks that aren't super well supported in more dynamic languages.

What we're doing here is calling Rust and Go(1.5) to do parallel Monte Carlo
simulations estimating pi and averaging the results.

Note: Go 1.5 is essential to this because Go didn't have shared library support
until 1.5. Also in Go 1.5 all Cpus are automatically used.

## Setup

So for this to work you need to have working Rust and Go installations. Rust
is probably fine 1.0+. For Go we need 1.5+.

I'm using Rust 1.2 beta and Go1.5 beta3.

To build the shared libraries:

```
cd monte-rs
cargo build --release
```

```
cd monte-go
go build -buildmode=c-shared -o libgomonte.so
```
