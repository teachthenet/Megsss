# Lesson 5 notes

### New Concepts

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

### Flower Path in Minecraft
```
import time
import mcpi.minecraft as minecraft
mc = minecraft.Minecraft.create(address="199.96.85.3", name="seanybob")

while True:

    pos = mc.player.getPos()
    x = pos.x
    y = pos.y
    z = pos.z
    
    block = 38
    mc.setBlock(x, y, z, block)
    
    time.sleep(0.1)
```
    
A trail of flowers behind us! We can change this to be any block we want, of course. Let's change it to fire, block ID 51.

You can stop an infinite loop with control+c in your terminal/shell.

#### CHALLENGE

- Using the code above as a base, make a roller coaster! You will want to place Powered Rail, and also put redstone blocks underneath each power rail.



