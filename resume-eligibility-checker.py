experience = int(input("Enter your years of experience: "))
if experience < 2:
    print("Fresher Level Job")
elif experience < 5:
    print("Junior Level Job")
else:
    print("Senior Level Job")