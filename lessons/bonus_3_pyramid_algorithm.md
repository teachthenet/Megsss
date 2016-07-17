# Lesson 8 notes

#### Goal
In this lesson, we're going to take the pyramid we created in lesson 4,
   and write an algorithm that will let us dynamically create it any size!
   To do this, look back at lesson 4, and see if you can detect a pattern in the numbers
   and how they change between each layer.

#### New Concepts

We have another new construct, another use of the for loop!

For loops are used to repeat some code a set number of times.

A for loop looks similar to a while loop. Observe the example below, where we print the numbers 0 through 4.

```python
for i in range(5):
    print i
```

Note three things.

- First, you can change the number 5 to make it loop a different number of times.
- Second, the current # of the loop is saved in a variable called "i", which you can access in the loop - observe how we are printing that variable out!
- Third, note that it printed the numbers 0-4 (instead of 1-5)! This is because computers start counting from the number 0, instead of the number 1 like humans tend to. So by telling it you want a for loop with range(5), you are saying give me 5 iterations or numbers - which is 0 through 4!

#### Code
Open up script.py in a code editor. Delete everything in it, we'll be starting from scratch!

Start with the code from lesson 4:
```
import mcpi.minecraft as minecraft
mc = minecraft.Minecraft.create(address="199.96.85.3", name="seanybob")

block = 24
# This is the block id for sandstone, which is good for a pyramid. 

#Get the player's current position so we can build the pyramid there.
pos = mc.player.getPos()
x = pos.x
y = pos.y
z = pos.z

x2 = x + 8 #Make it 9 blocks wide.
z2 = z + 8 #Make it 9 blocks long.

mc.setBlocks(x, y, z, x2, y, z2, block)

x = pos.x + 1
y = pos.y + 1 
z = pos.z + 1

x2 = x + 6 
z2 = z + 6 

mc.setBlocks(x, y, z, x2, y, z2, block)

x = pos.x+2
y = pos.y+2 
z = pos.z+2

x2 = x + 4 
z2 = z + 4 

mc.setBlocks(x, y, z, x2, y, z2, block)

x = pos.x + 3
y = pos.y + 3
z = pos.z + 3

x2 = x + 2
z2 = z + 2 

mc.setBlocks(x, y, z, x2, y, z2, block)

x = pos.x + 4
y = pos.y + 4
z = pos.z + 4

x2 = x + 0
z2 = z + 0 

mc.setBlocks(x, y, z, x2, y, z2, block)
```

Do you notice any patterns with the above code? Let's condense the code into a for loop and put question marks in the spots the patterns change.

```python
block = 24
# This is the block id for sandstone, which is good for a pyramid. 

#Get the player's current position so we can build the pyramid there.
pos = mc.player.getPos()

for i in range(5):
    x = pos.x + ?
    y = pos.y + ?
    z = pos.z + ?

    x2 = x + ?
    z2 = z + ?
    mc.setBlocks(x, y, z, x2, y, z2, block)
```
This is the foundation of your algorithm! We are going to create 5 layers in our pyramid, and thus loop through this code 5 times.

Note that the algorithm is not complete, we need to fill in the question marks!

Note that the variable "i" will be replaced with the current iteration of our while loop (starting with 0 and going up to 4).

```python
block = 24
# This is the block id for sandstone, which is good for a pyramid. 

#Get the player's current position so we can build the pyramid there.
pos = mc.player.getPos()

for i in range(5):
    x = pos.x + i
    y = pos.y + i
    z = pos.z + i

    x2 = x + ?
    z2 = z + ?
    mc.setBlocks(x, y, z, x2, y, z2, block)
```

The first part of the algorithm simple uses i as it is, incrementing by one each loop. But what about the second part?

```python
block = 24
# This is the block id for sandstone, which is good for a pyramid. 

#Get the player's current position so we can build the pyramid there.
pos = mc.player.getPos()

for i in range(5):
    x = pos.x + i
    y = pos.y + i
    z = pos.z + i

    x2 = x + 8 - (i*2)
    z2 = z + 8 - (i*2)
    mc.setBlocks(x, y, z, x2, y, z2, block)
```

Ah, so it's the max size minus i * 2 (since we decrease in width 2 blocks with each layer higher)

# CHALLENGES

- Change the "5" in range(5) to a slightly larger number, like 10. CAREFUL! If you go too high, you'll crash the server! Keep it under 15 to be kind to your neighbors. What happens? (inverted pyramid)

- The above happened because we limit the max base size to 8 in the algorithm (see x2 and z2) what happens if you increase the 8 there?

- What is the relationship between the number of rows in the pyramid, and the width in blocks of the bottom layer? Can we codify that into our algorithm?


```
import mcpi.minecraft as minecraft

#NOTE - replace "seanybob" below with your name
mc = minecraft.Minecraft.create(address="199.96.85.3", name="seanybob")

block = 24
# This is the block id for sandstone, which is good for a pyramid. 

#Get the player's current position so we can build the pyramid there.
pos = mc.player.getPos()

size_of_pyramid = 15

for i in range(size_of_pyramid):
    x = pos.x + i
    y = pos.y + i
    z = pos.z + i

    x2 = x + (size_of_pyramid*2) - 2 - (i*2)
    z2 = z + (size_of_pyramid*2) - 2 - (i*2)
    mc.setBlocks(x, y, z, x2, y, z2, block)
```

- Can you modify the script to make a second, one block smaller pyramid of air inside the first pyramid (effectively making the pyramid hollow)?
