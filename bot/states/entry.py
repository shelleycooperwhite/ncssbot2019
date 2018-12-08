def on_enter(data, output):
  output('Hello! How can I help?')

def on_input(input_data, data, output):

  if input_data == 'tell me a joke':
    return 'JOKE', None

  elif input_data == 'quit':
    return 'EXIT', None

  return 'ENTRY', None
