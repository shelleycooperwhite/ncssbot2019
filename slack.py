from flask import Flask, request, jsonify, json

app = Flask(__name__)

@app.route('/lol', methods=['GET', 'POST'])
def lol_bot():
  text = request.values.get('text')

  return jsonify({
    'response_type': 'in_channel',
    'text': f'lol {text}',
  })

@app.route('/slack/event', methods=['GET', 'POST'])
def event():
  print(request.values)
  print(request.get_json())

  challenge = request.get_json().get('challenge')

  return jsonify({'challenge': challenge})

if __name__ == 'main':
  app.run()
