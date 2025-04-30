# raphael clouiee inducil
# BSCpE 1-2 
# 04-07-25
# assignment 10: quiz
# Create the Quiz program that read the output file of the Quiz Creator. The user will answer the randomly selected question and check if the answer is correct.

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
    if file_lines[line_number}.startswith("Question: ")]
        question = file_lines[line_number].strip()
        answer_a = file_lines[line_number + 1].strip()
        answer_b = file_lines[line_number + 2].strip()
        answer_c = file_lines[line_number + 3].strip()
        answer_d = file_lines[line_number + 4].strip()
        correct_answer = file_lines[line_number + 5].strip()

# append to the list of questions and answers

        quiz_data.append({
            question_line,
            answer_a,
            answer_b,
            answer_c,
            answer_d,
            correct_answer
        })
        line_number += 7

# shuffle the list of questions and answers

random.shuffle(quiz_data)

# display the question and answers to the user
# ask user for input of the answer
# get the correct answer put it in a new variable
# compare using if to user's answer
# if correct, print correct
# else print wrong and show the correct answer
# loop to ask another question
# done