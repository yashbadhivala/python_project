print("Pattern & Number Analyzer")

while True:
    print("\n1. Pattern")
    print("2. Number Analysis")
    print("3. Quit")

    option = input("Enter option: ")

    if option == "1":
        rowCount = int(input("Rows: "))
        if rowCount <= 0:
            print("Break! wrong input.")
            break
        for x in range(1, rowCount+1):
            print("*" * x)
    elif option == "2":
        s = int(input("Start: "))
        e = int(input("End: "))
        if s >= e:
            print("Invalid range, use continue.")
            continue
        summ = 0
        for n in range(s, e+1):
            if n % 2 == 0:
                print(n, "is Even")
            else:
                print(n, "is Odd")
            summ += n
        print("Sum =", summ)
    elif option == "3":
        print("Bye Bye!")
        break
    else:
        print("Try again!")
