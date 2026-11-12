import random

departments = ["Computer Science", "Software Engineering", "Cybersecurity", "Information Technology"]
levels = [100, 200, 300, 400]
dataset = []

for i in range(1, 6):
    dataset.append({
        "Student ID": f"STUDENT-{100 + i}",
        "Department": random.choice(departments),
        "Level": random.choice(levels),
        "Attendance (%)": round(random.uniform(70.0, 99.5), 1),
        "Avg Exam Score": round(random.uniform(50.0, 95.0), 1)
    })

# Print formatted table
print(f"{'Student ID':<15} | {'Department':<22} | {'Level':<6} | {'Attendance (%)':<15} | {'Avg Exam Score':<15}")
print("-" * 83)
for s in dataset:
    print(f"{s['Student ID']:<15} | {s['Department']:<22} | {s['Level']:<6} | {s['Attendance (%)']:<15} | {s['Avg Exam Score']:<15}")
  
