from flask import Flask, request

app = Flask(__name__)

@app.route('/lol', methods=['GET', 'POST'])
def lol_bot():
  text = request.form.get('text')

  return f'lol {text}'

if __name__ == 'main':
  app.run()
