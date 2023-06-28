from college import College
from student import Student


mivchar = College('Mivchar')
moshe = Student('Moshe', '0543332221', 'Moshe@gmail.com')
yosi = Student('Yosi', '0543332222', 'Yosi@gmail.com')
mivchar.student_manager.add(moshe)

print(mivchar.student_manager.get(moshe))
print('hi')