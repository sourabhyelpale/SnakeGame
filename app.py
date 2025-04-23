from flask import Flask, render_template
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start')
def start_game():
    subprocess.run(['python', 'snake_game.py'])
    return "Game Over! Check the Python window for score. <br><a href='/'>Start Again</a>"

if __name__ == '__main__':
    app.run(debug=True)
