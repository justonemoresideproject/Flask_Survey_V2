from flask import Flask, redirect, request, render_template, flash
# from flask_debugtoolbar import DebugToolbarExtension
from surveys import Survey, Question

app = Flask(__name__)

app.config['SECRET_KEY'] = "chickenz"
# app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
# debug = DebugToolBarExtension(app)

RESPONSES_KEY = ""

@app.route('/')
def home_page():
    return render_template('home.html', survey=survey)

@app.route('/start', methods=["POST"])
def start():
    session[RESPONSES_KEY] = []
    return redirect('/questions/0')

@app.route('/answer', methods=['POST'])
def handle_question():
    # taken from solution
    choice = request.form['answer']

    responses = session[RESPONSES_KEY]
    responses.append(choice)
    session[RESPONSES_KEY] = responses

    if(len(responses) == len(survey.questions)):
        return redirect("/complete")
    else:
        return redirect(f"/questions/{len(responses)}")

@app.route('/questions/<int:qid>')
def show_questions(qid):
    responses = session.get(RESPONSES_KEY)

    if (responses is None):
        return redirect('/')
    
    if(len(responses) len(survey.questions)):
        return redirect("/complete")
    
    if(len(responses) != qid):
        flash(f"Invalid question id: {qid}.")
        return redirect(f"/questions/{len(responses)}")

    question = survey.questions[qid]
    return render_template("question.html", question_num=qid, question=question)

@app.route("/complete")
def complete():
    return render_template('thankYou.html')

# @app.route('/questions/3')
# def question_three():
#     if '2' in RESPONSE:
#         RESPONSE['3'] = 'NOTHING'
#         question = cookie_survey.questions[3].question
#         title = cookie_survey.title
#         instructions = cookie_survey.instructions
#         answer = request.args.get('answer')
#         if  answer == None:
#             flash('must give an answer')
#             redirect('/questions/2')
#         else:
#             RESPONSE['2'] = answer
#             return render_template('questionThree.html', question=question, title=title, instructions=instructions)
#     else:
#         flash('Cannot skip!')
#         return redirect('/questions/2')

# @app.route('/thankYou')
# def finish():

#     answer = request.args.get('answer')
#     if  answer == None:
#         flash('must give an answer')
#         redirect('/questions/3')
#     else:
#         RESPONSE['3'] = answer
#         return render_template('thankYou.html')
