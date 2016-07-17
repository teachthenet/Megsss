# Lesson 5 notes

### Building a maze with single pillar walls
```
import time
import mcpi.minecraft as minecraft
mc = minecraft.Minecraft.create(address="199.96.85.3", name="seanybob")

while True:

    pos = mc.player.getPos()
    x = pos.x + 1
    y = pos.y
    z = pos.z + 1
    
    block = 24
    mc.setBlocks(x, y, z, x, y+8, z, block)
    
    time.sleep(0.1)
```

You can stop an infinite loop with control+c in your terminal/shell.

#### CHALLENGE

- Modify the code above to build an eraser instead of a pillar. The eraser should clear out the space in front of you, turning it into air (so you can punch a hole through a mountain for a rail track, for example.)
