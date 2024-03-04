#Finding the name of the table in the database:
import sqlite3

connection = sqlite3.connect('FridayProj5.db')
cursor = connection.cursor()
cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
table_name = cursor.fetchone()[0]
cursor.execute(f"SELECT question, answer FROM QuestAns")
quiz_data = cursor.fetchall()
connection.close()

#Listing the questions and answers in the database:
for question, correct_answer in quiz_data:
    user_answer = input(question + " ")
    if user_answer == correct_answer:
        print("Correct!")
    else:
        print("Incorrect. The answer was", correct_answer)