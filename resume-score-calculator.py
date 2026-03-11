name=input("enter your name ")
experience_years = int(input("enter your years of experience "))
skills = int(input("enter the number of skills you have "))
projects = int(input("enter the number of projects you have completed "))
# calculate score
score = (experience_years * 2) + (skills * 3) + (projects * 5)
# print result
print(f"{name}, your resume score is: {score}")