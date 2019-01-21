extern crate peroxide;
use peroxide::*;

fn main() {
    let init = vec![5f64];
    let result = solve(f, init, (0, 10), 0.001, RK4);
    result.write_with_header("data/peroxide.csv", vec!["t", "y"], 4);
}

fn f(_t: Dual, ys: Vec<Dual>) -> Vec<Dual> {
    let y: Dual = ys[0];
    let k: f64 = 0.3;
    vec![-k * y]
}
