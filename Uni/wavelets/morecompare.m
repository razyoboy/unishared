%more compare

for mu = 1:1:5;
    for sigma = 5:-1:1;
        x = -15:0.001:15;
        y = normpdf(x,mu,sigma);
        plot(x,y)
        hold on
    end
end

        

    