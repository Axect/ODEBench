bdf1 = readtable("bdf1.csv");
gl4 = readtable("gl4.csv");
rk4 = readtable("rk4.csv");

result = [rk4.mean(1), rk4.mean(2), bdf1.mean(2), bdf1.mean(1), gl4.mean(1)];
mins = [rk4.min(1), rk4.min(2), bdf1.min(2), bdf1.min(1), gl4.min(1)];
maxs = [rk4.max(1), rk4.max(2), bdf1.max(2), bdf1.max(1), gl4.max(1)];
labels = ["Rust(RK4)", "Python(RK4)", "Rust(BDF1)", "Python(BDF1)", "Rust(GL4)"];

p = bar(1:5, result);
hold on
ax = ancestor(p, 'axes');
set(gca, 'XTickLabel', labels)
set(gca, 'YScale', 'log')
xrule = ax.XAxis;
xrule.FontWeight = 'bold';
title("Benchmark for various ODE solvers", 'FontSize', 20)

er = errorbar(1:5, result, mins, maxs);
er.Color = [0 0 0];
er.LineStyle = 'none';
er.CapSize = 14;

hold off

print('benchmark','-dpng','-r300')