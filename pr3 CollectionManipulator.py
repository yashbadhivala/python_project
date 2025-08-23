bigList = []

while True:
    print("\n[1] Add [2] Show [3] Update [4] Delete [5] Subjects [6] Exit")
    choose = input("Choice: ")

    if choose == "1":
        rid = int(input("Roll No: "))
        nm = input("Name: ")
        ag = int(input("Age: "))
        gd = input("Grade: ")
        db = input("DOB (YYYY-MM-DD): ")
        sb = input("Subjects (comma separated): ")
        lockKey = (rid, db)
        sbset = set([k.strip() for k in sb.split(",") if k.strip()])
        rec = {"idkey": lockKey, "name": nm, "age": ag, "grade": gd, "subjects": list(sbset)}
        bigList.append(rec)
        print("Added one record.")
    elif choose == "2":
        if len(bigList) == 0:
            print("No records available.")
        else:
            for rec in bigList:
                rid, db = rec["idkey"]
                print(f"ID:{rid} | Name:{rec['name']} | Age:{rec['age']} | Grade:{rec['grade']} | DOB:{db} | Subjects:{', '.join(rec['subjects'])}")
    elif choose == "3":
        who = int(input("Roll to update: "))
        flag = False
        for rec in bigList:
            if rec["idkey"][0] == who:
                flag = True
                print("1=Age  2=Subjects")
                ch = input("Field: ")
                if ch == "1":
                    rec["age"] = int(input("Enter new age: "))
                elif ch == "2":
                    rec["subjects"] = list(set([q.strip() for q in input("Enter subjects: ").split(",") if q.strip()]))
                print("Updated.")
                break
        if not flag:
            print("Roll not found.")
    elif choose == "4":
        who = int(input("Roll to delete: "))
        position = -1
        for i in range(len(bigList)):
            if bigList[i]["idkey"][0] == who:
                position = i
                break
        if position >= 0:
            del bigList[position]
            print("Removed record.")
        else:
            print("Not found.")
    elif choose == "5":
        offered = set()
        for r in bigList:
            offered |= set(r["subjects"])
        print("Offered:", ", ".join(sorted(offered)) if offered else "None")
    elif choose == "6":
        print("Exit. Bye!")
        break
    else:
        print("Invalid.")
