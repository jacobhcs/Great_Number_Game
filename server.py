from flask import Flask, render_template, request, redirect, session
import random

app = Flask(__name__)
app.secret_key = 'secretkey'

def generate_random_number():
  session['random_num'] = random.randint(1, 100)

@app.route('/')
def index():
  generate_random_number()
  print(session['random_num'])
  return render_template('index.html')

@app.route('/guess', methods=['POST'])
def guessgoal():
    print(session['random_num'])
    session['guess'] = request.form['guess']
    return redirect('/show')

@app.route('/show')
def showguess():
  print(session['guess'])
  if int(session['guess']) < session['random_num']:
     results = 'TO LOW'
  elif int(session['guess']) > session['random_num']:
     results = "TOO HIGH"
  else:
     results = "YOU GOT IT RIGHT!"
  return render_template('guess.html', randomguess=session['guess'], results=results)

if __name__=='__main__':
  app.run(debug=True)