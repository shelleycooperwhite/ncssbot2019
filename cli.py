def prompt():
  # Ask the user for input.
  return input('> ')

def run(state, context):
  # While state is not EXIT, talk to the user.
  while state != 'EXIT':
    # Enter the new state.
    bot.enter_state(state, context, print)

    # Do the action associated with this state.
    state, data = bot.execute_state(state, context, print, prompt)

if __name__ == '__main__':
  import bot

  state = 'ENTRY'
  context = {}

  run(state, context)
