for a = 0:1:5
    x = -10:0.000001:10;
    y = normpdf(x,a,1);
    y1 = makedist('Normal');
    y1.mu = a;
    p = cdf(y1,x);
    
    plot(x,p,'linewidth',2)
    title('CDF Comparision Between Different Values of \mu with a constant \sigma = 1')
    ylabel('f(x), cdf')
    xlabel('x')
    legend('\mu = 0','\mu = 1','\mu = 2','\mu = 3','\mu = 4','\mu = 5')
    hold on
    grid on
end
