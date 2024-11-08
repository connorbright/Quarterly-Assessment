import sqlite3

# Create a connection to the SQLite database (this will create the database file if it doesn't exist)
conn = sqlite3.connect('mcq_questions.db')
cursor = conn.cursor()

# Create the FIN3210 table to store the questions and answers
cursor.execute('''
CREATE TABLE IF NOT EXISTS FIN3210 (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    question TEXT NOT NULL,
    option_a TEXT NOT NULL,
    option_b TEXT NOT NULL,
    option_c TEXT NOT NULL,
    option_d TEXT NOT NULL,
    correct_answer TEXT NOT NULL
);
''')

# List of questions and answers (question, options, correct answer)
questions_and_answers = [
    ("What is the primary goal of financial management?", 
     "Maximize shareholder wealth", "Minimize debt", "Maximize sales", "Maximize profit", "A"),
    
    ("Which of the following is NOT a current asset?", 
     "Accounts receivable", "Inventory", "Cash", "Equipment", "D"),
    
    ("What does the time value of money concept state?", 
     "Money today is worth more than the same amount in the future", "Money in the future is worth more than the same amount today", 
     "Money is only valuable when it is invested", "Time has no impact on the value of money", "A"),
    
    ("Which financial statement shows the company’s profitability over a specific period?", 
     "Balance sheet", "Income statement", "Cash flow statement", "Owner’s equity statement", "B"),
    
    ("What is the formula for calculating the future value of an investment?", 
     "FV = PV / (1 + r)^n", "FV = PV * (1 + r)^n", "FV = PV * r^n", "FV = PV + r * n", "B"),
    
    ("The net present value (NPV) method is used to evaluate investments. A positive NPV means:", 
     "The project is expected to create value for the company", "The project will break even", "The project will result in a loss", "The project is financially neutral", "A"),
    
    ("What is the key difference between debt and equity financing?", 
     "Debt financing requires repayment, while equity financing does not", "Equity financing is risk-free, while debt financing is risky", 
     "Debt financing provides ownership in the company, while equity financing does not", "There is no difference", "A"),
    
    ("Which of the following is a characteristic of a bond?", 
     "It represents ownership in the company", "It is a short-term liability", "It provides fixed interest payments", "It is a form of equity", "C"),
    
    ("The cost of equity can be calculated using the:", 
     "Capital asset pricing model (CAPM)", "Dividend discount model (DDM)", "Weighted average cost of capital (WACC)", "Net present value (NPV)", "A"),
    
    ("What is the purpose of a company’s capital budgeting process?", 
     "To determine how much debt to issue", "To decide which investments or projects to undertake", 
     "To calculate the firm’s tax obligations", "To manage daily operations", "B")
]


# Insert questions and answers into the FIN3210 table
for question in questions_and_answers:
    cursor.execute('''
    INSERT INTO FIN3210 (question, option_a, option_b, option_c, option_d, correct_answer)
    VALUES (?, ?, ?, ?, ?, ?)
    ''', question)

# Commit the transaction to save the changes
conn.commit()

# Retrieve and display the data to verify
cursor.execute('SELECT * FROM FIN3210')
rows = cursor.fetchall()

for row in rows:
    print(f"ID: {row[0]}, Question: {row[1]}, A: {row[2]}, B: {row[3]}, C: {row[4]}, D: {row[5]}, Correct Answer: {row[6]}")

# Close the connection to the database
conn.close()
