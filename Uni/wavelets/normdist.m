% normpdf(x, mu, sigma)
% mu = mean, sigma = standard distribution
% defaults to mu = 0, sigma = 1

x = -3:0.00001:3;
y = normpdf(x,0,1);

plot(x,y,'linewidth',2)
title('Normal Probability Density Function')
ylabel('F(x), pdf')
xlabel('x')
legend('Normal Distribution with \mu = 0 and \sigma = 1')
grid on
