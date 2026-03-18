students = [
    {"id": 101, "name": "Alice", "score": 85},
    {"id": 102, "name": "Bob", "score": 78},
    {"id": 103, "name": "Charlie", "score": 92}
]
    
for s in students:
        print(s["name"])
        
total = 0
for s in students:
    total += s["score"]
avg = total / len(students)
print(avg)

students.append({"id": 104, "name": "David", "score": 88})

for s in students:
    if s["id"] == 102:
        s["score"] = 88
        
students = [s for s in students if s["name"] != "Charlie"]

print("\nStudents scoring more than 80:")
for s in students:
    if s["score"] > 80:
        print(s["name"])
        
def get_score(student):
    return student["score"]

students.sort(key=get_score, reverse=True)
print(students)

top_student = students[0]
print("\nTop Student:", top_student["name"])

print("\nStudent Report:")
for s in students:
    score = s["score"]
    
    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    else:
        grade = "C"
        
    print(f"Name: {s['name']} | Score: {score} | Grade: {grade}")
    
grade_count = {"A": 0, "B": 0, "C": 0}

for s in students:
    if s["score"] >= 90:
        grade_count["A"] += 1
    elif s["score"] >= 80:
        grade_count["B"] += 1
    else:
        grade_count["C"] += 1
        
print("\nGrade Count:", grade_count)
        