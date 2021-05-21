for a = 1:1:5
    x = -15:0.000001:15;
    y = normpdf(x,0,a);
    
    plot(x,y,'linewidth',2)
    title('Comparision Between Different Values of \sigma with a constant \mu = 0')
    ylabel('F(x), pdf')
    xlabel('x')
    legend('\sigma = 1','\sigma = 2','\sigma = 3','\sigma = 4','\sigma = 5')
    hold on
    grid on
end
