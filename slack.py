from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/lol', methods=['GET', 'POST'])
def lol_bot():
  text = request.form.get('text')

  return jsonify({
    'response_type': 'in_channel',
    'text': f'lol {text}',
  })

if __name__ == 'main':
  app.run()
