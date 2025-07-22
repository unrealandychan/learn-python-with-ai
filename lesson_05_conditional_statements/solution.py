
# Lesson 5: Solution

score_str = input("Enter your test score: ")
score = int(score_str)

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"Your grade is: {grade}")

if score < 70:
    print("Keep working hard, you can improve!")
