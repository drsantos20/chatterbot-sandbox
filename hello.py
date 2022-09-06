from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer, ListTrainer

app = Flask(__name__)

english_bot = ChatBot("Chatterbot", storage_adapter="chatterbot.storage.SQLStorageAdapter")
trainer = ListTrainer(english_bot)

trainer.train([
    "Olá, Bom dia",
    "Bom dia!",
])

trainer.train([
    "Opa",
    "Como posso te ajudar?",
])

trainer.train([
    "Preciso de uma informação",
    "Qual seria a informação?",
])


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return str(english_bot.get_response(userText))


@app.route('/hello')
def hello():
    return 'Hello, World!'


if __name__ == "__main__":
    app.run()
