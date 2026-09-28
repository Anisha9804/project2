import nm as np
from project import all_files

attendance, course, marks, payments, students, trainers = all_files()

attendance["total_persentage"] = (attendance["attended_classes"] / attendance["total_classes"]) * 100
print(attendance)

attendance["attendence_ststus"] = attendance["total_persentage"].apply(lambda x: "good" if x >= 75 else "low")
print(attendance)

marks["average_marks"] = np.mean(
    marks[["python_marks", "sql_marks", "powerbi_marks", "numpy_marks", "pandas_marks"]],
    axis=1
)
print(marks)

max_marks = np.max(marks[["python_marks", "sql_marks", "powerbi_marks", "numpy_marks", "pandas_marks"]])
min_marks = np.min(marks[["python_marks", "sql_marks", "powerbi_marks", "numpy_marks", "pandas_marks"]])
print(max_marks)
print(min_marks)