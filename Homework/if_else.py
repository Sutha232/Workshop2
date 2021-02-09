# จงเขียนโปรแกรมเพื่อทำการคำนวณเกรดโดยมีเงื่อนไขดังนี้

# คะแนน 80 - 100 ได้ A
# คะแนน 75 - 79 ได้ B+
# คะแนน 70 - 74 ได้ B
# คะแนน 65 - 69 ได้ C+
# คะแนน 60 - 64 ได้ C
# คะแนน 55 - 59 ได้ D+
# คะแนน 50 - 54 ได้ D
# คะแนน 0 - 49 ได้ F

# และให้แสดงผลตามตัวอย่างด้านล่าง

# Enter your score: 49
# grade:  F
x = int(input("Enter Your score : "))
if (x >= 80) and (x < 100):
    print(
        "Your score is :",
        x,
    )
    print("Grade: A")
elif (x >= 75) and (x <= 79):
    print(
        "Your score is :",
        x,
    )
    print("Grade: B+")
elif (x >= 70) and (x <= 74):
    print(
        "Your score is :",
        x,
    )
    print("Grade: B")
elif (x >= 65) and (x <= 69):
    print(
        "Your score is :",
        x,
    )
    print("Grade: C+")
elif (x >= 60) and (x <= 64):
    print(
        "Your score is :",
        x,
    )
    print("Grade: C")
elif (x >= 55) and (x <= 59):
    print(
        "Your score is :",
        x,
    )
    print("Grade: D+")
elif (x >= 50) and (x <= 54):
    print(
        "Your score is :",
        x,
    )
    print("Grade: D")
else:
    print(
        "Your score is :",
        x,
    )
    print("Grade: F")