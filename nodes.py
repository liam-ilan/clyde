import runtime

class Program:
  def __init__(self, events):
    self.events = events

  def __repr__(self, depth = 0):
    res = ""
    res += ("\t" * depth) + "program"  + "\n"
    for e in self.events:
      res += e.__repr__(depth + 1)
      
    return res

  # returns runtime object
  def runtime(self):
    res = runtime.Runtime()

    # add listeners to runtime object
    for e in self.events:
      e.runtime = res

      res.listeners.append(
        [
          e.conditionMethod,
          e.statementMethod
        ]
      )

    return res

class Event:
  def __init__(self, condition, statement):
    self.condition = condition
    self.statement = statement

  def __repr__(self, depth = 0):
    res = ""
    res += ("\t" * depth) + "event" + "\n"
    res += self.condition.__repr__(depth + 1)
    res += self.statement.__repr__(depth + 1)
    return res

  # returns true if statement should run, and false if it should not
  async def conditionMethod(self):
    return await self.condition.check(self.runtime)

  # runs statement
  async def statementMethod(self):
    return await self.statement.run(self.runtime)

class Statement:
  def __init__(self, lines):
     self.lines = lines

  def __repr__(self, depth = 0):
    res = ""
    res += ("\t" * depth) + "statement: " + "\n"
    for m in self.lines:
      res += m.__repr__(depth + 1)
    return res
  
  # runs all lines
  async def run(self, runtime):
    for l in self.lines:
      await l.run(runtime)

class Command:
  def __init__(self, name, args):
    self.name = name
    self.args = args

  def __repr__(self, depth = 0):
    res = ""
    res += ("\t" * depth) + "command: " + self.name + "\n"
    for arg in self.args:
      res += arg.__repr__(depth + 1)
    return res

  # runs a command according to the methods array in runtime
  async def run(self, runtime):
    newArgs = []

    # run all args
    for arg in self.args:
      newArgs.append(await arg.run(runtime))

    # call
    await (runtime.methods[self.name])(newArgs, runtime)

class Assignment:
  def __init__(self, name, value):
    self.name = name
    self.value = value

  def __repr__(self, depth = 0):
    res = ""
    res += ("\t" * depth) + "assignment: " + self.name + "\n"
    res += self.value.__repr__(depth + 1)
    return res

  # sets variable
  async def run(self, runtime):
    runtime.vars[self.name] = self.value

class Name:
  def __init__(self, id):
    self.id = id

  def __repr__(self, depth = 0):
    res = ("\t" * depth) + "name: " + self.id + "\n" 
    return res

  # returns value behind name
  async def run(self, runtime):
    try:
      return await runtime.vars[self.id].run(runtime)
    except:
      return

  # returns check method result of value behind name
  async def check(self, runtime):
    try:
      return await runtime.vars[self.id].check(runtime)
    except:
      return False

class String:
  def __init__(self, value):
    self.value = value

  def __repr__(self, depth = 0):
    res = ("\t" * depth) + "string: " + self.value + "\n" 
    return res

  # return string
  async def run(self, runtime):
    return self.value

  # check if string is message
  async def check(self, runtime):
    return self.value == runtime.vars["message"]
