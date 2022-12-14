
from flask import Flask, render_template, session, request, redirect
app = Flask(__name__)
app.secret_key = 'gdhabcvyus7623yt78r28g1bhjbbcd78g1uybuyb8b76xcffg67g67g26g67'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():

    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comment'] = request.form['comment']

    return redirect('/results')

@app.route('/results')
def results():
    return render_template('results.html')




if __name__=='__main__':
    app.run(debug=True)