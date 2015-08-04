extern crate rand;

use rand::distributions::{IndependentSample, Range};
use std::thread;
use std::sync::Arc;
use std::sync::mpsc;

fn simulate_pi(needles: i32) -> f64 {
    let mut hits = 0;
    let between = Range::new(-1f64, 1.);
    let mut rng = rand::thread_rng();

    for _ in 0..needles {
        let x = between.ind_sample(&mut rng);
        let y = between.ind_sample(&mut rng);

        if x*x + y*y <= 1. {
            hits += 1;
        }

    }
    4. * (hits as f64) / (needles as f64)
}

#[no_mangle]
pub extern fn estimate_pi(sims: i32, needles: i32) -> f64 {
    let mut data: Vec<f64> = Vec::new();
    let nx = Arc::new(needles);

    let (tx, rx) = mpsc::channel();

    for _ in 0..sims {
        let nx = nx.clone();
        let tx = tx.clone();

        thread::spawn(move || {
            let val = simulate_pi(*nx);
            tx.send(val).unwrap();
        });
    }

    // via channels
    for _ in 0..sims {
        let val = rx.recv().unwrap();
        data.push(val);
    }

    // average
    let sum = data.iter().fold(0f64, |mut sum, &val| { sum += val; sum });
    sum / (sims as f64)
}
