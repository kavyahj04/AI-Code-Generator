use std::time::Instant;

fn lcg(seed: u64, a: u64, c: u64, m: u64) -> impl Iterator<Item = u64> {
    std::iter::successors(Some(seed), move |&value| {
        Some((a.wrapping_mul(value).wrapping_add(c)) % m)
    })
}

fn max_subarray_sum(n: usize, seed: u64, min_val: i64, max_val: i64) -> i64 {
    let mut random_numbers = vec![0i64; n];
    let lcg_gen = lcg(seed, 1664525, 1013904223, 1u64 << 32);
    
    for (i, &val) in lcg_gen.take(n).enumerate() {
        random_numbers[i] = (val % (max_val - min_val + 1) + min_val) as i64;
    }
    
    let mut max_sum = i64::MIN;
    for i in 0..n {
        let mut current_sum = 0i64;
        for j in i..n {
            current_sum += random_numbers[j];
            if current_sum > max_sum {
                max_sum = current_sum;
            }
        }
    }
    max_sum
}

fn total_max_subarray_sum(n: usize, initial_seed: u64, min_val: i64, max_val: i64) -> i64 {
    let mut total_sum = 0i64;
    let lcg_gen = lcg(initial_seed, 1664525, 1013904223, 1u64 << 32);
    
    for seed in lcg_gen.take(20) {
        total_sum += max_subarray_sum(n, seed, min_val, max_val);
    }
    total_sum
}

fn main() {
    let n = 10000;
    let initial_seed = 42;
    let min_val = -10;
    let max_val = 10;
    
    let start_time = Instant::now();
    let result = total_max_subarray_sum(n, initial_seed, min_val, max_val);
    let end_time = Instant::now();
    
    let duration = end_time - start_time;
    println!("Total Maximum Subarray Sum (20 runs): {}", result);
    println!("Execution Time: {:.6f} seconds", duration.as_secs_f64());
}