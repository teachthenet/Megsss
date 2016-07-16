# Lesson 3 notes

#### Goal
Create a building programmatically

#### Solid Cobblestone Building
```python
import mcpi.minecraft as minecraft
mc = minecraft.Minecraft.create(address="199.96.85.3", name="seanybob")

pos = mc.player.getPos()
x = pos.x
y = pos.y
z = pos.z

x2 = x + 10
y2 = y + 5
z2 = z + 8

block_id = 4

mc.setBlocks(x, y, z, x2, y2, z2, block_id)
```

#### Hollow Cobblestone Building
```python
import mcpi.minecraft as minecraft
mc = minecraft.Minecraft.create(address="199.96.85.3", name="seanybob")

pos = mc.player.getPos()
x = pos.x
y = pos.y
z = pos.z

x2 = x + 10
y2 = y + 5
z2 = z + 8

block_id = 4
mc.setBlocks(x, y, z, x2, y2, z2, block_id)

air_block_id = 0
mc.setBlocks(x+1, y+1, z+1, x2-1, y2-1, z2-1, air_block_id)
```

#### CHALLENGE

- Using the code above as a base, make a swimming pool. You'll need a third layer of blocks on top made out of air to make the top of the swimming pool open.

#### Things to think about

- Why build this in code? Can't we build it faster by hand? Because... scaling: Make the building twice as tall.
- If you make the swimming pool in the sky, you can simulate rain by removing and replacing a block in the bottom of it every 2 seconds.