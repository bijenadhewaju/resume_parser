# Resume Project Counter (using loop)
project_count = int(input("Enter the number of projects you have completed: "))
total_projects = 0
for i in range(project_count):
    project_name = input(f"Enter the name of project {i+1}: ")
    total_projects += 1
print(f"Total projects completed: {total_projects}")