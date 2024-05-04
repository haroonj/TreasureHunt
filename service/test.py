# import os
#
# from openai import OpenAI
#
# os.environ["OPENAI_API_KEY"] = ""
# client = OpenAI()
# response = client.chat.completions.create(
#     model="gpt-4",
#     messages=[
#         {
#             "role": "system",
#             "content": "You will be provided with a topic and child age, and your task is to generate a story consisting of 5 interconnected questions related to this topic, suitable for a child aged. Each question should naturally lead to the next, forming a coherent narrative. For each question, return options for answers and mention the correct answer in a valid JSON "
#         },
#         {"role": "user",
#          "content": "the topic is science, the age is 7"}],
#     temperature=0.7,
#     max_tokens=518,
#     top_p=1
# )
# print(response.choices[0].message.content)
# from service.QuestionGenerator import QuestionGenerator
#
# generator = QuestionGenerator()
# session = {'name': 'hh', 'age': '8'}
# print(generator.generate_questions(session, 'Geography'))
