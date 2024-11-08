import sqlite3

# Create a connection to the SQLite database (this will create the database file if it doesn't exist)
conn = sqlite3.connect('mcq_questions.db')
cursor = conn.cursor()

# Create the BMGT4410 table to store the questions and answers
cursor.execute('''
CREATE TABLE IF NOT EXISTS BMGT4410 (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    question TEXT NOT NULL,
    option_a TEXT NOT NULL,
    option_b TEXT NOT NULL,
    option_c TEXT NOT NULL,
    option_d TEXT NOT NULL,
    correct_answer TEXT NOT NULL
);
''')

# List of 10 questions and answers for the BMGT4410 Business Management course (question, options, correct answer)
questions = [
    ("What is the primary goal of conflict management?", 
     "To eliminate all conflict in an organization", "To resolve the conflict in a way that benefits both parties", 
     "To avoid conflict at all costs", "To punish the party causing the conflict", "B"),
    
    ("Which of the following is a common style of conflict resolution?", 
     "Competing", "Avoiding", "Collaborating", "All of the above", "D"),
    
    ("In negotiation, which strategy involves finding a solution that meets the needs of both parties?", 
     "Win-lose", "Competing", "Integrative negotiation", "Distributive negotiation", "C"),
    
    ("Which of the following best describes the principle of ‘BATNA’ in negotiation?", 
     "Best Alternative to a Negotiated Agreement", "Better Agreement Than Negotiated Agreement", 
     "Best Attitude Toward New Agreements", "Basic Agreement to Negotiate Always", "A"),
    
    ("Which conflict resolution strategy involves ignoring the conflict and hoping it will go away?", 
     "Accommodation", "Compromise", "Avoidance", "Collaboration", "C"),
    
    ("What is the ‘ZOPA’ in negotiation?", 
     "Zone of Potential Agreement", "Zero Opportunity for Agreement", "Zone of Preferred Agreement", 
     "Zero Offer of Potential Agreement", "A"),
    
    ("Which type of negotiation is focused on dividing a fixed amount of resources?", 
     "Integrative negotiation", "Distributive negotiation", "Principled negotiation", "Collaborative negotiation", "B"),
    
    ("Which of the following is a characteristic of a win-win negotiation outcome?", 
     "One party benefits while the other loses", "Both parties feel that they gained value from the negotiation", 
     "One party compromises heavily", "One party dominates the negotiation", "B"),
    
    ("Which of the following is NOT a key principle of principled negotiation?", 
     "Separate the people from the problem", "Focus on positions, not interests", 
     "Generate options for mutual gain", "Use objective criteria", "B"),
    
    ("What is the role of active listening in conflict resolution?", 
     "To ensure that the speaker's message is correctly understood", "To immediately respond with your point of view", 
     "To dominate the conversation", "To minimize the other person's concerns", "A")
]


# Insert questions and answers into the BMGT4410 table
for question in questions:
    cursor.execute('''
    INSERT INTO BMGT4410 (question, option_a, option_b, option_c, option_d, correct_answer)
    VALUES (?, ?, ?, ?, ?, ?)
    ''', question)

# Commit the transaction to save the changes
conn.commit()

# Retrieve and display the data to verify
cursor.execute('SELECT * FROM BMGT4410')
rows = cursor.fetchall()

for row in rows:
    print(f"ID: {row[0]}, Question: {row[1]}, A: {row[2]}, B: {row[3]}, C: {row[4]}, D: {row[5]}, Correct Answer: {row[6]}")

# Close the connection to the database
conn.close()
