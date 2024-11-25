name = input("what is your name?")
birthday = int(input("when is your birthday?"))
age = 1403 - birthday
if age >= 18:
    print("you can vote!")
else:
    print("you can not vote!")    