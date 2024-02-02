from flask import Flask, render_template, request, jsonify
import pyshorteners
import pyperclip

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/shorten', methods=['POST'])
def shorten():
    long_url = request.form['url']
    shortened_url = pyshorteners.Shortener().tinyurl.short(long_url)
    return jsonify({'shortened_url': shortened_url})

if __name__ == '__main__':
    app.run(debug=True)
