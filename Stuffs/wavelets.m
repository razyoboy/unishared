%Standard distribution (Figure 1)
x = [-10:.1:10];
y = normpdf(x,0,1);%(x,mu,sigma)
plot(x,y,'LineWidth',2)
title('Normal distribution(µ = 0,σ =1)','FontSize', 24)
xlabel('Observations','FontSize', 24)
ylabel('Probability density','FontSize', 24)

%µ = 0:0.1:2 animated
v = VideoWriter('mean.avi');
v.FrameRate = 5;
open(v);
x = [-5:.1:5];
for mu = 0:0.1:2
    s = 1;
    y = normpdf(x,mu,s);%(x,mu,sigma)
    plot(x,y)
    hold on
    pause(0.001)
    frame = getframe(gcf);
    writeVideo(v,frame);
end
close(v);

%σ = 0.5:0.5:2 animated
v = VideoWriter('sigma.avi');
v.FrameRate = 5;
open(v);
x = [-10:0.1:10];
for s = 0.5:0.5:2%can't be zero
    mu = 0;
    y = normpdf(x,mu,s);
    plot(x,y,'LineWidth',2)
    legend({'σ = 0.5','σ = 1','σ = 1.5','σ = 2'},'FontSize',10)
    hold on
    pause (0.001)
    frame = getframe(gcf);
    writeVideo(v,frame);
end
close(v);


%compare σ(Figure2b)
x = [-15:0.1:15];
y0 = normpdf(x,0,1);
y1 = normpdf(x,0,2);
y2 = normpdf(x,0,3);
y3 = normpdf(x,0,4);
plot(x,y0,'-r',x,y1,'--k',x,y2,'-.b',x,y3,'.-m','LineWidth',2)
legend({'σ = 1','σ = 2','σ = 3','σ = 4'},'FontSize',24)
title('Comparing of changes when σ is different (σ > 0 and µ = 0)',...
'FontSize',24)
xlabel('Observations','FontSize',24)
ylabel('Probability density','FontSize',24)

%comparing µ (Figure2a)
x = [-10:0.1:10];
y0 = normpdf(x,0,1);
y1 = normpdf(x,1,1);
y2 = normpdf(x,-1,1);
y3 = normpdf(x,2,1);
y4 = normpdf(x,-2,1);
plot(x,y0,'-r',x,y1,'--k',x,y2,'-.b',x,y3,'.-m',x,y4,'-g','LineWidth',2)
legend({'µ = 0','µ = 1','µ = -1','µ = 2','µ = -2'},'FontSize',24)
title('Comparing of changes when µ is different (σ = 1)','FontSize', 24)
xlabel('Observations','FontSize', 24)
ylabel('Probability density','FontSize', 24)

%comparing with variated parameters (Figure3)
x = [-15:0.1:15];
y0 = normpdf(x,0,1);
y1 = normpdf(x,1,2);
y2 = normpdf(x,-1,1);
y3 = normpdf(x,1,2);
y4 = normpdf(x,-1,2);
y5 = normpdf(x,2,1);
y6 = normpdf(x,2,2);
y7 = normpdf(x,-2,2);
plot(x,y0,'b',x,y1','g',x,y2,'r',x,y3,'c',x,y4,'m',x,y5,'k',x,y6,'y',x,y7,...
'-.b','LineWidth',2)
legend('(µ = 0,σ = 1)','(µ = 1,σ = 1)','(µ = 0,σ = 1)','(µ = -1,σ = 1)',...
'(µ = 1,σ = 2)','(µ = -1,σ = 2)','(µ = 2,σ = 1)','(µ = 2,σ = 2)',...
'(µ = -2,σ = 2)','FontSize', 24)
title('Comparing of changes in diversed parameter µ and σ','FontSize', 24)
xlabel('Observations','FontSize', 24)
ylabel('Probability density','FontSize', 24)

%comparing with variated parameters (Figure3)
x = [-15:0.1:15];
y0 = normpdf(x,0,1);
y1 = normpdf(x,0.5,1.5);
y2 = normpdf(x,1,2);
y3 = normpdf(x,1.5,2.5);
y4 = normpdf(x,2,3);

plot(x,y0,'b',x,y1','g',x,y2,'r',x,y3,'k',x,y4,'m','LineWidth',2)
legend('(µ = 0,σ = 1)','(µ = 0.5,σ = 1.5)','(µ = 1,σ = 2)','(µ = 1.5,σ = 2.5)',...
'(µ = 2,σ = 3)','FontSize', 24)
title('Comparing of changes in diversed parameter µ and σ','FontSize', 24)
xlabel('Observations','FontSize', 24)
ylabel('Probability density','FontSize', 24)


%Nopparuj Jongserechoke 6213460 EGBI โปรดให้เครดิตคนทำ (me)


