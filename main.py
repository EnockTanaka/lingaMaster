import random

class LinguaMasterGame:
    def _init_(self):
        self.levels = ["beginner", "intermediate", "advanced"]
        self.texts = {
            "beginner": ["Text 1", "Text 2", "Text 3"],
            "intermediate": ["Text 4", "Text 5", "Text 6"],
            "advanced": ["Text 7", "Text 8", "Text 9"]
        }

    def start_game(self):
        print("Welcome to LinguaMaster! Let's begin.")
        self.select_level()

    def select_level(self):
        print("Choose your level:")
        for i, level in enumerate(self.levels):
            print(f"{i+1}. {level.capitalize()}")
        choice = input("Enter the level number: ")
        level = self.levels[int(choice) - 1]
        self.play_level(level)

    def play_level(self, level):
        print(f"\nStarting {level.capitalize()} level...")
        texts = self.texts[level]
        random.shuffle(texts)
        for text in texts:
            self.analyze_text(text, level)

    def analyze_text(self, text, level):
        print(f"\nAnalyzing text: {text}")
        if level == "beginner":
            self.beginner_activity(text)
        elif level == "intermediate":
            self.intermediate_activity(text)
        elif level == "advanced":
            self.advanced_activity(text)

    def beginner_activity(self, text):
        # Beginner-level activity logic
        print(f"Beginner activity for text: {text}")
        # Example activity: Fill in the blanks
        # You can replace this with your specific beginner-level activity
        blanks = ["_1", "2", "3_"]
        answers = ["answer1", "answer2", "answer3"]
        for blank, answer in zip(blanks, answers):
            user_input = input(f"Fill in {blank}: ")
            if user_input.lower() != answer:
                print("Incorrect answer. Try again!")
                user_input = input(f"Fill in {blank}: ")
                if user_input.lower() != answer:
                    print("Incorrect answer. Moving to the next text.")
                    return
        print("Congratulations! You completed the beginner activity.")

    def intermediate_activity(self, text):
        # Intermediate-level activity logic
        print(f"Intermediate activity for text: {text}")
        # Example activity: Identify rhetorical devices
        # You can replace this with your specific intermediate-level activity
        devices = ["simile", "metaphor", "personification"]
        correct_answers = ["simile", "metaphor", "personification"]
        for device, answer in zip(devices, correct_answers):
            user_input = input(f"Identify a rhetorical device in the text: {device.capitalize()}: ")
            if user_input.lower() != answer:
                print("Incorrect answer. Try again!")
                user_input = input(f"Identify a rhetorical device in the text: {device.capitalize()}: ")
                if user_input.lower() != answer:
                    print("Incorrect answer. Moving to the next text.")
                    return
        print("Congratulations! You completed the intermediate activity.")

    def advanced_activity(self, text):
        # Advanced-level activity logic
        print(f"Advanced activity for text: {text}")
        # Example activity: Analyze author's style
        # You can replace this with your specific advanced-level activity
        prompt = "Write a paragraph analyzing the author's style in the text."
        user_input = input(prompt)
        #print("

game = LinguaMasterGame()  # Creating an instance of the Game class
game.start_game()  # Calling the start_game method on the game instance
