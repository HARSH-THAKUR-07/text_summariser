from flask import Flask, render_template, request

app = Flask(__name__)

def simple_summarizer(text, num_sentences=2):
    sentences = text.split('. ')
    summary = '. '.join(sentences[:num_sentences]) + ('.' if len(sentences) > num_sentences else '')
    return summary

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/summarize', methods=['POST'])
def summarize():
    text = request.form['text']
    summary = simple_summarizer(text)
    return render_template('index.html', summary=summary)

if __name__ == '__main__':
    app.run(debug=True)
