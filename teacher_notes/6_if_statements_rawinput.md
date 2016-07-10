# Lesson 6 notes

#### Goal

In this lesson, we'll be setting up a building toolkit!

#### Code
Open up script.py in a code editor. Delete everything in it, we'll be starting from scratch!

```python
import mcpi.minecraft as minecraft
mc = minecraft.Minecraft.create(address="199.96.85.3", name="seanybob")
```
The first 2 lines are similar to the previous lesson. Be sure to replace "seanybob" with your name!

Remeber raw_input() from earlier? Let's use that to craft a dynamic building toolkit! To do so, we're going to learn a new construct called if statements.

```python
user_command = raw_input("Enter command: ")
if user_command == "diamond":
    diamond_block_id = 56
    mc.setBlock(x, y-1, z, diamond_block_id)
if user_command == "gold":
    gold_block_id = 14
    mc.setBlock(x, y-1, z, gold_block_id)
```

So now when we run this script, we wait for user input, then execute the command the user specified. See how the indentation works? The code inside the if statement only gets executed if it matches what the user typed in. The double equals sign is an equality operator, testing if things are equal.

Let's write a command to build a pillar at the user's location.
```python
user_command = raw_input("Enter command: ")
if user_command == "pillar":
    pos = mc.player.getPos()
    x = pos.x
    y = pos.y
    z = pos.z
    
    x2 = x + 1 #Make it 1 block wide.
    y2 = y + 8 #Make it 8 blocks high
    z2 = z + 1 #Make it 1 block long.
    
    mc.setBlocks(x, y, z, x2, y2, z2, 4)
if user_command == "building":
    pos = mc.player.getPos()
    x = pos.x
    y = pos.y
    z = pos.z
    x2 = x + 8
    y2 = y + 5
    z2 = z + 8
    mc.setBlocks(x, y, z, x2, y2, z2, 4)
```

Sweet! Now we have a mini-rcon like tool. It's not very fun to have to execute it each time though. What if we wrap it in a while True: loop?

```python
while True:
    user_command = raw_input("Enter command: ")
    if user_command == "pillar":
        pos = mc.player.getPos()
        ...
```

# Challenges
- Use this to craft a building toolkit of particular things you want to build many of.