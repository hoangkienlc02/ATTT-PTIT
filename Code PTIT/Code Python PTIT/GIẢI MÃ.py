for i in range(int(input())):
    s = input()
    for i in range(0, len(s)-1, 2): # chạy từ 0 và có bước nhảy là 2 là vị trí của các chữ cái trong chuỗi đã nhập
        for j in range(0, int(s[i+1])):
            print(s[i], end = "")
    print()
'''
Input:
    2
    A8
    A2E1C4G3D1
Output:
    AAAAAAAA
    AAECCCCGGGD 
'''