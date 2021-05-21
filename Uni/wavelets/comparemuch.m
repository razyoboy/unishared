x = -15:0.0001:15;
y0 = normpdf(x,0,2);
y1 = normpdf(x,2,5);
y2 = normpdf(x,3,1);
y3 = normpdf(x,-4,3);

plot(x,y0,x,y1,x,y2,x,y3,'linewidth',2)
ylabel('F(x),pdf')
xlabel('x')
legend('\mu = 0, \sigma = 2','\mu = 2, \sigma = 5', '\mu = 3, \sigma = 1', '\mu = -4, \sigma = 3')
grid on
title('Comparision Between Various Values of \mu and \sigma')

