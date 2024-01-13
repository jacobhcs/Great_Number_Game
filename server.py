from flask import Flask, render_template, request, redirect, session
import random

app = Flask(__name__)
app.secret_key = 'secretkey'

def generate_random_number():
  session['random_num'] = random.randint(1, 100)

@app.route('/')
def index():
  session.clear()
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
  if 'guess' not in session:
        return redirect('/')
  elif int(session['guess']) < session['random_num']:
     results = 'TO LOW'
     session['color'] = 'bg-danger'
  elif int(session['guess']) > session['random_num']:
     results = "TOO HIGH"
     session['color'] = 'bg-danger'
  else:
     results = "YOU GOT IT RIGHT!"
     session['color'] = 'bg-success'
     session['reset'] = True
  return render_template('guess.html', randomguess=session['guess'], results=results)

@app.route('/reset', methods=['POST'])
def reset():
   return redirect('/')

if __name__=='__main__':
  app.run(debug=True)