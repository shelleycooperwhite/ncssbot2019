from bot.states import *

states = {
  'ENTRY': entry,
  'JOKE': joke,
}

def enter_state(state, context, output):
  # Always check for end command.
  if state == 'EXIT':
    return output('Goodbye!')

  states[state].on_enter(context, output)

def execute_state(state, context, output, input_fn):
  input_data = input_fn()

  # Always check for end command.
  if input_data == 'quit':
    return 'EXIT', {}

  return states[state].on_input(input_data, context, output)
