# cli quiz app 

questions = [
    "1) What does ip in ip address stand for?",
    "2) Which company developed the java programming language originally?",
    "3) What type of memory is volatile?",
    "4) Which shortcut is commonly used to copy text on windows?",
    "5) In binary, what is 1010 equal to in decimal?"
]

options = [
    ["a) Internet protocol", "b) Internal process", "c) Instant program", "d) Integrated package"],
    ["a) Microsoft", "b) Oracle", "c) Sun Microsystems", "d) IBM"],
    ["a) ROM", "b) RAM", "c) Hard disk", "d) SSD"],
    ["a) ctrl + v", "b) ctrl + x", "c) ctrl + c", "d) ctrl + z"],
    ["a) 8", "b) 10", "c) 12", "d) 15"]
]

answers = ["a", "c", "b", "c", "b"]

score = 0
points = 10 

# quiz loop
for i in range(len(questions)):
    print("\n" + questions[i])
    for opt in options[i]:
        print(opt)
    user_ans = input("your answer: ").lower()
    
    if user_ans == answers[i]:
        print("Correct!")
        score += points
    else:
        print(f"Wrong answer! Correct answer is {answers[i]}")

# final score
print("\nquiz over!")
print(f"your final score: {score}/{len(questions)*points}")

if score == len(questions) * points:
    print("Excellent! Perfect score!")
elif score >= 30:
    print("Good job!")
else:
    print("Keep practicing!")