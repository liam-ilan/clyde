# NOTE: as of right now, this repo is mostly just a clone of the original repl, with some tweaks. (https://repl.it/@discordbotlang/clyde)

# Clyde
Clyde is a simple programming language that allows anyone, with no experience, to build a Discord bot. 
It is crafted to create a simple experience for those using it.

Join our [discord server](https://discord.gg/BFX5xAa) to test out a demo bot built using Clyde.

Note: this language is pretty simple and barebones for now. (WIP)

## How To
Clyde can run and deploy your own bot within repl.it.

First off, clone this repl (fork or download).

To setup the discord bot,
1. Open the discord developer portal.
2. Create a new application.
3. Add a bot to your discord application.
4. Create a file named .env. This file will be hidden from the public.
5. Copy the Bot's token, and paste into the .env file in the following format:
```
TOKEN=<Your token goes here>
```

To invite the bot to your server,
1. Go to the OAuth2 tab
2. Check the box labeled bot under scopes
3. Under bot permissions, check all the boxes you need
4. At the bottom of scopes, there will be a text box with a link
5. Copy and paste the link into you browser.

You can edit your code in the main.clyde file. See tutorial for more info.

## Tutorial
Writing code for your bot using Clyde is super simple.

To say something when a message is sent,
```
on "ping":
  say "pong"
```

Messages in Clyde are always surrounded by quotes.
Say is currently the only command implemented.

You can have multiple events,
```
on "ping":
  say "pong"

on "What's up?":
  say "Hey!"
```

You can create variables within Clyde much like the simple syntax found within Python,
```
on "Hello":
  name = "Bob"
  say name
```

Sometimes, we want to say many things, in many commands,
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

And sometimes, we just want one line,
```
on "Hello": say "hi", "greetings", "good morning"
```

We can also create complex bots, with these simple rules,
```
on "!ping":
  say "pong"

on "!info":
  say "Greetings. I am a demo bot to display the capabilities of Clyde."
  say "Written by Pranav Karthik and Liam Ilan."

on "!":
  say "please supply a command"
  
on "ping":
  say "You need to type !ping :)"
```

## Conclusion
While building Clyde, we wanted to add numerous features which we unfortunately could not, due to the time restrictions.
Some of those features include:
* more commands
* conditionals
* embeds
* arithmetic (and numbers)
* lists
* errors
* discord-specific attributes (user, server, channel, etc.)

## Demo
Join our [discord server](https://discord.gg/BFX5xAa) to test out a demo bot built using Clyde.

## Credits
* @discordsheep - Parser + Runtime
* @Parzivox - Lexer + Runtime