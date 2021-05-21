%Eqn. 6.20 is defined as, the summation of binopdf, hence we would use
%binocdf
%CI is at 95%

%First Group Non-Infected with CI of 90
%loop = [0.10 0.05 0.01];
disp('Please enter the number of sucess (x)')
xin = input('> ');
x = double(xin);
disp('And the total number of the event (n)')
nin = input('> ');
n = double(nin);
%%%!!!!  x = 957; n = 976  !!!!!!%%%
for loop = [0.10 0.05 0.01]
    CINum = 100*(1-loop);

    phat = x/n;
    p1 = 0.80:0.00001:1.00;
    p2 = 0.80:0.00001:1.00;
    LowerBond = 1 - binocdf(x-1,n,p1);
    alpha = loop;
    
    poslow = find(LowerBond <= (alpha/2));
    realposlow = max(poslow);

    LowerBondAns = p1(realposlow);

    UpperBond = binocdf(x,n,p2);
    posup = find(UpperBond <= alpha/2);
    realposup = min(posup);
    
    UpperBondAns = p2(realposup);

    disp(['For CI of ',num2str(CINum),'%, the probability (p-hat) is ', num2str(phat), ' with the CI intervals between ', num2str(LowerBondAns), ' and ', num2str(UpperBondAns)])
end 