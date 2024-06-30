# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPE_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPE_CREDS)
SHEET = GSPREAD_CLIENT.open('Stress-Scale-2 (PP3)')

stress_questions = SHEET.worksheet('Stress')

print("ARE YOU SO STRESSED?")
print("This is just to know the level of stress you have been in.\n")
print("Choose the number 0, 1, 2, 3 or 4 as your answer to each of the ten questions.")
print("0 = never, 1 = almost never, 2 = sometimes, 3 = fairly often, 4 = very often \n")

def question():
    for query in stress_questions.range('A1:A2'):
        print(query.value + "\n")
        
def answer():    
    user_answer = input(f"Your Answer: ")
    print(user_answer)
    
    
question()
answer()
    
    