from flask import Flask, render_template
import openai


# rec
openai.api_key = API_KEY
PROMPT = "generate a goofy, funny, fake NY Times style newspaper text."
app = Flask(__name__)

response = openai.Completion.create(
    prompt = PROMPT
) # <-- fix this piece of garbage
@app.route("/")
def index():
    return render_template('index.html') # don't know how to properly acess a chat completion...
