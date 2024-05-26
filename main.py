print("Welcome to the quiz game!")
proceed = str(input("Would you like to start the game? Yes or No "))
score = 0

if proceed.lower() != "yes":
    print("That's alright! See you next time!")
    quit()

q1 = input("Question No.1 : Who is the president of USA?")
if q1.lower() == "joe biden":
    print("Correct!")
    score += 1
else:
    print("Incorrect! See you next time!")
    print(f"Your score: {score}/3")

q2 = input("Question No.2 : What is Apple's operating system?")
if q2.lower() == "ios":
    print("Correct!")
    score += 1
else:
    print("Incorrect! See you next time!")
    print(f"Your score: {score}/3")

q2 = input("Question No.3 : What does RAM stand for?")
if q2.lower() == "random access memory":
    print("Correct! You answered all the questions correctly!")
    score += 1
    print(f"Your score: {score}/3")
else:
    print("Incorrect! See you next time!")
    print(f"Your score: {score}/3")

