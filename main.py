import json
from datetime import datetime

# Study tips
study_tips = [
    "Study for 25 minutes and take a 5-minute break.",
    "Revise your notes daily.",
    "Practice previous question papers.",
    "Create a study schedule and follow it.",
    "Avoid distractions while studying."
]

# Motivation quotes
motivation_quotes = [
    "Success is the sum of small efforts repeated daily.",
    "Believe in yourself and all that you are.",
    "Dream big and work hard.",
    "Every day is a new opportunity to learn.",
    "Consistency beats talent when talent doesn't work hard."
]

# Get user name
name = input("Enter your name: ")

print(f"\nHello, {name}! Welcome to Smart Student Assistant")

while True:
    print("\n===== SMART STUDENT ASSISTANT =====")
    print("1. Generate Study Tip")
    print("2. Generate Motivation Quote")
    print("3. Display Current Date & Time")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    result = ""

    if choice == "1":
        tip = study_tips[0]
        print("\nStudy Tip:")
        print(tip)
        result = f"Study Tip: {tip}"

    elif choice == "2":
        quote = motivation_quotes[0]
        print("\nMotivation Quote:")
        print(quote)
        result = f"Motivation Quote: {quote}"

    elif choice == "3":
        current_time = datetime.now()
        formatted_time = current_time.strftime("%d-%m-%Y %H:%M:%S")
        print("\nCurrent Date & Time:")
        print(formatted_time)
        result = f"Current Date & Time: {formatted_time}"

    elif choice == "4":
        print("\nThank you for using Smart Student Assistant!")
        break

    else:
        print("\nInvalid Choice! Please try again.")
        continue

    # Save output to file
    with open("output.txt", "a") as file:
        file.write(result + "\n")