# Input details to check eligibility for a job application

# ask user for input
name=input("enter your name ")
experience_years = int(input("enter your years of experience "))

if experience_years < 1:
    role="Intern or Trainee"
elif experience_years < 3:
    role="Junior Developer"
elif experience_years < 5:
    role="Mid-level Developer"
else:
    role="Senior Developer"

print(f"{name}, based on your {experience_years} years of experience, you are eligible for the role of {role}.")