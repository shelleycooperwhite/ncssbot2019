import random

JOKES = [
  'Why don\'t jokes work in octal? Because 7 10 11.',
  'I could tell you a joke about UDP but I don\'t know if you would get it.',
  'There are 10 kinds of people: those who understand binary and those who don\'t.',
]

def on_enter(data, output):
  output('Here it is:')
  output(random.choice(JOKES))
  output('Would you like to hear another?')

def on_input(input_data, data, output):
  if input_data == 'yes':
    return 'JOKE', None

  return 'ENTRY', None
