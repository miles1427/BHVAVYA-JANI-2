def personality_test():
    print("Welcome to the Personality Test!")
    print("Choose one option (a, b, c, or d) for each question.\n")

    score = {
        "introvert": 0,
        "extrovert": 0,
        "thinker": 0,
        "feeler": 0
    }

    questions = [
        {
            "question": "1. What do you prefer doing on a weekend?",
            "options": {
                "a": ("Reading a book at home", "introvert"),
                "b": ("Going to a party", "extrovert"),
                "c": ("Solving puzzles", "thinker"),
                "d": ("Volunteering or helping someone", "feeler")
            }
        },
        {
            "question": "2. How do you make decisions?",
            "options": {
                "a": ("Based on logic and analysis", "thinker"),
                "b": ("Based on emotions and values", "feeler"),
                "c": ("Whatever feels less stressful", "introvert"),
                "d": ("Whatever sounds most exciting", "extrovert")
            }
        },
        {
            "question": "3. You’re in a new group. What do you do?",
            "options": {
                "a": ("Observe and wait for others to approach", "introvert"),
                "b": ("Start conversations right away", "extrovert"),
                "c": ("Analyze the group before joining in", "thinker"),
                "d": ("Make sure everyone feels comfortable", "feeler")
            }
        }
    ]

    for q in questions:
        print(q["question"])
        for key, value in q["options"].items():
            print(f"  {key}) {value[0]}")
        answer = input("Your answer: ").lower()
        while answer not in q["options"]:
            answer = input("Invalid input. Please choose a, b, c, or d: ").lower()
        personality_type = q["options"][answer][1]
        score[personality_type] += 1
        print()

    print("Calculating your personality...\n")

    max_type = max(score, key=score.get)
    print(f"Your dominant personality type is: {max_type.upper()}")
    
    # Optional: You can give a little explanation too
    descriptions = {
        "introvert": "You enjoy your own company and recharge in calm environments.",
        "extrovert": "You're energized by social interactions and outgoing settings.",
        "thinker": "You rely on logic and objectivity to make decisions.",
        "feeler": "You are guided by empathy and emotional understanding."
    }
    print(descriptions[max_type])


# Run the test
personality_test()
