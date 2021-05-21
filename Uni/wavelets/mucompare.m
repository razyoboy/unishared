for a = 0:1:5
    x = -5:0.00001:10;
    y = normpdf(x,a,1);
    
    plot(x,y,'linewidth',2)
    title('Comparision Between Different Values of \mu constant \sigma = 1')
    ylabel('F(x), pdf')
    xlabel('x')
    legend('\mu = 0','\mu = 1','\mu = 2','\mu = 3','\mu = 4','\mu = 5')
    hold on
    grid on
    
end 