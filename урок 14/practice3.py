students = (
    ("Анна", 20, 4.5),
    ("Валентин", 23, 3.8),
    ("Алексей", 21, 4.9),
    ("Ангелина", 35, 4.7),
    ("Василий", 45, 5.0),
    )
spisikStudentov = students[0][0]
if students[1][0] > spisikStudentov:
    spisikStudentov = students[1][0]
if students[2][0] > spisikStudentov:
    spisikStudentov = students[2][0]
if students[3][0] > spisikStudentov:
    spisikStudentov = students[3][0]
if students[4][0] > spisikStudentov:
    spisikStudentov = students[4][0]
listOfGrades = students[0][2]
if students[1][2] > listOfGrades:
    spisikStudentov = students[1][2]
if students[2][2] > listOfGrades:
    spisikStudentov = students[2][2]
if students[3][2] > listOfGrades:
    spisikStudentov = students[3][2]
if students[4][2] > listOfGrades:
    spisikStudentov = students[4][2]
listOfAges = students[0][1]
if students[1][1] > listOfAges:
    spisikStudentov = students[1][1]
if students[2][1] > listOfAges:
    spisikStudentov = students[2][1]
if students[3][1] > listOfAges:
    spisikStudentov = students[3][1]
if students[4][1] > listOfAges:
    spisikStudentov = students[4][1]

print(f"список по возврасту(по возврастанию): {listOfAges}")
print(f"список по оценке: {listOfGrades}")
print(f"список по имени(по алфавиту): {spisikStudentov}")