#[macro_use]
extern crate peroxide;
use peroxide::fuga::*;

fn main() {
    let init_state = State::<f64>::new(0f64, c!(5), c!(0));
    let mut ode_solver = ExplicitODE::new(f);
    
    ode_solver
        .set_method(ExMethod::RK4)
        .set_initial_condition(init_state)
        .set_step_size(1e-3)
        .set_times(10_000)
        .set_stop_condition(|x| x.get_state().param == 10f64);

    let result = ode_solver.integrate();
    
    let mut df = DataFrame::new(vec![]);
    df.push("t", Series::new(result.col(0)));
    df.push("y", Series::new(result.col(1)));

    df.print();
}

fn f(st: &mut State<f64>, _env: &NoEnv) {
    let y = st.value[0];
    let dy = &mut st.deriv;
    let k: f64 = 0.3;
    dy[0] = -k * y;
}
