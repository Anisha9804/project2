import pandas as pd
from sqlalchemy import create_engine
from urllib.parse import quote_plus
def all_files():
        attendance=pd.read_csv("attendance.csv")
        course=pd.read_csv("courses.csv")
        marks=pd.read_csv("marks.csv")
        payments=pd.read_csv("payments.csv")
        students=pd.read_csv("students.csv")
        trainers=pd.read_csv("trainers.csv")

        print(all_files)
        
        return attendance, course, marks, payments, students, trainers 
attendance, course, marks, payments, students, trainers = all_files()

print(attendance.shape)
print(course.shape)
print(marks.shape)
print(payments.shape)
print(students.shape)
print(trainers.shape)

print(attendance.columns)
print(course.columns)
print(marks.columns)
print(payments.columns)
print(students.columns)
print(trainers.columns)

print(attendance.isnull().sum())
print(course.isnull().sum())
print(marks.isnull().sum())
print(payments.isnull().sum())
print(students.isnull().sum())
print(trainers.isnull().sum())

print(attendance.duplicated().sum())
print(course.duplicated().sum())
print(marks.duplicated().sum())
print(payments.duplicated().sum())
print(students.duplicated().sum())
print(trainers.duplicated().sum())

merger = pd.merge(students, course, on="course_id", how="inner")
print(merger)

marks["average_marks"] = marks[["python_marks", "sql_marks", "powerbi_marks", "numpy_marks", "pandas_marks"]].mean(axis=1)
print(marks)

sorted_df = marks.sort_values(by="average_marks", ascending=False)
print(sorted_df)

result = marks[marks["average_marks"] > 80]
print(result)

attendance["total_persentage"] = (attendance["attended_classes"] / attendance["total_classes"]) * 100
print(attendance)

attendance["attendence_ststus"] = attendance["total_persentage"].apply(lambda x: "good" if x >= 75 else "low")
print(attendance)

marks["perfomance"] = marks["average_marks"].apply(lambda x: "Excellent" if x >= 85 else ("good" if x >= 70 else "Needs Improvement"))
print(marks[["student_id", "average_marks", "perfomance"]])

max_marks = marks[["python_marks", "sql_marks", "powerbi_marks", "numpy_marks", "pandas_marks"]].max()
min_marks = marks[["python_marks", "sql_marks", "powerbi_marks", "numpy_marks", "pandas_marks"]].min()
print(max_marks)
print(min_marks)




# attendance = pd.read_csv("attendance.csv")
# course = pd.read_csv("courses.csv")
# marks = pd.read_csv("marks.csv")
# payments= pd.read_csv("payments.csv")
# students = pd.read_csv("students.csv")
# trainers= pd.read_csv("trainers.csv")

password=quote_plus("Anisha9804")


engine = create_engine(
    f"mysql+pymysql://root:{password}@localhost:3306/project"
)

attendance.to_sql(
    name="attendance",
    con=engine,
    if_exists="replace",
    index=False
)
course.to_sql(
    name="courses",
    con=engine,
    if_exists="replace",
    index=False
)
marks.to_sql(
    name="marks",
    con=engine,
    if_exists="replace",
    index=False
)   
payments.to_sql(
    name="payments",
    con=engine,
    if_exists="replace",
    index=False
)
students.to_sql(
    name="students",
    con=engine,
    if_exists="replace",
    index=False
)
trainers.to_sql(
    name="trainers",
    con=engine,
    if_exists="replace",
    index=False
)
