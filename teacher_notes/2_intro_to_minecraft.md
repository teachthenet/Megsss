# Lesson 2 notes

#### Goal
Teleport your character to a point you define in code.


#### Code 
Open up script.py in a code editor. We'll be going through this file line-by-line to start with.

```python
import mcpi.minecraft as minecraft
```
This first line imports the mcpi.minecraft library, making it available under the name 'minecraft'

-----------------

```python
#NOTE - replace "seanybob" below with your name
mc = minecraft.Minecraft.create(address="199.96.85.3", name="seanybob")
```

- Anything prefixed by the '#' symbol is a comment for humans, and is ignored by the computer.
- Here we see we are creating a connection to the minecraft server and storing it in a variable named "mc".
- The server we are connecting to is located at IP address 127.0.0.1 and linking to the login name "seanybob".
- As mentioned in the comment above it, you need to change "seanybob" to your minecraft name that you chose.

-----------------

```python
x = 52
y = 52
z = -57
```

- Here we are creating 3 variables for later use.
- In the variable named 'x', we are storing the number 52.
- In the variable named 'y', we are storing the number 52.
- In the variable named 'z', we are storing the number -57.

-----------------

```python
mc.player.setPos(x, y, z)
```

- Using our connection to our minecraft server (we previously saved the connection to the mc variable)...
- We will access our player object inside that minecraft server...
- And then set our position in the minecraft server to the x/y/z coordinates indicated by the variables we just set earlier.

The variables in the call get replaced, essentially turning into the values we stored in them earlier: 

mc.player.setPos(52, 52, -57)


#### Terminal

To execute the script, in your terminal cd to the directory the script is located:
```shell
cd ~/TeachCraft-Challenges
```

Then run the script like so:
```shell
python script.py
```

Each time you edit the code, you will need save it and then re-run the script using the above command.

----------------------

# CHALLENGES

- Modify the script to go to a different x/y/z location.
- Figure out which of the three coordinates (x, y, or z) controls how high up you are in the air.
- Review API reference sheet (link below), observe function .setBlock(x, y, z, block)
- Use it to give us a block to stand on when we teleport.
- Everyone choose a teleport location. This will be your "secret" location in the world where you will be building things. Share it with others if you'd like them to come build with you, or to just see what you've built. This is how you can protect yourself against griefing (think of it like a password)

some_block_id = 4
mc.setBlock(x, y-1, z, some_block_id)

http://www.stuffaboutcode.com/p/minecraft-api-reference.html



