# Improve the ask_number(): function so that the function can be
# called with a step value (step of 1)

def ask_number(question, low, high, step = 1):
  """Ask for a number within in a range."""
  response = None
  while response not in range(low, high):
    response = int(input(question)) + step
  return response

ask_number("Pick a number from 0 - 8: ", 0, 8, 2)
