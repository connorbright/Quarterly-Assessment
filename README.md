# Quarterly-Assessment

MCQ Question Viewer - Python Tkinter Application
This Python application is a Multiple Choice Question (MCQ) viewer that interacts with an SQLite database. The app allows users to select a course, load questions from the database, and answer them through a graphical user interface (GUI) built using Tkinter. It is designed to help users study and practice multiple-choice questions.

Features
Select a course from a dropdown menu.
Display questions one by one with multiple-choice answer options.
Track and provide feedback on whether the selected answer is correct.
Navigate through questions with a submit button that automatically loads the next question.
Reset quiz after all questions are answered.
Works with SQLite database to fetch questions and answers.
Requirements
Before you run this application, ensure that you have the following installed on your system:

Python 3.x (you can download it from python.org)
Tkinter (for GUI): Tkinter comes pre-installed with Python on most systems. If not, it can be installed by running pip install tk.
SQLite3 (also comes pre-installed with Python in most cases).
Setup
Step 1: Clone or Download the Repository
You can either clone the repository using Git or download the project as a ZIP file and extract it.

bash
Copy code
git clone <repository-url>
Step 2: Create the Database
The application assumes that an SQLite database file named mcq_questions.db exists in the same directory as the application.

Ensure that the database is set up with the following structure:

Database file: mcq_questions.db
Tables:
DS4210
DS3850
DS4220
FIN3210
BMGT4410
Each table should have the following columns:
id (integer, primary key)
question (text)
option_a (text)
option_b (text)
option_c (text)
option_d (text)
correct_answer (text)
You can create this database manually using SQLite3 or use any database management tool to populate it with your questions and answers.

Step 3: Install Dependencies
If you don't already have Tkinter installed, you can install it by running:

bash
Copy code
pip install tk
Step 4: Running the Application
Once you have set up the database and installed the necessary dependencies, navigate to the directory where the main.py file is located and run the following command:

bash
Copy code
python main.py
This will open the application window, allowing you to interact with the MCQ questions.

Usage
1. Select a Course:
From the dropdown menu, select a course (table name). The available courses are:

DS4210
DS3850
DS4220
FIN3210
BMGT4410
2. Load Questions:
Click the "Load Questions" button to fetch questions from the selected course's table in the database. The first question will be displayed along with four answer options.

3. Answer the Question:
Select one of the options (A, B, C, or D) to answer the question.
Click the "Submit Answer" button to check if your answer is correct.
The next question will be displayed automatically after submitting an answer.
4. End of Quiz:
Once all the questions have been answered, a message will appear indicating that the quiz is complete.