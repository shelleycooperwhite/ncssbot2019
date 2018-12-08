from bot.states import *

states = {
  'ENTRY': entry,
  'JOKE': joke,
#   'WHAT IS EVENT QUERY': what_event_query,
#   'WHEN IS EVENT QUERY': when_event_query,
#   'WHERE IS EVENT QUERY': where_event_query,
#   'UNKNOWN EVENT QUERY': unknown_event_query,
#   'NO QUERY': no_query,
}

def enter_state(state, data, output):
  states[state].on_enter(data, output)

def execute_state(state, data, output, input_fn):
  input_data = input_fn()
  return states[state].on_input(input_data, data, output)
