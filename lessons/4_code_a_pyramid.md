# Lesson 4 notes

#### Goal
Make a pyramid with layers

#### Code
```python
import mcpi.minecraft as minecraft
mc = minecraft.Minecraft.create(address="199.96.85.3", name="seanybob")

# Hint: Instead of thinking of the pyramid as one building, think of every layer of the pyramid as a separate building that is only 1 block high.

block = 24

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

x = pos.x + 2
y = pos.y + 2 
z = pos.z + 2

x2 = x + 4 
z2 = z + 4 

mc.setBlocks(x, y, z, x2, y, z2, block)


```

######CHALLENGES 
- Finish the pyramid!