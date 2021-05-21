%*(0,1)
x = [-10:.1:10];
y = normpdf(x,0,1);%(x,mu,sigma)
plot(x,y)
title('Normal distribution(µ = 0,σ =1)')
xlabel('Observations')
ylabel('Probability density')

%mu0-2 with function
x = -5:0.1:5;
for mu = 0:0.1:2
    y = 0;
  
    y = 1/sqrt(2*pi).*exp((-(x-mu).^2)./2);
    plot(x,y)
    title('Normal distribution with various µ when σ = 1')
    xlabel('Observations')
    ylabel('Probability density')
    hold on
    pause(0.5)
end

%mu =0-2 with syntax
x = [-5:.1:5];
for mu = 0:0.1:2
    s = 1;
    y = normpdf(x,mu,s);%(x,mu,sigma)
    plot(x,y)
    hold on
    pause(0.5)
end

%*(0,2)
x = [-10:.1:10];
y = normpdf(x,0,2);%(x,mu,sigma)
plot(x,y)
title('Normal distribution(µ = 0,σ =2)')
xlabel('Observations')
ylabel('Probability density')

%compare s
x = [-20:0.1:20];
y0 = normpdf(x,0,1);
y1 = normpdf(x,0,2);
y2 = normpdf(x,0,3);
y3 = normpdf(x,0,4);
plot(x,y0,'-r',x,y1,'--k',x,y2,'-.b',x,y3,'.-m')
legend('σ = 1','σ = 2','σ = 3','σ = 4')
title('Comparing of changes when σ is different (cannot be negative)')
xlabel('Observations')
ylabel('Probability density')

%comparing mu
x = [-20:0.1:20];
y0 = normpdf(x,0,1);
y1 = normpdf(x,1,1);
y2 = normpdf(x,-1,1);
y3 = normpdf(x,2,1);
y4 = normpdf(x,-2,1);
plot(x,y0,'-r',x,y1,'--k',x,y2,'-.b',x,y3,'.-m',x,y4,'-c')
legend('µ = 0','µ = 1','µ = -1','µ = 2','µ = -2')
title('Comparing of changes when µ is different (σ = 1)')
xlabel('Observations')
ylabel('Probability density')

%comparing with variated parameters
x = [-20:0.1:20];
y0 = normpdf(x,0,1);
y1 = normpdf(x,1,1);
y2 = normpdf(x,-1,1);
y3 = normpdf(x,1,2);
y4 = normpdf(x,-1,2);
y5 = normpdf(x,2,1);
y6 = normpdf(x,2,2);
y7 = normpdf(x,-2,2);
plot(x,y0,'b',x,y1','g',x,y2,'r',x,y3,'c',x,y4,'m',x,y5,'k',x,y6,'y',x,y7,'-.b')
legend('(µ = 0,σ = 1)','(µ = 1,σ = 1)','(µ = 0,σ = 1)','(µ = -1,σ = 1)',...
'(µ = 1,σ = 2)','(µ = -1,σ = 2)','(µ = 2,σ = 1)','(µ = 2,σ = 2)',...
'(µ = -2,σ = 2)')
title('Comparing of changes in variated parameter µ and σ')
xlabel('Observations')
ylabel('Probability density')




