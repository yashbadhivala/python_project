print("Welcome to My Data Sheet")
print("Let's collect a few simple details.")

# Inputs
nam = input("Type your name: ")
ageNo = int(input("Type your age: "))
metersHeight = float(input("Type your height (meters): "))
fav_digit = int(input("Type your favourite number: "))

# Show type() and id()
print("\nCollected:")
for label, value in [("nam", nam), ("ageNo", ageNo), ("metersHeight", metersHeight), ("fav_digit", fav_digit)]:
    print(label, "=", value, "| type:", type(value), "| id:", id(value))

# Operator demo
born = 2025 - ageNo
print("\nEstimated birth year ->", born)
print("End of program.")