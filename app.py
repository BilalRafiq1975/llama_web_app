from flask import Flask, render_template, request, jsonify
from chat import LlamaChat

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_input = request.form['user_input']
        if user_input.lower() in ['exit', 'quit']:
            return render_template('index.html', messages=[])
        chat = LlamaChat()
        response = chat.get_response(user_input)
        return render_template('index.html', messages=[{'role': 'user', 'content': user_input}, {'role': 'assistant', 'content': response}])
    return render_template('index.html', messages=[])

if __name__ == '__main__':
    app.run(debug=True)
