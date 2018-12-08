def prompt():
  '''The prompt for the commandline interface of the assistant.'''
  return input('> ')

def run(state, data):
  # While state is not EXIT, talk to the user.
  while state != 'EXIT':
    # Enter the new state.
    bot.enter_state(state, data, print)

    # Do the action associated with this state.
    state, data = bot.execute_state(state, data, print, prompt)

if __name__ == '__main__':
  import bot

  state = 'ENTRY'
  data = None

  run(state, data)
