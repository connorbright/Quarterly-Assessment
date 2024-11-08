import sqlite3

# Step 1: Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('mcq_questions.db')  # This will create a file named 'mcq_questions.db'
cursor = conn.cursor()

# Step 2: Create the DS3850 table to store the questions and answers
cursor.execute('''
CREATE TABLE IF NOT EXISTS DS3850 (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    question TEXT NOT NULL,
    option_a TEXT NOT NULL,
    option_b TEXT NOT NULL,
    option_c TEXT NOT NULL,
    option_d TEXT NOT NULL,
    correct_answer TEXT NOT NULL
)
''')

# Step 3: Insert multiple-choice questions and answers into the DS3850 table
questions = questions = [

    ("Which of the following functions can be used to find the average of a range of cells in Excel?", 
     "SUM()", "AVERAGE()", "COUNT()", "MAX()", "B"),

    ("Which Excel function would you use to count the number of cells containing numbers in a range?", 
     "COUNTA()", "COUNT()", "SUM()", "AVERAGE()", "B"),

    ("What is a Pivot Table used for in Excel?", 
     "To visualize data with charts", 
     "To sort data alphabetically", 
     "To summarize and analyze large sets of data", 
     "To find duplicates in data", 
     "C"),

    ("What type of chart would you typically use to show the relationship between two variables in Excel?", 
     "Pie chart", 
     "Line chart", 
     "Bar chart", 
     "Scatter plot", 
     "D"),

    ("What is the purpose of the `IF` function in Excel?", 
     "To calculate the sum of a range", 
     "To apply conditional formatting", 
     "To perform a conditional test and return a value based on the result", 
     "To create a pivot table", 
     "C"),

    ("Which Excel function returns the current date?", 
     "TODAY()", 
     "NOW()", 
     "DATE()", 
     "CURRENT()", 
     "A"),

    ("What is the purpose of the `CONCATENATE` function in Excel?", 
     "To add numbers together", 
     "To combine multiple text strings into one", 
     "To split text into separate columns", 
     "To count the number of characters in a cell", 
     "B"),

    ("What type of chart would be most appropriate for comparing data across categories, such as sales by region?", 
     "Line chart", 
     "Bar chart", 
     "Pie chart", 
     "Histogram", 
     "B"),

    ("Which Excel function allows you to look up data in a vertical column?", 
     "HLOOKUP()", 
     "VLOOKUP()", 
     "INDEX()", 
     "MATCH()", 
     "B"),

    ("Which chart type would you use to show parts of a whole?", 
     "Line chart", 
     "Bar chart", 
     "Pie chart", 
     "Scatter plot", 
     "C"),
]

# Step 4: Insert data into the DS3850 table
cursor.executemany('''
INSERT INTO DS3850 (question, option_a, option_b, option_c, option_d, correct_answer)
VALUES (?, ?, ?, ?, ?, ?)
''', questions)

# Step 5: Commit changes and close the connection
conn.commit()

# Querying the database to check if everything was inserted
cursor.execute('SELECT * FROM DS3850')
rows = cursor.fetchall()

# Print all questions from the DS3850 table
for row in rows:
    print(f"ID: {row[0]}")
    print(f"Question: {row[1]}")
    print(f"A) {row[2]}")
    print(f"B) {row[3]}")
    print(f"C) {row[4]}")
    print(f"D) {row[5]}")
    print(f"Correct Answer: {row[6]}")
    print()

conn.close()

print("Questions have been successfully saved into the DS3850 table.")
