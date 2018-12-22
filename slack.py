import os, requests

from flask import Flask, request, jsonify, json

import bot

app = Flask(__name__)


def send_message(text, channel):
  """
  Send a message to a slack channel.
  """
  if text:
    json_response = {'text': text, 'channel': channel}
    headers = {
      'Authorization': 'Bearer {}'.format(os.environ['TOKEN']),
      'Content-Type': 'application/json',
    }
    response = requests.post('https://slack.com/api/chat.postMessage', data=json.dumps(json_response), headers=headers)
    print(response.json())
    print('Sent a message')


@app.route('/lol', methods=['GET', 'POST'])
def lol_bot():
  text = request.values.get('text')

  return jsonify({
    'response_type': 'in_channel',
    'text': f'lol {text}',
  })

@app.route('/slack/event', methods=['GET', 'POST'])
def slack_event():
  global state, data

  payload = request.get_json()
  print(payload)
  if payload:

    if payload.get('type') == 'url_verification':
      return payload.get('challenge')

    event = payload.get('event')
    # If it was a message and it wasn't from our bot, send a message back
    # todo exclude slash commands
    # if event.get('type') == 'message' and event.get('subtype') != 'bot_message':
      # send_message('Hello from bot!', event.get('channel'))

    # If it was a message and it wasn't from our bot, send a message back
    if event.get('type') == 'message' and event.get('subtype') != 'bot_message':
      def output(text):
        return send_message(text, event.get('channel'))

      def prompt():
        return event.get('text')

      # While state is not EXIT, talk to the user.
      if state != 'EXIT':
        # Enter the new state.
        bot.enter_state(state, context, output)

        # Do the action associated with this state.
        state, data = bot.execute_state(state, context, output, prompt)

  return jsonify({})

state = 'ENTRY'
context = {}

if __name__ == 'main':

  app.run()
