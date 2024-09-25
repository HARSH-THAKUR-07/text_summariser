from flask import Flask, render_template, request
from transformers import pipeline

app = Flask(__name__)
summarizer = pipeline("summarization")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/summarize', methods=['POST'])
def summarize():
    text = request.form['text']
    summary = summarizer(text, max_length=130, min_length=30, do_sample=False)
    return render_template('index.html', summary=summary[0]['summary_text'])

if __name__ == '__main__':
    app.run(debug=True)
