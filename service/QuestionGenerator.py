import os

from openai import OpenAI

from model.Question import Question


class QuestionGenerator:
    def __init__(self):
        self.schema = '''
        {
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "story": {
      "type": "array",
      "items": [
        {
          "type": "object",
          "properties": {
            "question": {
              "type": "string"
            },
            "options": {
              "type": "array",
              "items": [
                {
                  "type": "string"
                },
                {
                  "type": "string"
                },
                {
                  "type": "string"
                },
                {
                  "type": "string"
                }
              ]
            },
            "answer": {
              "type": "string"
            }
          },
          "required": [
            "question",
            "options",
            "answer"
          ]
        },
        {
          "type": "object",
          "properties": {
            "question": {
              "type": "string"
            },
            "options": {
              "type": "array",
              "items": [
                {
                  "type": "string"
                },
                {
                  "type": "string"
                },
                {
                  "type": "string"
                },
                {
                  "type": "string"
                }
              ]
            },
            "answer": {
              "type": "string"
            }
          },
          "required": [
            "question",
            "options",
            "answer"
          ]
        }
      ]
    }
  },
  "required": [
    "story"
  ]
}
        '''

    def generate_questions(self, session, topic):
        age = session['age']
        os.environ["OPENAI_API_KEY"] = ""
        client = OpenAI()
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {
                    "role": "system",
                    "content": "You will be provided with a topic and child age, and your task is to generate a story consisting of 5 interconnected questions related to this topic, suitable for a child aged. Each question should naturally lead to the next, forming a coherent narrative. For each question, return options for answers and mention the correct answer in a valid JSON comply with this schema {0} just return the json with out schema".format(
                        self.schema),
                },
                {"role": "user",
                 "content": "the {0} is science, the age is {1}".format(topic, age)}],
            temperature=0.7,
            max_tokens=518,
            top_p=1
        )
        # print(response.choices[0].message.content)
        questions = Question.from_json(response.choices[0].message.content)
        return questions
