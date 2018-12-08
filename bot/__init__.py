from bot.states import *

states = {
  'ENTRY': entry,
  'JOKE': joke,
}

def enter_state(state, context, output):
  states[state].on_enter(context, output)

def execute_state(state, context, output, input_fn):
  input_data = input_fn()
  return states[state].on_input(input_data, context, output)
