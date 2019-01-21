extern crate peroxide;
use peroxide::*;

pub fn main() {
   let result = solve(test, vec![5f64], (0, 10), 1e-4, BDF1(1e-15)); 
   result.write_with_header("data/peroxide_bdf1.csv", vec!["t", "y"], 6);
}

fn test(t: Dual, ys: Vec<Dual>) -> Vec<Dual> {
    let y = ys[0];
    vec![-0.3 * y]
}
