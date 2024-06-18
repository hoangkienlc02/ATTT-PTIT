ok = 0
def main1():
    main()
    print(ok)
def main():
    if 4 % 2 == 0:
        ok = 1
    else: ok = 2
main1()