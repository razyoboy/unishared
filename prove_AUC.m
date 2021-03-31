%error function plot
x = -5:0.1:5;
y = erf(x);
plot(x,y,'LineWidth',2)
title('An error function','FontSize',24)

%error function value
x = -5:1:5;
y = erf(x)

%AUC = 1 ?
upper = (0.5)*erf(inf/sqrt(2))
lower = (0.5)*erf(-inf/sqrt(2))
AUC = upper - lower

%Nopparuj Jongserechoke 6213460 EGBI โปรดให้เครดิตคนทำ (me)