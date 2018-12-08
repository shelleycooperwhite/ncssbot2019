def on_enter(context, output):
  output('Hello! How can I help?')

def on_input(input_data, context, output):

  if input_data == 'tell me a joke':
    return 'JOKE', {}

  elif input_data == 'quit':
    return 'EXIT', {}

  return 'ENTRY', {}
