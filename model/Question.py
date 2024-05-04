import json


class Question:
    def __init__(self, text, answer, choices):
        self.question_text = text
        self.answer = answer
        self.choices = choices

    def __str__(self):
        return self.question_text

    def get_answer(self):
        return self.answer

    def get_choices(self):
        return self.choices

    def to_dict(self):
        return {
            'question': self.question,
            'answer': self.answer,
            'options': self.options
        }


    @classmethod
    def from_json(cls, json_data):
        data = json.loads(json_data)
        questions = []
        for item in data["story"]:
            print(item)
            question = Question(item["question"], item["answer"], item["options"])
            questions.append(question)

        return questions

    def to_json(self, questions):
        story_dict = {'story': [question.to_dict() for question in questions]}
        return json.dumps(story_dict, indent=4)

