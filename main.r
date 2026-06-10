use std::time::Instant;

// Linear Congruential Generator
fn lcg(seed: u64, a: u64, c: u64, m: u64) -> impl Iterator<Item = u64> {
    std::iter::successors(Some(seed), move |&value| {
        Some((a * value + c) % m)
    })
}

// Maximum subarray sum using Kadane's algorithm
fn max_subarray_sum(n: usize, seed: u64, min_val: i64, max_val: i64) -> i64 {
    let mut random_numbers = vec![0i64; n];
    let lcg_gen = lcg(seed, 1664525, 1013904223, 2u64.pow(32));
    
    for (i, &val) in lcg_gen.enumerate().take(n) {
        random_numbers[i] = (val % (max_val - min_val + 1) + min_val) as i64;
    }
    
    // Kadane's algorithm for maximum subarray sum
    let mut max_sum = i64::MIN;
    let mut current_sum = 0;
    
    for &num in &random_numbers {
        current_sum = num.max(current_sum + num);
        max_sum = max_sum.max(current_sum);
    }
    
    max_sum
}

fn total_max_subarray_sum(n: usize, initial_seed: u64, min_val: i64, max_val: i64) -> i64 {
    let mut total_sum = 0i64;
    let lcg_gen = lcg(initial_seed, 1664525, 1013904223, 2u64.pow(32));
    
    for seed in lcg_gen.take(20) {
        total_sum += max_subarray_sum(n, seed, min_val, max_val);
    }
    
    total_sum
}

fn main() {
    let n = 10000;
    let initial_seed = 42;
    let min_val = -10i64;
    let max_val = 10i64;
    
    let start_time = Instant::now();
    let result = total_max_subarray_sum(n, initial_seed, min_val, max_val);
    let end_time = Instant::now();
    
    let duration = end_time.duration_since(start_time);
    let seconds = duration.as_secs_f64();
    
    println!("Total Maximum Subarray Sum (20 runs): {}", result);
    println!("Execution Time: {:.6f} seconds", seconds);
}