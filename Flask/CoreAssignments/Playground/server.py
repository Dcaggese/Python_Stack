from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def welcome():
    return "working"

@app.route('/play/<times>/<color>')
def play(times,color):
    num = int(times)
    return render_template("index.html", box_div = 'width:200px;height:200px;border:2px;background-color:'+ color, count = num)

if __name__ == "__main__":
    app.run(debug = True)