Fun with FFI
------------

It's pretty awesome that we now have the option to do FFI things in languages
saner than C. An area where this would come in handy is doing concurrent/parallel
tasks that aren't super well supported in more dynamic languages.

What we're doing here is calling Rust and Go(1.5) to do parallel Monte Carlo
simulations estimating Pi and averaging the results.

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
cd monte-go/src
go build -buildmode=c-shared -o libgomonte.so
```

## Usage

```
python monte.py -h

usage: monte.py [-h] [-l {go,python,rust}] S N

Run Monte Carlo Pi simulations in Python, Go or Rust.

positional arguments:
  S                     Number of simulations
  N                     Number of needles per simulation

optional arguments:
  -h, --help            show this help message and exit
  -l {go,python,rust}, --lang {go,python,rust}
                        language to run in, defaults to Python
```



## Results

These are some of the timings I got on my machine.

Python:

```
time python monte.py  -l=python 1000 10000

Running 1000 simulations with 10000 needles in "python".
Estimate Pi = 3.1420776
       18.41 real        18.02 user         0.16 sys
```

Go:

```
time python monte.py  -l=go 1000 10000

Running 1000 simulations with 10000 needles in "go".
Estimate Pi = 3.1413148
        4.82 real        15.15 user         0.49 sys
```

Rust:

```
time python monte.py  -l=rust 1000 10000

Running 1000 simulations with 10000 needles in "rust".
Estimate Pi = 3.1423152
        1.42 real         0.48 user         1.84 sys
```

So I'm not sure why the Go result is slower than the Rust result. Maybe it's
just that Rust is faster than Go, could be. But this is just loops for the most
part so I wouldn't expect one to be much slower than the other.

Go 1.5 is reported to be a bit slower than 1.4 since not everything has been
optimized yet from the great C purge; that might be it. I would compare with 1.4
buttttttt I can't so that's that!

On the bright side I have 4 cores on my machine and we got ~4x speedup at
minimum so that's nice!
