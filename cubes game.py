from random import randint
'''
נקבל כקלט כמה כסף יש לנו לשחק
עלות משחק 3 ש"ח
אם יש עודף נחזיר אותו ללקוח

בכל תור נגריל שתי קוביות:
אם הן זהות, זכינו ב-100 ש"ח
אם הן זהות ושוות ל-6, ז\כינו ב1000 ש"ח
אם הן לא זהות אבל קוביה 2 שווה ל-2, זכינו ב40 ש"ח
אם הן לא זהות אבל קוביה 1 שווה ל-1 זכונו ב-20 ש"ח
לבסוף נדפיס למסך כמה כסף זכינו
'''

money = int(input("Please provide the amount of money you want to play: "))
extra = money%3
print("\nyou have extra of " + str(extra) + " NIS\n")
money = money - extra
summary = 0

for i in range(money//3):
    cube1 = randint(1,6)
    cube2 = randint(1,6)
    print("round number " + str(i+1))
    print("\ncube1 is " + str(cube1))
    print("cube2 is " + str(cube2) + "\n--------------------------------\n")
    if cube1 == cube2 and cube1 == 6:
        summary += 1000
    elif cube1 == cube2 and cube1 != 6:
        summary += 100
    elif cube1 != cube2 and cube2 == 2:
        summary += 40
    elif cube1 != cube2 and cube1 == 1:
        summary += 20
    else:
        continue
print("\nyou won " + str(summary) + " NIS!")


