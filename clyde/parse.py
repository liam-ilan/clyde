import nodes

# program: {event}
def parse(tokens):
  events = []
  currentEvent = []

  # itterate over tokens
  for token in tokens:

    # if start of event
    if token.type == "EVENT":

      # if currentEvent exists
      if len(currentEvent) > 0: 

        # parse event and add to events
        events.append(parseEvent(currentEvent))

      # reset current event
      currentEvent = []

    # add to currentEvent on every loop  
    currentEvent.append(token)

  # add final event
  events.append(parseEvent(currentEvent))

  # return program
  return nodes.Program(events)

# event: "on" condition ":" statement
def parseEvent(tokens):

  # are we looking at the conditional part of the event
  isCondition = False

  # place to store condition and statement tokens
  condition = []
  statement = []

  # itterate of tokens
  for token in tokens:

    # deal with isCondition
    if token.type == "EVENT":
      isCondition = True
    elif token.type == "COLON":
      isCondition = False

    # append to condition or statement
    elif isCondition:
      condition.append(token)
    else:
      statement.append(token)

  # return parsed event
  return nodes.Event(parseCondition(condition), parseStatement(statement))

# condition: value
def parseCondition(tokens):

  # if is value
  if (tokens[0].type == "STRING" or tokens[0].type == "NAME") and len(tokens) == 1:
    return parseValue(tokens)

def parseIf(tokens):
  return nodes.If(parseValue([tokens[1]]), parseCommand(tokens[2:]))

# string: STRING
def parseString(tokens):
  return nodes.String(tokens[0].value)

# name: NAME
def parseName(tokens):
  return nodes.Name(tokens[0].value)

# statement: {command | assignment}
def parseStatement(tokens):

  # current line
  currentLine = []

  # lines to give to statement
  lines = []

  # current state
  state = ""

  commandIgnoreCounter = 0

  i = 0
  for token in tokens:

    # assignment
    if i + 1 < len(tokens) and tokens[i + 1].type == "EQUAL":

      # add to lines parsed line
      if state == "assignment":
        lines.append(parseAssignment(currentLine))
      elif state == "command":
        lines.append(parseCommand(currentLine))
      elif state == "if":
        lines.append(parseIf(currentLine))

      # reset
      currentLine = []

      # set state
      state = "assignment"

    if token.type == "IF":
      commandIgnoreCounter += 1

      # add to lines parsed line
      if state == "assignment":
        lines.append(parseAssignment(currentLine))
      elif state == "command":
        lines.append(parseCommand(currentLine))
      elif state == "if":
        lines.append(parseIf(currentLine))

      currentLine = []

      state = "if"

    # command
    if token.type == "COMMAND" and commandIgnoreCounter == 0:

      # add to lines parsed line
      if state == "assignment":
        lines.append(parseAssignment(currentLine))
      elif state == "command":
        lines.append(parseCommand(currentLine))
      elif state == "if":
        lines.append(parseIf(currentLine))

      # reset
      currentLine = []

      # set state
      state = "command"
    
    elif token.type == "COMMAND":
      commandIgnoreCounter = 0

    # add token
    currentLine.append(token)

    i += 1

  
  # add last line
  if state == "assignment":
    lines.append(parseAssignment(currentLine))
  elif state == "command":
    lines.append(parseCommand(currentLine))
  elif state == "if":
    lines.append(parseIf(currentLine))
  
  # return statement
  return nodes.Statement(lines)

# command: COMMAND arguments
def parseCommand(tokens):
  return nodes.Command(tokens[0].value, parseArguments(tokens[1:]))

# assignment: NAME "=" value
def parseAssignment(tokens):
  return nodes.Assignment(tokens[0].value, parseValue(tokens[2:]))

# arguments: value {"," value}
def parseArguments(tokens):

  # result
  res = []

  # current
  currentArgument = []
  
  # for each token
  for token in tokens:

    # if seperator, push arg
    if token.type == "SEPERATOR":
      res.append(parseValue(currentArgument))
      currentArgument = []

    # add to current arg
    else:
      currentArgument.append(token)

  # add final arg
  res.append(parseValue(currentArgument))

  # return
  return res

# value: string | name
def parseValue(tokens):
  if (tokens[0].type == "STRING"):
    return parseString(tokens)
  elif (tokens[0].type == "NAME"):
    return parseName(tokens)
  elif (tokens[0].type == "BOOLEAN"):
    return parseBoolean(tokens)

def parseBoolean(tokens):
  return nodes.Boolean(tokens[0].value)