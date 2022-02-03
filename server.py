from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html", row=8, col=8, color1='red', color2='black')


@app.route('/<int:x>')
def row(x):
    return render_template("index.html", row=x, col=8, color1='red', color2='black')


@app.route('/<int:x>/<int:y>')
def row_col(x, y):
    return render_template("index.html", row=x, col=y, color1='red', color2='black')


@app.route('/<int:x>/<int:y>/<string:one>')
def row_col_1(x, y, one):
    return render_template("index.html", row=x, col=y, color1=one, color2='black')


@app.route('/<int:x>/<int:y>/<string:one>/<string:two>')
def row_col_2(x, y, one, two):
    return render_template("index.html", row=x, col=y, color1=one, color2=two)


if __name__ == "__main__":
    app.run(debug=True)
