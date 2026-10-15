import pandas as pd
import numpy as np

subjects = ["Maths", "Science", "English", "Computer"]

def calculate_total(marks):
    return np.sum(marks)

def calculate_average(marks):
    return round(np.mean(marks), 2)

def assign_grade(average):
    # Grading rule based on average marks
    if average >= 90:
        return "A+"
    elif average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    else:
        return "F"

def check_result(marks):
    # Pass rule: at least 35 in every subject
    return "Pass" if np.min(marks) >= 35 else "Fail"

def process_data(df):
    totals, averages, grades, results = [], [], [], []
    for index, row in df.iterrows():
        marks = row[subjects].values.astype(int)
        avg = calculate_average(marks)
        totals.append(calculate_total(marks))
        averages.append(avg)
        grades.append(assign_grade(avg))
        results.append(check_result(marks))
    df["Total"] = totals
    df["Average"] = averages
    df["Grade"] = grades
    df["Result"] = results
    return df

def show_analysis(df):
    print("\n===== STUDENT PERFORMANCE ANALYSIS =====\n")
    top = df.loc[df["Average"].idxmax()]
    low = df.loc[df["Average"].idxmin()]
    print("Highest average:", top["Name"], "-", top["Average"])
    print("Lowest average :", low["Name"], "-", low["Average"])
    print("Class average  :", round(np.mean(df["Average"]), 2))
    print("\nPassed:", (df["Result"] == "Pass").sum())
    print("Failed:", (df["Result"] == "Fail").sum())
    print("\nSubject-wise average:")
    subject_avg = df[subjects].mean().round(2)
    print(subject_avg)
    print("Best subject   :", subject_avg.idxmax())
    print("Weakest subject:", subject_avg.idxmin())
    print("\nGrade distribution:")
    print(df["Grade"].value_counts())
    print("\nTop 3 students:")
    print(df.sort_values("Average", ascending=False)[["Name", "Department", "Average", "Grade"]].head(3))

def main():
    df = pd.read_csv("students.csv")
    print("Number of records:", df.shape[0])
    print("Columns:", list(df.columns))
    df = process_data(df)
    print("\n", df[["Student_ID", "Name", "Total", "Average", "Grade", "Result"]])
    show_analysis(df)

if __name__ == "__main__":
    main()
