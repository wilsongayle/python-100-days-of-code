# from data import question_data
from quiz_brain import QuizBrain
from question_bank import QuestionBank

NUMBER_OF_QUESTIONS = 10

def quiz_game():
    question_bank = QuestionBank(NUMBER_OF_QUESTIONS).get_questions()

    quiz = QuizBrain(question_bank)

    while quiz.still_has_questions():
        quiz.next_question()

    quiz.end_game()

quiz_game()