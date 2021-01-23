# ODE Benchmark

## 1. Runge-Kutta 4th order (RK4)

* step size: 1e-3

| Library | Version | Mean [ms] |
| :------ | :-----: | --------: |
| Peroxide | 0.7.6  | 13.8 ± 1.1 |  
| Peroxide | 0.30.2  | 2.4 ± 0.1 |  
| scipy `odeint` | 1.6.0 | 170.5 ± 4.5 |

## 2. Backward Differentiation Formual 1st order (BDF1)

* step size: 1e-4

| Library | Version | Mean [ms] |
| :------ | :-----: | --------: |
| Peroxide | 0.7.6 | 502 ± 13 |  
| Python | 3.7.1 | 14604 ± 355 |

## 3. Gauss-Legendre 4th order (GL4)

* step size: 1e-3

| Library | Version | Mean [ms] |
| :------ | :-----: | --------: |
| Peroxide | 0.7.6 | 99.3 ± 2.5 |  
| Peroxide | 0.30.2 | 99.3 ± 2.9 |  
