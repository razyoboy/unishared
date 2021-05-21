%MEGA COMPARE

for a = [1:1:5];
    x = -15:0.0001:15;
    y = normpdf(x,a,a);
    
    name = ['\mu, \sigma = ',num2str(a)];
    plot(x,y,'linewidth',2,'DisplayName',name)
    title('Comparision Between Various Values of \mu and \sigma')
    ylabel('F(x),pdf')
    xlabel('x')
    legend show
    hold on
    grid on
end

    