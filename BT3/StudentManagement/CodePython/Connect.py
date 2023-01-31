from sqlite3 import *


# Connect python with Database
connected = connect("StudentManagement.db")

# Create cursor obj
cursor = connected.cursor()

# Create tables
createSubject = """CREATE TABLE IF NOT EXISTS "Subject" (
	"SubjectID"	TEXT,
	"SubjectName"	TEXT,
	"Units"	INTEGER,
	PRIMARY KEY("SubjectID"));
"""
createClass = """CREATE TABLE IF NOT EXISTS "Class" (
	"ClassID"	TEXT,
	"ClassName"	TEXT,
	"ClassYear"	TEXT,
	PRIMARY KEY("ClassID"));
"""
createStudent = """CREATE TABLE IF NOT EXISTS "Student" (
	"StudentID"	TEXT,
	"StudentName"	TEXT,
	"StudentAddress"	TEXT,
	"ClassID"	TEXT,
	PRIMARY KEY("StudentID"),
	FOREIGN KEY("ClassID") REFERENCES "Class"("ClassID"));
"""
createGrade = """CREATE TABLE IF NOT EXISTS "StudentGrades" (
	"StudentID"	TEXT,
	"SubjectID"	TEXT,
	"Grades"	REAL,
	PRIMARY KEY("StudentID","SubjectID"),
	FOREIGN KEY("StudentID") REFERENCES "Student"("StudentID"),
	FOREIGN KEY("SubjectID") REFERENCES "Subject"("SubjectID"));
"""
# cursor.execute(createSubject)
# cursor.execute(createClass)
# cursor.execute(createStudent)
# cursor.execute(createGrade)


# Insert data into table

insertSubject = """INSERT INTO "Subject" ("SubjectID","SubjectName","Units")
 VALUES ('S01','Thiết kế cơ sở dữ liệu',2),
        ('S02','Lập trình hướng đối tượng',3),
        ('S03','Cấu trúc dữ liệu và giải thuật',3),
        ('S04','Lý thuyết đồ thị',2),
        ('S05','Mạng máy tính',3);
"""
InsertClass = """INSERT INTO "Class" ("ClassID","ClassName","ClassYear")
 VALUES ('C01','Computer Science','2020-2024'),
        ('C02','Software Engineering','2020-2024'),
        ('C03','Computer Science','2019-2023');
"""
insertStudent = """INSERT INTO "Student" ("StudentID","StudentName","StudentAddress","ClassID")
 VALUES  ('T01','Phạm Huy Hoàng','25 Nguyễn Đình Chiều','C01'),
        ('T02','Đậu Văn Đạt','133 Nguyễn Thị Minh Khai','C02'),
        ('T03','Trương Hà Vũ Huy','69 Mai Thị Lựu','C01'),
        ('T04','Nguyễn Quốc Đạt','5 Nguyễn Bỉnh Khiêm','C03'),
        ('T05','Nguyễn Hổ','445 Điện Biên Phủ','C02'),
        ('T06','Nguyễn Long Nhật','256 Xô Viết Nghệ Tĩnh','C03'),
        ('T07','Nguyễn Văn Lâm','350 Bạch Đằng','C01'),
        ('T08','Nguyễn Ngọc Thiện','1001 Phạm Thế Hiển','C01'),
        ('T09','Lê Trường Thọ','985 Huỳnh Phúc Tấn','C01'),
        ('T10','Bùi Quốc Hào','150 Võ Văn Tần','C02'),
        ('T11','Trần Nhật Huy','555 Cách Mạng Tháng 8','C02'),
        ('T12','Từ Thị Cẩm Nhung','123 Võ Thị Sáu','C03'),
        ('T13','Phạm Nguyễn Duy Khánh','23 Pasteur','C01'),
        ('T14','Nguyễn Huy Bảo','2 Phan Văn Trị','C01'),
        ('T15','Nguyễn Võ Đình Anh','66 Võ Văn Ngân','C01'),
        ('T16','Trần Thành An','50 Lê Văn Việt','C03'),
        ('T17','Lê Hồng Đức','169 Đinh Tiên Hoàng','C03'),
        ('T18','Trần Hữu Ân','50 Nguyễn Hữu Cảnh','C02'),
        ('T19','Nguyễn Hùng Anh','15 Mai Chí Thọ','C03'),
        ('T20','Nguyễn Hoàng An','110 Nguyễn Văn Linh','C01');
"""
insertGrade = """INSERT INTO "StudentGrades" ("StudentID","SubjectID","Grades")
 VALUES  ('T01','S01',6.5),
        ('T01','S02',7.5),
        ('T01','S03',4.0),
        ('T02','S02',5.0),
        ('T02','S04',6.0),
        ('T03','S01',7.5),
        ('T03','S02',9.0),
        ('T03','S05',10.0),
        ('T04','S03',8.5),
        ('T04','S04',6.5),
        ('T05','S01',4.0),
        ('T05','S02',5.0),
        ('T05','S04',9.0),
        ('T06','S01',7.0),
        ('T06','S02',8.0),
        ('T07','S01',1.0),
        ('T07','S03',3.0),
        ('T07','S04',3.5),
        ('T08','S01',2.0),
        ('T08','S05',6.0),
        ('T09','S02',7.5),
        ('T09','S01',8.0),
        ('T09','S03',9.5),
        ('T10','S04',10.0),
        ('T10','S01',10.0);
"""
# cursor.execute(insertSubject)
# cursor.execute(InsertClass)
# cursor.execute(insertStudent)
# cursor.execute(insertGrade)


querySubject = """select * from Subject"""
queryClass = """select * from Class"""
queryStudent = """select * from Student"""
queryStudentGrade = """select * from StudentGrades"""

# Query

queryName = [
    '5.1. Show Students of class ID = "C02"	',
    '5.2. Show Students of class name = "Computer Science"',
    '5.3. Show Students (All information) of class year = "2020-2024"',
    '5.4. Show Subject name and units of the Subject ID = "S01"',
    '5.5. Grades of Subject ID = "S02" of Student ID = "T02"',
    '5.6. Find Subject (ID, Name and Grades) that Student ID = "T02" fail',
    '5.7. Show all the Subject (*) that Student ID = "T03" never took the exam',
    "5.8. Number of Students for each class",
    "5.9. Find the classes with the largest number of students",
    '5.10. GPA (grade point average) of student ID = "T02"',
]

query1 = '''SELECT *
FROM Student
WHERE ClassID="C02"'''
query2 = """SELECT StudentID,StudentName,StudentAddress,s.ClassID,ClassName,ClassYear
FROM Student s
JOIN Class c ON (s.ClassID=c.ClassID)
WHERE c.ClassName='Computer Science'"""
query3 = """SELECT StudentID,StudentName,StudentAddress,s.ClassID,ClassName,ClassYear
FROM Student s
JOIN Class c ON (s.ClassID=c.ClassID)
WHERE c.ClassYear='2020-2024'"""
query4 = """SELECT SubjectName,Units
FROM Subject
WHERE SubjectID='S01'"""
query5 = """SELECT *
FROM StudentGrades
WHERE SubjectID='S02' AND StudentID='T02'"""
query6 = """SELECT sg.SubjectID,s.SubjectName,sg.Grades
FROM StudentGrades sg
JOIN Subject s ON (sg.SubjectID=s.SubjectID)
WHERE sg.Grades<5 AND sg.StudentID='T02'"""
query7 = """SELECT DISTINCT *
FROM Subject 
WHERE SubjectID NOT IN
(
	SELECT SubjectID
	FROM StudentGrades
	WHERE StudentID='T02'
)"""
query8 = """SELECT ClassID,COUNT(StudentID) AS 'Number of students'
FROM Student
GROUP BY ClassID"""
query9 = """SELECT *
FROM (
	SELECT ClassID,COUNT(StudentID),dense_rank() over (order by COUNT(StudentID) desc) as ss
	FROM Student
	GROUP BY ClassID)
WHERE ss=1"""
query10 = """SELECT StudentID, AVG(Grades)
FROM StudentGrades
WHERE StudentID='T02'
GROUP BY StudentID"""


columnName = []
dataList = []

# get name column and data


def executeQuery(cursor, query):
    dataList = []
    cursor.execute(query)
    dataList = cursor.fetchall()
    return dataList


def getData(cursor, query):
    columnName = []
    data = cursor.execute(query)
    for column in data.description:
        columnName.append(column[0])
    return columnName



connected.commit()
