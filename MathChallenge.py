"""
A math challenge game where the user tries to complete 10 math problems under a certain amount of time.
"""

import time
import random

CLEAR = "\033[2J"
RETURN = "\033[H"

operations = {'+':'+',
              '-':'-',
              'x':'*',
              '/':'/',
              '^':'**'}

MIN_NUMBER = 0
MAX_NUMBER = 12

MAX_DIVISION = 144
MAX_EXPONENT = 12

TOTAL_PROBLEMS = 10

def generate_problem():
    """
    Generates one problem. Returns the problem and its answer
    """
    operation = random.choice(list(operations))
    if operation == '^':
        base = random.randint(MIN_NUMBER,MAX_NUMBER)
        problem = f"{str(base)} ^ 2"
        answer = eval(f"{str(base)}**2")
    elif operation == '/':
        dividend = 3
        divisor = 2
        while dividend % divisor != 0:
            dividend = random.randint(MIN_NUMBER,MAX_DIVISION)
            divisor = random.randint(1,MAX_NUMBER)
        problem = f"{str(dividend)} / {str(divisor)}"
        answer = eval(problem)
    else:
        left = random.randint(MIN_NUMBER,MAX_NUMBER)
        right = random.randint(MIN_NUMBER,MAX_NUMBER)
        problem = f"{str(left)} {operation} {str(right)}"
        answer = eval(f"{str(left)}{operations[operation]}{str(right)}")
    return problem,answer

def challenge():
    """
    Starts one round of 10 problems. Returns the amount of time elapsed as a float and formatted in a string
    """
    print("Ready...")
    time.sleep(2)
    for n in range (3):
        print(3-n)
        time.sleep(1)
    
    start_time = time.time()
    for n in range (TOTAL_PROBLEMS):
        problem_num = n+1
        problem,answer = generate_problem()
        user_answer = ""
        while answer != user_answer:
            print(f"{CLEAR}{RETURN}Problem #{problem_num}")
            try:
                user_answer = int(input(f"{problem} =  ").strip())
            except Exception as e:
                continue
            
    end_time = time.time()
    time_elapsed = round(end_time - start_time,3)
    reformatted_time = f"{int(time_elapsed//60):02d}:{(time_elapsed%60):06.3f}"
    return time_elapsed,reformatted_time

#Start program
formatted_high_score = "00:00.000"
high_score = 999999999
print("How fast can you complete 10 problems? ")
keep_playing = "y"
while keep_playing == "y":
    print(f"Best Time: {formatted_high_score}")
    time_elapsed,reformatted_time = challenge()
    print(f"Time: {reformatted_time}")
    if time_elapsed < high_score:
        high_score = time_elapsed
        formatted_high_score = reformatted_time
        print(f"New Best Time!")
    print(f"Best Time: {formatted_high_score}")

    while True:
        keep_playing = input("Would you like to keep playing? (Y/N) ").lower().strip()
        if keep_playing == "y" or keep_playing == "n":
            break
        else:
            print("That is not an accepted answer. Try again.")

