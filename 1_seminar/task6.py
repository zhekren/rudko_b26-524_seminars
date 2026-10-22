f = open(r'/Users/jokovich/Desktop/Python_basics/1_seminar/123.txt')
def func(text_file):
     grades = []
     for i in text_file:
          line = i.rstrip('\n').split(';')
          line[1] = int(line[1])
          grades.append([line[1], line[0]])

     max_grade = max(grades)
     min_grade = min(grades)[0]

     for i in range(len(grades)):
          grades[i] = grades[i][0]
     middle_grade = sum(grades)/len(grades)

     counter_upper60 = 0
     for i in range(len(grades)):
          if grades[i] >= 60:
               counter_upper60 += 1

     return max_grade, min_grade, middle_grade, counter_upper60

print(func(open(r'/Users/jokovich/Desktop/Python_basics/1_seminar/123.txt')))