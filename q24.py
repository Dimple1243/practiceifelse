abhi=int(input("enter the people "))
divya=int(input("enter the people1 "))
shalu=int(input("enter the people "))
if abhi<divya and abhi<shalu:
    if divya>abhi and divya>shalu:
        print("abhi is youngest")
        print("divya is oldest")
    else:
        print("abhi is youngest")
        print("shalu is oldest")
elif divya<abhi and divya<shalu:
    if abhi>divya and abhi>shalu:
        print("divya is youngest")
        print("abhi is oldest")
    else:
        print("divya is youngest")
        print("shalu is oldest")
elif shalu<abhi and shalu<divya:
    if abhi>shalu and abhi>divya:
        print("shalu is youngest")
        print("abhi is oldest")
    else:
        print("shalu is youngest")
        print("divya is oldest")