from flask import Flask
from flask import request
from flask import render_template
from calculator import ProfitCalculator

app = Flask(__name__)


@app.route("/", methods=["GET"])
def home():
    return render_template('home.html', title="Stock Profit Calculator")


@app.route("/", methods=["POST"])
def output():
    result = ProfitCalculator().calculate_profit(request.form)
    return render_template('result.html', title="Profit Report", result=result)


if __name__ == "__main__":
    app.run(debug=True)
