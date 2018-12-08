from flask import Flask, request

app = Flask(__name__)

def lol_bot():
  text = request.args.get('text')

  return f'lol {text}'

app.add_url_rule('/lol', 'lol_bot', lol_bot)

if __name__ == 'main':
  app.run()
