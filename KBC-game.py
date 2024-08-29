questions = [
    "Q.1: How many continents are there?\na) 5\t\tb) 9\nc) 7\t\td) 3",
    "Q.2: What is the current population?\na) 8-billion\t\tb) 4-billion\nc) 7-billion\t\td) 10-billion",
    "Q.3: What was the last dangerious pandamic?\na) Covid-19\t\tb) HIV/AIDS Pandemic\nc) Spanish Flu\t\td) The Black Death",
    "Q.4: Who is powerfull country in world?\na) China\t\tb) United States\nc) European Union\t\td) Russia",
    "Q.5: What is the most powerfull man-made weapon?\na) Tsar Bomba\t\tb) ICBMs\nc) B83 Nuclear Bomb\t\td) MOAB"
]

Correct_answer = ["c", "a", "b", "b", "a"]

points = 0
correct_answered = 0

for i, correct in zip(questions, Correct_answer):
    print(i)
    
    ans = input("Enter correct option (a, b, c or d): ")
    
    if ans == correct:
        print("Correct")
        points = points + 100
        correct_answered += 1
    if ans != correct:
        print("Wrong")
        points = points - 50
        
        
print(f"\nCorrect answered question are {correct_answered}/{len(questions)}")
print(f"points = {correct_answered * 100}")
print(f"Minus wrong answer points (-50/question): {(len(questions) - correct_answered) * 50}")
print(f"Total Points = {points}")
