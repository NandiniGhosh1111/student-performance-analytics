# Student Performance Analytics System

**Student:** Nandini Ghosh

**Course:** EWB Courses - Python with AI

## 1. Objective

The aim of this project is to build a Python system that reads student data and analyses it using NumPy and Pandas. It calculates total and average marks, assigns grades, finds pass and fail students, and shows subject-wise performance and top performers. It helps a teacher understand how the class is performing without calculating everything by hand.

## 2. Technologies Used

- Python 3
- NumPy for numerical calculations
- Pandas for loading and analysing the data
- Google Colab for writing and testing the code
- GitHub for submission

## 3. Dataset Description

The dataset is stored in `students.csv` and contains 15 student records. The columns are Student_ID, Name, Department, Maths, Science, English, Computer and Attendance. Students belong to three departments: CSE, ECE and IT. Marks are out of 100. The Attendance column is stored in the dataset but is not used in the grading calculations.

## 4. Implementation

- **Step 1:** The student data is saved in students.csv and loaded into a Pandas DataFrame using read_csv. The program prints the number of records and the column names.
- **Step 2:** Reusable functions are created for each calculation. calculate_total uses NumPy sum to add the marks of the four subjects. calculate_average uses NumPy mean to find the average, rounded to two decimal places.
- **Step 3:** The function assign_grade gives each student a grade based on the average marks. The grading rule is: 90 and above is A+, 80 to 89 is A, 70 to 79 is B, 60 to 69 is C, 50 to 59 is D, and below 50 is F.
- **Step 4:** The function check_result decides Pass or Fail. A student passes only if they score at least 35 in every subject. If the lowest mark is below 35, the student fails.
- **Step 5:** The function process_data uses a loop to go through each student row. For every student it calculates total, average, grade and result, and adds them as new columns (Total, Average, Grade, Result) in the DataFrame.
- **Step 6:** The function show_analysis finds the highest and lowest average, the class average, the number of students who passed and failed, the subject-wise averages, the best and weakest subject, the grade distribution and the top 3 students.
- **Step 7:** The main function runs all the steps in order, and the program starts from it.

## 5. Key Features

- Loads and organises student data using a Pandas DataFrame
- Uses NumPy for sum, mean and minimum calculations
- Reusable functions: calculate_total, calculate_average, assign_grade, check_result, process_data, show_analysis and main
- Uses a loop to process every student record
- Assigns grades using a clearly defined rule
- Identifies pass and fail students using the minimum 35 marks rule
- Finds the highest, lowest and class average performance
- Gives subject-wise analysis with the best and weakest subject
- Shows the grade distribution
- Lists the top 3 students

## 6. How to Run

1. Install the libraries with: `pip install numpy pandas`
2. Keep main.py and students.csv in the same folder.
3. Run the program with: `python main.py`

## 7. Output

The program prints the number of records and column names, then a table with each student's total, average, grade and result, followed by the analysis. The main results for this dataset are:

- Highest average: Divya Menon with 95.25
- Lowest average: Arjun Patel with 34.25
- Class average: 69.23
- Passed: 13 students
- Failed: 2 students (Karthik Iyer and Arjun Patel)
- Subject-wise average: Maths 66.67, Science 67.67, English 71.27, Computer 71.33
- Best subject: Computer
- Weakest subject: Maths
- Grade distribution: A+ 2 students, A 3 students, B 4 students, C 1 student, D 3 students, F 2 students
- Top 3 students: Divya Menon (95.25, A+), Sneha Reddy (92.5, A+) and Aarav Sharma (88.5, A)

## 8. Final Outcome

The project successfully analyses the performance of 15 students. It calculates total and average marks, assigns grades, identifies pass and fail students, and gives subject-wise analysis and the list of top performers. The results are shown clearly in the output without needing to read the code.

## 9. Challenges and Learning

- **Challenge:** Student_ID and Attendance are also numeric columns, so calculating on the whole row would give wrong totals.
  **Solution:** I created a subjects list with only the four subject columns and used it to select the marks for each student.
- **Challenge:** The marks taken from each row were not in a clean numeric format for NumPy.
  **Solution:** I converted them to a NumPy integer array using values.astype(int) before using sum, mean and min.
- **Challenge:** Deciding the pass condition, because a student with a good average can still fail one subject.
  **Solution:** I used np.min on the marks so a student passes only if every subject is at least 35.
- **Challenge:** The code was first written in separate cells in Google Colab.
  **Solution:** I moved everything into functions and saved it as main.py using %%writefile so it runs as one program.
- **Learning:** I learned how to use Pandas and NumPy together, write reusable functions, use loops and conditions for processing data, and organise and publish a project on GitHub.

## 10. GitHub Repository

https://github.com/NandiniGhosh1111/student-performance-analytics


