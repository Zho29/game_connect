#Exercise 3.2
phrase="Pony stash token"
print(phrase[5:10])
print(phrase[-16:-12])
print(phrase[::-1])
print(phrase[::3])
print((phrase[11:]),(phrase[5:10]),(phrase[:4]))


#Exercise 3.3
name=input("Enter your first and last name: ")
birthday=input("Enter your birthday: ")  # 12012000
day=birthday[0:2]
month=birthday[2:4]
year=birthday[4:]
print(f"{name} was born on {day}/{month}/{year}")