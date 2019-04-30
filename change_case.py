#change case
print("This program changes case of string")

daString = input("paste string here")

print("1 = all upper case, 2 = all lower case, 3 = title case")

daCase = input("Input case preference: ")

if daCase == "1":
    print(daString.upper())
elif daCase == "2":
    print(daString.lower())
elif daCase == "3":
    print(daString.title())
else:
    print("wrong input, try again")