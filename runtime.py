import discord
import os

class Runtime():
  client = discord.Client()
  token = os.environ["TOKEN"]

  # current channel
  channel = None

  # all variables are global
  vars = {}

  # listeners is an array of arrays of size 2
  # first item in each array is condition method
  # second is statement method
  listeners = []
  
  # methods
  async def say(args, runtime):
    [await runtime.channel.send(i) for i in args]
    
  methods = {"say": say}

  def run(self):
    @self.client.event
    async def on_ready():
      print("Discord Bot Ready!")

    @self.client.event
    async def on_message(message):

      # ignore messages sent by self
      if message.author == self.client.user:
        return
    
      self.vars["message"] = message.content

      # set current channel
      self.channel = self.client.get_channel(message.channel.id)
      
      # go through listeners
      # i[0] is a condition method
      # i[1] is a statement method
      for i in self.listeners:
        if await (i[0])():
          await (i[1])()
   
    self.client.run(self.token)