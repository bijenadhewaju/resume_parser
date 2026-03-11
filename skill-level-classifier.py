
name = input("enter your name: ")
skill_amount = int(input("enter the number of skills you have: "))
if skill_amount < 3:
    skill_level = "Beginner"
elif skill_amount < 6:
    skill_level = "Intermediate"
else:
    skill_level = "Advanced"
print(f"{name}, based on your {skill_amount} skills, you are at the {skill_level} level.")