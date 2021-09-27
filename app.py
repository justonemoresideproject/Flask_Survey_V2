from flask import Flask, redirect, request, render_template, flash
# from flask_debugtoolbar import DebugToolbarExtension
from surveys import Survey, Question

app = Flask(__name__)

app.config['SECRET_KEY'] = "chickenz"
# app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
# debug = DebugToolBarExtension(app)

cookie_survey = Survey('Rate the cookie you just had', 'give a yes, no, a number, or written response', [
    Question('Do you like cookies?'),
    Question('Are cookies your favorite treat?'),
    Question('On a scale from 1 - 5 (5 being best) how good was your cookie?'),
    Question('Write out a 20 page paper on how much you love or hate cookies')
])

# RESPONSES = []

RESPONSE = {}

@app.route('/')
def home_page():
    return render_template('home.html')

@app.route('/questions/0')
def question_zero():
    RESPONSE['0'] = 'NOTHING'
    question = cookie_survey.questions[0].question
    title = cookie_survey.title
    instructions = cookie_survey.instructions
    return render_template('questionZero.html', question=question, title=title, instructions=instructions)

@app.route('/questions/1')
def question_one():
    if '0' in RESPONSE:
        RESPONSE['1'] = 'NOTHING'    
        question = cookie_survey.questions[1].question
        title = cookie_survey.title
        instructions = cookie_survey.instructions
        answer = request.args.get('answer')
        if answer == None:
            flash('must give an answer')
            return redirect('/questions/0')
        else:
            RESPONSE['0'] = answer
            return render_template('questionOne.html', question=question, title=title, instructions=instructions)
    else:
        flash('Cannot skip!')
        return redirect('/questions/0')

@app.route('/questions/2')
def question_two():
    if '1' in RESPONSE:
        RESPONSE['2'] = 'NOTHING'
        question = cookie_survey.questions[2].question
        title = cookie_survey.title
        instructions = cookie_survey.instructions
        answer = request.args.get('answer')
        if answer == None:
            flash('must give an answer')
            redirect('/questions/1')
        else:
            RESPONSE['1'] = answer
            return render_template('questionTwo.html', question=question, title=title, instructions=instructions)
    else:
        flash('Cannot skip!')
        return redirect('/questions/1')

@app.route('/questions/3')
def question_three():
    if '2' in RESPONSE:
        RESPONSE['3'] = 'NOTHING'
        question = cookie_survey.questions[3].question
        title = cookie_survey.title
        instructions = cookie_survey.instructions
        answer = request.args.get('answer')
        if  answer == None:
            flash('must give an answer')
            redirect('/questions/2')
        else:
            RESPONSE['2'] = answer
            return render_template('questionThree.html', question=question, title=title, instructions=instructions)
    else:
        flash('Cannot skip!')
        return redirect('/questions/2')

@app.route('/thankYou')
def finish():

    answer = request.args.get('answer')
    if  answer == None:
        flash('must give an answer')
        redirect('/questions/3')
    else:
        RESPONSE['3'] = answer
        return render_template('thankYou.html')
