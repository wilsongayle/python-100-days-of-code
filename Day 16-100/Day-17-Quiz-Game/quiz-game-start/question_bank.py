import requests
import html
from question_model import Question

class QuestionBank:
    def __init__(self, q_number):
        self.number_of_questions = q_number

    def get_questions(self):
        url = "https://opentdb.com/api.php"
        query_params = {
            "amount": self.number_of_questions,
            "type": "boolean"
        }
        response = requests.get(url, params=query_params)

        if response.status_code == 200:
            question_data = response.json()["results"]
        else:
            print(f"Failed to fetch data. Status code: {response.status_code}")
            return None

        question_bank = []

        for question in question_data:
            clean_question = html.unescape(question["question"])
            question_bank.append(Question(clean_question, question["correct_answer"]))

        return question_bank