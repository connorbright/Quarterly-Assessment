import sqlite3

# Create a connection to the SQLite database (this will create the database file if it doesn't exist)
conn = sqlite3.connect('mcq_questions.db')
cursor = conn.cursor()

# Create the DS4220 table to store the questions and answers
cursor.execute('''
CREATE TABLE IF NOT EXISTS DS4220 (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    question TEXT NOT NULL,
    option_a TEXT NOT NULL,
    option_b TEXT NOT NULL,
    option_c TEXT NOT NULL,
    option_d TEXT NOT NULL,
    correct_answer TEXT NOT NULL
);
''')

# List of 10 questions and answers (question, options, correct answer)
questions = [
    ("What is the primary goal of business analytics?", 
     "To generate reports for business managers", "To make data-driven decisions", "To collect data from various sources", "To monitor business performance", "B"),
    
    ("Which of the following best describes a ‘descriptive analysis’?", 
     "Forecasting future trends", "Making predictions about the future", "Summarizing historical data", "Determining the cause of business problems", "C"),
    
    ("In business analytics, what is the purpose of data visualization?", 
     "To manipulate data", "To store data in databases", "To present data in an understandable way", "To filter out noisy data", "C"),
    
    ("Which of the following is NOT a type of data?", 
     "Qualitative data", "Quantitative data", "Logarithmic data", "Discrete data", "C"),
    
    ("What does the term ‘big data’ refer to?", 
     "A large collection of unstructured data", "Data that can be processed by a computer", "Data that is analyzed in real-time", "Data sets that require complex analysis techniques", "D"),
    
    ("Which of the following statistical measures is used to describe the average of a dataset?", 
     "Median", "Mode", "Mean", "Variance", "C"),
    
    ("Which of the following is an example of a predictive analytics technique?", 
     "Descriptive statistics", "Regression analysis", "Data cleaning", "Data visualization", "B"),
    
    ("Which of the following methods is used to make decisions based on the analysis of past business data?", 
     "Data mining", "Forecasting", "Descriptive analytics", "Prescriptive analytics", "C"),
    
    ("What is a common purpose of a regression analysis in business analytics?", 
     "To analyze the relationship between variables", "To identify patterns in customer behavior", 
     "To group data into categories", "To perform time-series forecasting", "A"),
    
    ("In a decision tree, what does each 'node' represent?", 
     "A decision made by the business", "A decision point or a split in the data", 
     "A result of a specific action", "A regression model prediction", "B")
]


# Insert questions and answers into the DS4220 table
for question in questions:
    cursor.execute('''
    INSERT INTO DS4220 (question, option_a, option_b, option_c, option_d, correct_answer)
    VALUES (?, ?, ?, ?, ?, ?)
    ''', question)

# Commit the transaction to save the changes
conn.commit()

# Retrieve and display the data to verify
cursor.execute('SELECT * FROM DS4220')
rows = cursor.fetchall()

for row in rows:
    print(f"ID: {row[0]}, Question: {row[1]}, A: {row[2]}, B: {row[3]}, C: {row[4]}, D: {row[5]}, Correct Answer: {row[6]}")

# Close the connection to the database
conn.close()
