# raphael clouiee inducil
# BSCpE 1-2 
# 04-07-25
# assignment 10: quiz
# Create the Quiz program that read the output file of the Quiz Creator. The user will answer the randomly selected question and check if the answer is correct.

import random

# user input for file (txt) name of what to read

quiz_file = input("Enter the name of your quiz file (without .txt): ") + ".txt"

# open with read mode 

with open(quiz_file, "r") as file:
    file_lines = file.readlines()

# add new variable to read file line using .readlines
# initialize empty list for questions and lines

quiz_data = []
line_number = 0

# while loop file and collect the questions and multiple choice answers
# grab 6 lines from file (qstn, a, b, c, d, ca)

while line_number < len(file_lines):
    if file_lines[line_number].startswith("Question: "):
        question = file_lines[line_number].strip()
        answer_a = file_lines[line_number + 1].strip()
        answer_b = file_lines[line_number + 2].strip()
        answer_c = file_lines[line_number + 3].strip()
        answer_d = file_lines[line_number + 4].strip()
        correct_answer = file_lines[line_number + 5].strip()

# append to the list of questions and answers

        quiz_data.append([
            question,
            answer_a,
            answer_b,
            answer_c,
            answer_d,
            correct_answer
        ])
        line_number += 7

# shuffle the list of questions and answers

random.shuffle(quiz_data)

# scoring system

score = 0

# display the question and answers to the user

for quiz_item in quiz_data:
    print("\n" + quiz_item[0])
    print(quiz_item[1])
    print(quiz_item[2])
    print(quiz_item[3])
    print(quiz_item[4])

# ask user for input of the answer

    user_answer = input("Your answer (A, B, C, D): ").strip().upper()

# get the correct answer put it in a new variable

    correct_answer = quiz_item[5].split(": ")[1].strip().upper()

# compare using if to user's answer
# if correct, print correct
# else print wrong and show the correct answer

    if user_answer == correct_answer:
        print("Correct!")
        score += 1
    else:
        print("Wrong! The correct answer is: " + correct_answer)

# loop to ask another question

    continue_quiz = input("Do you want to continue? (yes/no): ").strip().lower()
    if continue_quiz != "yes":
        print("Thank you for playing!")
        break

# done

print(f"\nYou got {score} correct out of {len(quiz_data)}.")
