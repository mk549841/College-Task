for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    c=0
    dum = []
    dic = {0: 1}

    for i in a:
        dic[i] = dic.get(i, 0) + 1
    for i in dic:
        dum.append((i, dic[i]))

    dum = sorted(dum, reverse=True)

    x = []

    for i, j in dum:
        if j > 1:
            x.append(i)
            c=c+1
        if j > 3:
            x.append(i)
            c=c+1

        if len(x) >= 2:
            break

    if len(x) >= 2:
        print(x[0] * x[1],c)
    else:
        print(-1)
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    c=0
    dum = []
    dic = {0: 1}

    for i in a:
        dic[i] = dic.get(i, 0) + 1
    for i in dic:
        dum.append((i, dic[i]))

    dum = sorted(dum, reverse=True)

    x = []

    for i, j in dum:
        if j > 1:
            x.append(i)
            c=c+1
        if j > 3:
            x.append(i)
            c=c+1

        if len(x) >= 2:
            break

    if len(x) >= 2:
        print(x[0] * x[1],c)
    else:
        print(-1)

/*
Ishaan has a craving for sticks. He has N sticks. He observes that some of his sticks are of the same length, and thus he can make squares out of those.
He wants to know how big a square he can make using those sticks as sides. Since the number of sticks is large, he can't do that manually. Can you tell him the maximum area of the biggest square that can be formed.
Also calculate how many such squares can be made using the sticks.

Input : 
First line of input contains a single integer T denoting the number of test cases.
The first line of each test case contains an integer N denoting number of sticks.
The next line contains N space-separated integers denoting the length of the sticks.

Output : 
For each test case, print two space-separated integers denoting the maximum area and the number of such squares.
If no square can be formed, print -1.

Constraints : 
1 <= T <= 100
1 <= N <= 250
1 <= Stick(i) <= 10^3
*/
