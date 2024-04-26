from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'

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
    topics = ["Science", "History & Culture", "Geography", "Sports", "Math"]
    if request.method == 'POST':
        session['topic'] = request.form['topic']
        return redirect(url_for('learning_objective'))
    return render_template('topics.html', topics=topics)


@app.route('/learning_objective')
def learning_objective():
    if 'topic' not in session:
        return redirect(url_for('topics'))  # Ensure there is a fallback if the session does not have a topic
    topic = session['topic']
    objectives = {
        "Science": "Learn about the scientific principles that govern the universe.",
        "History & Culture": "Explore the rich histories and diverse cultures around the world.",
        "Geography": "Discover the various geographical features and landscapes of our planet.",
        "Sports": "Understand the fundamentals of different sports and their historical significance.",
        "Math": "Dive into the concepts and applications of mathematics in everyday life."
    }
    objective = objectives.get(topic, "No objective available for this topic.")
    return render_template('learning_objective.html', topic=topic, objective=objective)

@app.route('/question', methods=['GET', 'POST'])
def question():
    if 'topic' not in session:
        return redirect(url_for('topics'))  # Redirect to topic selection if no topic is chosen

    # Example dictionary of questions and answers by topic
    questions = {
        "Science": [
            {"question": "What is the boiling point of water?", "choices": ["100°C", "90°C", "120°C", "80°C"], "answer": "100°C"},
            {"question": "Which gas is most prevalent in the Earth's atmosphere?", "choices": ["Oxygen", "Hydrogen", "Carbon Dioxide", "Nitrogen"], "answer": "Nitrogen"}
        ],
        # Add similar dictionaries for other topics
    }

    topic = session['topic']
    if 'current_question' not in session:
        session['current_question'] = 0  # Initialize question index

    current_question = session['current_question']
    if request.method == 'POST':
        user_answer = request.form['answer']
        correct_answer = questions[topic][current_question]['answer']
        if user_answer == correct_answer:
            session['current_question'] += 1  # Move to the next question
        if session['current_question'] >= len(questions[topic]):
            return redirect(url_for('completion'))  # Redirect when all questions are answered

    question_data = questions[topic][current_question]
    return render_template('question.html', question=question_data['question'], choices=question_data['choices'])

@app.route('/completion')
def completion():
    # Reset the questions index
    session.pop('current_question', None)
    return render_template('completion.html')  # Show some completion message

if __name__ == '__main__':
    app.run(debug=True)
