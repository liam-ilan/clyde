# Clyde
Clyde is a simple programming language that allows anyone, with no experience, to build a Discord bot. 
It is crafted to create a simple experience for those using it.

This was originally a replit language jam submission (https://repl.it/@discordbotlang/clyde).

Join our [discord server](https://discord.gg/BFX5xAa) to test out a demo bot built using Clyde.

Note: this language is pretty simple and barebones for now. (WIP)

## Setup
To setup the discord bot,
1. Open the discord developer portal.
2. Create a new application.
3. Add a bot to your discord application.
4. Create a .env file.
5. Copy the Bot's token, and paste into the .env file in the following format:
```
TOKEN=<Your token goes here>
```

To invite the bot to your server,
1. Go to the OAuth2 tab
2. Check the box labeled bot under scopes
3. Under bot permissions, check all the boxes you need
4. At the bottom of scopes, there will be a text box with a link
5. Copy and paste the link into you browser to invite the bot

## Hello World
Delete the contents of `main.clyde`, and write the following:
```
on "hello bot":
  say "hello world"
```

Then run `poetry run python clyde/main.py` 
or, if debugging, run `poetry run python clyde/debug.py`

Your bot should be online, and if you say "hello bot", it will respond with "hello world"

## Tutorial
Writing code for your bot using Clyde is super simple.

Clyde programs are made up of multiple listeners.
They start with `on` followed by a message surrounded in quotes, then a colon, and then a list of instructions.

Listeners listen for messages sent by a user of your bot, and will run their instructions if they hear the correct message.

Example:
```
on "ping":
  say "pong"
```

You can have multiple listeners,
```
on "ping":
  say "pong"

on "What's up?":
  say "Hey!"
```

Sometimes, you want to say many things, in many commands,
```
on "Hello":
  say "hi"
  say "hello"
```

Or many things, in one command,
```
on "Hello":
  say "hi", "greetings", "good morning"
```

And sometimes, you just want one line,
```
on "Hello": say "hi", "greetings", "good morning"
```

If you want to print a message to the console, instead of sending it to your server,
```
on "log something":
  log "something logged!"
```

You can also store messages in variables, for later use,
```
on "Hello":
  name = "Bob"
  say name
```

You can store booleans (true or false) in variables too,
```
on "turn light on":
  light = true

on "turn light off":
  light = false
```

And then run commands if a boolean is true,
```
on "turn light on":
  light = true

on "turn light off":
  light = false

on "light on?":
  if light say "light is on"
```

## Demo
Join our [discord server](https://discord.gg/BFX5xAa) to test out a demo bot built using Clyde.

## Credit
* https://github.com/pranavkarthik10
* https://github.com/liam-ilan