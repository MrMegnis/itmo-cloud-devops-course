from flask import Flask, render_template, request, jsonify
from model_interface import HuggingFaceQAModel
from logging import warning
import os

app = Flask(__name__)

# Loading model for question answering
warning("Start model loading")
# model = HuggingFaceQAModel(model_name="Megnis/bert-finetuned-sbersquad")
# comment because to long to load in lab
warning("End model loading")
warning(os.path.dirname(os.path.abspath(__file__)))
warning("some env stuff:" + os.getenv("envStuff"))


@app.route('/api', methods=['GET'])
def api():
    return jsonify({'answer': "api is working"})


@app.route('/api/get_answer', methods=['POST'])
def get_answer():
    context = request.form['context']
    question = request.form['question']

    # get answer from model
    # response = model.generate(context=context, question=question)
    response = "response"  # comment upper code for testing

    # return answer in JSON format
    return jsonify({'context': context, 'question': question, 'answer': response})


@app.route('/api/get_model_answer', methods=['POST'])
def get_model_answer():
    context = request.form['context']
    question = request.form['question']

    # get answer from model
    # response = model._get_model_answer(context=context, question=question)
    response = "response"  # comment upper code for testing

    # return answer in JSON format
    return jsonify({'context': context, 'question': question, 'model_answer': response})


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True, port=5000)
