# Lesson 4 notes

#### Goal
Make a pyramid with layers

#### Code
Open up script.py in a code editor. Delete everything in it, we'll be starting from scratch!

```python
import mcpi.minecraft as minecraft
mc = minecraft.Minecraft.create(address="199.96.85.3", name="seanybob")
```
The first 2 lines are similar to the previous lesson. Be sure to replace "seanybob" with your name!

```
# Hint: Instead of thinking of the pyramid as one building, think of every layer of the pyramid as a separate building that is only 1 block high.

block = 24
# This is the block id for sandstone, which is good for a pyramid. 

#Get the player's current position so we can build the pyramid there.
pos = mc.player.getPos()
x = pos.x
y = pos.y
z = pos.z

x2 = x + 8 #Make it 8 blocks wide.
# y2 = y 
z2 = z + 8 #Make it 8 blocks long.

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

######CHALLENGES 
- Make the pyramid hollow inside (just talk it through, don't do it)
- Make a house with a pyramid-like roof on top of it
- Make code that builds a giant tree (using wood and leaf blocks)