def get_spm_grade(mark):
    if mark >= 90:
        return "A+"
    elif mark >= 80:
        return "A"
    elif mark >= 70:
        return "A-"
    elif mark >= 65:
        return "B+"
    elif mark >= 60:
        return "B"
    elif mark >= 50:
        return "C+"
    elif mark >= 40:
        return "C"
    else:
        return "G"

scores = []
a_count = 0

print("--- CUSTOM SPM REPORT CARD GENERATOR ---")
print("Type each subject you take (or type 'done' when finished):\n")

while True:
    subject = input("Subject name (or 'done'): ")
    
    if subject.lower() == "done":
        break
        
    mark = int(input(f"Enter mark for {subject} (0-100): "))
    grade = get_spm_grade(mark)
    scores.append(mark)
    
    if grade in ["A+", "A", "A-"]:
        a_count += 1
        
    print(f"  -> {subject}: {mark}% ({grade})\n")

if len(scores) > 0:
    average = sum(scores) / len(scores)
    print("--- FINAL SUMMARY ---")
    print(f"Total Subjects: {len(scores)}")
    print(f"Total A's Scored: {a_count} out of {len(scores)}")
    print(f"Overall Average: {average:.1f}%")
else:
    print("No subjects entered!")