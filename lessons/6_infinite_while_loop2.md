# Lesson 6 notes

### Eraser
```
import time
import mcpi.minecraft as minecraft
mc = minecraft.Minecraft.create(address="199.96.85.3", name="seanybob")

while True:

    pos = mc.player.getPos()
    x = pos.x
    y = pos.y
    z = pos.z
    
    x2 = x + 4
    y2 = y + 4
    z2 = z + 4
    
    
    block = 0
    mc.setBlocks(x, y, z, x2, y2, z2, block)
    
    time.sleep(0.1)
```

### Building walls
```
import time
import mcpi.minecraft as minecraft
mc = minecraft.Minecraft.create(address="199.96.85.3", name="seanybob")

while True:

    pos = mc.player.getPos()
    x = pos.x + 1
    y = pos.y
    z = pos.z + 1
    
    x2 = x
    y2 = y + 8
    z2 = z
    
    
    block = 24
    mc.setBlocks(x, y, z, x2, y2, z2, block)
    
    time.sleep(0.1)
```

You can stop an infinite loop with control+c in your terminal/shell.

#### CHALLENGE

- Modify the Building walls code above to built a platform that follows you instead of a wall that follows you (flat instead of tall)
