# resumes as list of strings
resumes= [
    "John Doe, john.doe@email.com, Python, Java, 3 years",
    "Jane Smith, jane.smith@email.com, JavaScript, React, 5 years",
    "Emily Davis, emily.davis@email.com, Python, Django, 2 years",
    "Michael Brown, michael.brown@email.com, C++, Linux, 4 years",
    "Tom Wilson, tom.wilson@email.com, Python, Flask, 3 years",
    "Tom Wilson, tom.wilson@email.com, Python, Flask, 3 years"
]

# extract data  and store in dictionary format
extracted_data = []
for resume in resumes: 
    name, email, *skills, experience = resume.split(", ") # skills is a list of skills, experience is the last element
    extracted_data.append({
        "name": name,
        "email": email,
        "skills": skills,
        "experience": experience
    })

# identify unique skills across all resumes using set
unique_skills = set()
for data in extracted_data:
    unique_skills.update(data["skills"])

# define required skills for a job role using tuple
required_skills = ("Python", "Django", "Flask")

# match candidates based on skill similarity atleast one required skill should be in candidate's skills
matched_candidates=[]
for data in extracted_data:
    if any(skill in data["skills"] for skill in required_skills):
        matched_candidates.append(data["name"])
print("Matched candidates for the job role:", matched_candidates)

# ranking candidates based on matching score
matching_scores = []
for data in extracted_data:
    score=sum(1 for skill in required_skills if skill in data["skills"])
    matching_scores.append((data["name"], score))

# sort candidates based on score in descending order simple way without key function
matching_scores.sort(key=lambda x:x[1], reverse=True)
print("Candidates ranked based on matching score:")
for name, score in matching_scores:
    print(f"{name}: {score}")

# detect duplicates
duplicate_resumes = set()
for resume in resumes:
    if resume in duplicate_resumes:
        print(f"Duplicate resume found: {resume}")
    else:
        duplicate_resumes.add(resume)

# Generate formatted shortlist report
print("\nShortlist Report:")
for name, score in matching_scores:
    if score > 0: 
        print(f"Candidate: {name}, Matching Score: {score}\n")


# Filter candidates based on experience
for data in extracted_data:
    if int(data["experience"].split()[0]) >=0:
        print(f"Candidate: {data['name']}, Experience: {data['experience']} years")