birthdays_dict = {
    "Albert Einstein": "02/15/1702",
    "Benjamin Franklin": "01/17/1706",
    "Ada Lovelace": "01/12/1700"
}

print(">>> Welcome to the birthday dictionary. We know the birthdays of:")
for name in birthdays_dict:
    print(f" {name}")

value = input(">>> Whose birthday do you want to look up? ")

print(f"{value}'s birthday is {birthdays_dict.get(value, f'Sorry, we don\'t have the birthday for {value}.')}")
