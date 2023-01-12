from flask import Flask, request, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from surveys import satisfaction_survey as survey

responses = []
app = Flask(__name__)
app.config['SECRET_KEY'] = 'key'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

@app.route('/')
def render_page():
    responses.clear()
    return render_template('base.html', survey = survey)

@app.route('/question/1')
def render_survey_page():
    return render_template('question1.html', survey = survey)

@app.route('/answer1', methods = ['POST'])
def record_answer():
    answer = request.form['answer']
    responses.append(answer)
    return redirect('/question/2')

    
@app.route('/question/2')
def render_survey_page2():
    if len(responses) < 1:
        flash('Please answer all questions before proceeding')
        return redirect('/question/1')
    return render_template('question2.html', survey = survey)

@app.route('/answer2', methods = ['POST'])
def record_answer2():
    answer = request.form['answer']
    responses.append(answer)
    return redirect('/question/3')

@app.route('/question/3')
def render_survey_page3():
    if len(responses) < 2:
        flash('Please answer all questions before proceeding')
        return redirect('/question/2')
    return render_template('question3.html', survey = survey)

@app.route('/answer3', methods = ['POST'])
def record_answer3():
    answer = request.form['answer']
    responses.append(answer)
    return redirect('/question/4')

@app.route('/question/4')
def render_survey_page4():
    if len(responses) < 3:
        flash('Please answer all questions before proceeding')
        return redirect('/question/3')
    return render_template('question4.html', survey = survey)

@app.route('/answer4', methods = ['POST'])
def record_answer4():
    answer = request.form['answer']
    responses.append(answer)
    return redirect('/complete')

@app.route('/complete')
def render_complete():
    if len(responses) < 4:
        flash('Please answer all questions before proceeding')
        return redirect('/question/4')
    return render_template('complete.html', survey = survey, responses = responses)