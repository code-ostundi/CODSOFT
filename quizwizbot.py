import random
import re

class QuizwizBot:
    
    not_interested = ("not really", "no thanks", "maybe later", "not today", "pass")
    goodbye_phrases = ("bye", "goodbye", "see you later", "take care", "catch you later", "exit")

    def __init__(self):
        self.responses = {
            'ask_trivia': r'\bquestion\b',
            'give_feedback': r'\banswer\b',
            'fun_fact': r'\bfact\b',
            'play_again': r'\bplay\b\s+again'
        }
        self.trivia_questions = {
            "What is the currency of Japan?": "Yen",
            "Who is known for developing the theory of relativity?": "Einstein",
            "What’s the largest ocean on Earth?": "Pacific",
            "Which planet is known as the Red Planet?": "Mars",
            "Who painted the Mona Lisa?": "Da Vinci"
        }
        self.fun_facts = [
            "Did you know? Kangaroos can’t walk backward",
            "Here’s a quirky fact: A group of flamingos is called a 'flamboyance'.",
            "Giraffes have black tongues.",
            "Here's a historical tidbit: The shortest war in history lasted only 38-45 minutes between Britain and Zanzibar on August 27, 1896.",
            "Check this out: Octopuses have three hearts and their blood is blue!"
        ]
        self.current_question = None
        self.correct_answer = None

    def greet_user(self):
        self.username = input("Hey there! I'm QuizwizBot. What's your name?\n")
        initial_response = input(f"Hello {self.username}, are you in the mood for some trivia fun?\n")
        if initial_response.lower() in self.not_interested:
            print("No worries! Feel free to come back anytime. Have a fantastic day!")
            return
        self.start_interaction()

    def handle_exit(self, user_input):
        if user_input.lower() in self.goodbye_phrases:
            print("Thanks for hanging out! Catch you later!")
            return True
        return False

    def start_interaction(self):
        while True:
            user_input = input("Type 'question' if you want a trivia question, 'fact' if you'd like a fun fact, or 'exit' to wrap things up:\n").lower()
            if self.handle_exit(user_input):
                break
            response = self.generate_reply(user_input)
            print(response)

    def generate_reply(self, user_input):
        if re.search(self.responses['ask_trivia'], user_input):
            return self.handle_ask_trivia()
        elif re.search(self.responses['give_feedback'], user_input):
            return self.handle_give_feedback()
        elif re.search(self.responses['fun_fact'], user_input):
            return self.handle_fun_fact()
        elif re.search(self.responses['play_again'], user_input):
            return self.handle_play_again()
        else:
            return self.handle_unknown_query()

    def handle_ask_trivia(self):
        self.current_question, self.correct_answer = random.choice(list(self.trivia_questions.items()))
        return f"Alright, here's a trivia question for you: {self.current_question}\nType 'answer' to provide your response, or 'exit' if you want to end the game."

    def handle_give_feedback(self):
        if self.current_question:
            user_answer = input("What's your answer?\n")
            if user_answer.strip().lower() == self.correct_answer.lower():
                self.current_question = None
                self.correct_answer = None
                return "Awesome! You got it right!"
            else:
                self.current_question = None
                self.correct_answer = None
                return f"Not quite. The correct answer was {self.correct_answer}. Better luck next time!"
        else:
            return "You need to answer a trivia question first. Type 'question' to get a trivia question."

    def handle_fun_fact(self):
        return random.choice(self.fun_facts) + "\n"

    def handle_play_again(self):
        return self.handle_ask_trivia()

    def handle_unknown_query(self):
        return "Hmm, I'm not sure about that. You can type 'question' for a trivia question, 'fact' for a fun fact, or 'exit' if you want to end our chat.\n"


fun_trivia_bot = QuizwizBot()
fun_trivia_bot.greet_user()
