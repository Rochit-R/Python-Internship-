class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0

    def display_question(self, question):
        print(question['question'])
        for idx, option in enumerate(question['options'], 1):
            print(f"{idx}. {option}")

    def get_user_answer(self):
        while True:
            try:
                choice = int(input("Enter your choice: "))
                if 1 <= choice <= len(self.questions[0]['options']):
                    return choice
                else:
                    print("Invalid choice. Please enter a number within the given range.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    def check_answer(self, question, user_answer):
        correct_answer = question['answer']
        if user_answer == correct_answer:
            print("Correct!")
            self.score += 1
        else:
            print("Incorrect. The correct answer is:", question['options'][correct_answer - 1])

    def run_quiz(self):
        for question in self.questions:
            self.display_question(question)
            user_choice = self.get_user_answer()
            self.check_answer(question, user_choice)
        print("Quiz completed!")
        print("Your final score is:", self.score)


if __name__ == "__main__":
    questions = [
        {
            "question": "Which programming language is commonly used for developing AI applications?",
            "options": ["Python", "C++", "Java"],
            "answer": 1
        },
        {
            "question": "What does 'AI' stand for?",
            "options": ["Advanced Intelligence", "Artificial Intelligence", "Automated Interaction"],
            "answer": 1
        },
        {
            "question": "Which AI technique is inspired by the structure and function of the human brain?",
            "options": ["Genetic Algorithms", "Expert Systems", "Neural Networks"],
            "answer": 1
        },
        {
            "question": "What is the name of the AI that defeated the world champion Go player?",
            "options": ["Watson", "Deep Blue", "AlphaGo"],
            "answer": 1
        },
        {
            "question": "What is the process of teaching a machine learning model with labeled data?",
            "options": ["Unsupervised Learning", "Reinforcement Learning", "Supervised Learning"],
            "answer": 1
        },
        {
            "question": "What is the term for a computer program that simulates human conversation?",
            "options": ["Robot", "Chatbot", "Algorithm"],
            "answer": 1
        },
        {
            "question": "Which company developed the AI assistant 'Siri'?",
            "options": ["Microsoft", "Google", "Apple"],
            "answer": 1
        }
    ]

    quiz = Quiz(questions)
    quiz.run_quiz()
