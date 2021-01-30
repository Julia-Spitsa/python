lessons = {}
with open('file6.txt', 'r', encoding="utf-8") as f:
    for line in f:
        lesson, lec, pr, lab = line.split(' ')
        hours = int(lec)+int(pr)+int(lab)
        print(lesson, hours)
        lessons.update({lesson: hours})
print(lessons)
