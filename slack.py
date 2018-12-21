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
  challenge = request.values.get('challenge')
  print(request.values)

  return jsonify({'challenge': challenge})

if __name__ == 'main':
  app.run()
