# Lesson 5 notes

#### New Concepts

Now for a new construct, an infinite while loop!

Infinite while loops are used to make a set of code execute repeatedly, over and over, until the user decides to stop it.

An infinite while loop's structure looks like this:

```python
while True:
    <execute this indented code>
    <jump back to the top of the while statement>
```

For example, will constantly print the pattern "1 2 3 1 2 3 1 2 3 1 2 3..." over and over.

```python
while True:
    print "1"
    print "2"
    print "3"
```

We can make the computer count to infinity like this:

```python
counter = 0
while True:
    counter = counter + 1
    print counter
```

We can make the computer act like a clock by counting seconds, using time.sleep to make the computer pause between each second.
```python
import time
counter = 0
while True:
    counter = counter + 1
    print counter
    time.sleep(1)
```

How to use this with minecraft? Observe.

```
import mcpi.minecraft as minecraft
mc = minecraft.Minecraft.create(address="199.96.85.3", name="seanybob")
while True:
    #Retrieve the current player's X, Y, and Z coordinates
    pos = mc.player.getPos()
    x = pos.x
    y = pos.y
    z = pos.z
    #This is the minecraft block ID of the flower block.
    block = 38
    #Set the block at the x/y/z coordinates of the current player to the block id we chose above.
    mc.setBlock(x, y, z, block)
```
    
A trail of flowers behind us! We can change this to be any block we want, of course. We could do water (to make a water slide), lava, tnt, or even railroad track to make a roller coaster. You could even do the raw materials to build a snowman behind you.

You can kill an infinite loop with control+c in your terminal/shell.


