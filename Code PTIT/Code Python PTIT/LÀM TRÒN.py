for t in range(int(input())):
    i = input()
    n = int(i)
    s = list(i)
    if (n>10):      
        for i in range(len(s)-1,0,-1):
            if (int(s[i])>=5):
                s[i-1] = str(int(s[i-1])+1)
            s[i]="0"
    print("".join(s))
