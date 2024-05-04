import json

from flask import Flask, render_template, request, redirect, url_for, session

from model.Question import Question
from model.Topic import Topic
from service.QuestionGenerator import QuestionGenerator

app = Flask(__name__)
app.secret_key = 'your_secret_key'
topicService = Topic()


@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['name'] = request.form['name']
        session['age'] = request.form['age']
        session['language'] = request.form['language']
        return redirect(url_for('topics'))
    return render_template('login.html')


@app.route('/topics', methods=['GET', 'POST'])
def topics():
    topic_list = topicService.get_topics();
    if request.method == 'POST':
        session['topic'] = request.form['topic']
        return redirect(url_for('learning_objective'))
    return render_template('topics.html', topics=topic_list)


@app.route('/learning_objective')
def learning_objective():
    if 'topic' not in session:
        return redirect(url_for('topics'))  # Ensure there is a fallback if the session does not have a topic
    topic = session['topic']
    objectives = topicService.get_objectives()
    objective = objectives.get(topic, "No objective available for this topic.")
    return render_template('learning_objective.html', topic=topic, objective=objective)


@app.route('/question', methods=['GET', 'POST'])
def question():
    if 'topic' not in session:
        return redirect(url_for('topics'))  # Redirect to topic selection if no topic is chosen

    topic = session['topic']
    questions = get_questions_by_topic(session, topic)
    print("here324")
    if 'current_question' not in session:
        session['current_question'] = 0  # Initialize question index

    current_question = session['current_question']
    if request.method == 'POST':
        user_answer = request.form['answer']
        correct_answer = questions[current_question].answer
        if user_answer == correct_answer:
            session['current_question'] += 1  # Move to the next question
            if session['current_question'] >= len(questions):
                return redirect(url_for('completion'))  # Redirect when all questions are answered

    question_data = questions[current_question]
    print(question_data.choices)
    return render_template('question.html', question=question_data.question_text, choices=question_data.choices)


@app.route('/completion')
def completion():
    # Reset the questions index
    session.pop('active_topic_user', None)
    session.pop('current_question', None)
    return render_template('completion.html')  # Show some completion message


def get_questions_by_topic(session, topic):
    if session['active_topic_user'] != session['name'] + session['topic'] + ".json":
        generator = QuestionGenerator()
        questions = generator.generate_questions(session, topic)
        session['active_topic_user'] = session['name'] + session['topic'] + ".json"
        question = Question()
        json_object = question.to_json(questions)
        with open(session['active_topic_user'], "w") as outfile:
            outfile.write(json_object)
        return questions
    else:
        with open(session['active_topic_user'], 'r') as openfile:
            json_object = json.load(openfile)
        questions = Question.from_json(json_object)
        return questions


if __name__ == '__main__':
    app.run(debug=True)
