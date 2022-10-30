from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def checkerboard():
    return render_template("index.html")

@app.route('/<col>')
def dynamicCheckerboard(col):
    return render_template("dynamic.html", column = int(col))

if __name__ == "__main__":
    app.run(debug=True)