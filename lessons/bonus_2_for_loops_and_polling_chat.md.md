# Advanced Lesson 2

#### Goal

It's annoying to have to switch back and forth between your shell and minecraft to trigger commands, right?

Let's swap our raw_input tool to be triggered off chat messages sent in minecraft instead!

#### New Concepts

In this lesson, we'll look at a new concept - a for loop!

```python
import time
while True:
    for chatpost in mc.events.pollChatPosts():
        user_command = chatpost.message
        print user_command
    time.sleep(1)
```

This code will execute the code inside the while loop once for every chat message found in the minecraft chat post since the last time we looked. By sticking this in an infinite while loop, we can actually watch all messages posted in chat, forever!


#### Challenges
- Let's rebuilt lesson 6 using this instead.
- Make a chatbot! If someone says X, your bot should reply with Y. (Look for api call needed in docs to post to chat).
- Limit it with if statement so only you can activate it, using these two items:
```
my_id = mc.getPlayerEntityId(my_player_name)
```
and
```
if chatpost.entityId == my_id:
```
- Add some more building commands to your bot, e.g. a pixel art guy