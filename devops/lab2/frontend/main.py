from flask import Flask, render_template, request, jsonify
import requests
from logging import warning
import os

app = Flask(__name__)

warning(os.path.dirname(os.path.abspath(__file__)))
with open("run/secrets/TOKEN", "r", encoding="utf-8") as f:
    TOKEN = f.readline()
warning("Check that token exist: " + TOKEN)
warning("interpolation example: " + os.getenv("some_frequently_changing_env"))


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        context = request.form.get('context', '')
        question = request.form.get('question', '')

        # get answer from model
        response = "response"

        # return answer in JSON format
        return render_template('index.html', context=context, question=question, answer=response)
    else:
        return render_template('index.html')


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True, port=5000)
