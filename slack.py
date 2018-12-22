from flask import Flask, request, jsonify, json

import requests

app = Flask(__name__)


def send_message(text, channel):
  '''Send a message of a particular type to a slack channel.'''
  if text:
    json_response = {'text': text, 'channel': channel}
    headers = {
      'Authorization': 'Bearer xoxb-509687114689-511356328919-sfElXzwnCkF8aMLLwJVpeCMs',
      'Content-Type': 'application/json',
    }
    requests.post('https://slack.com/api/chat.postMessage', data=json.dumps(json_response), headers=headers)


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

  payload = request.get_json()
  # if payload:
  #   event = payload.get('event')
  #   if event.get('type') == 'message':
  #     # todo: Send message back to user

  send_message('Hello from bot!', 'DF08WMPR8')

  return ('', 204)

if __name__ == 'main':
  app.run()
