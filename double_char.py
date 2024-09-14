current_String = input()
while current_String != "End":
    if current_String != "SoftUni":
        for letter in current_String:
            print(letter * 2, end="")
        print()
    current_String = input()
