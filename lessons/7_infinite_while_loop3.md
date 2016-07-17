# Lesson 7 notes

### Summon snowmen, and wipe them out with
#execute @e[type=Arrow] ~ ~ ~ execute @e[r=50] ~ ~ ~ summon LightningBolt
#execute @e[type=Arrow] ~ ~ ~ summon Creeper ~ ~ ~ {ignited:1,Fuse:1}
```
import time
import mcpi.minecraft as minecraft
mc = minecraft.Minecraft.create(address="199.96.85.3", name="seanybob")

while True:

    pos = mc.player.getPos()
    x = pos.x + 5
    y = pos.y
    z = pos.z + 5
    
    block = 24
    mc.setBlocks(x, y, z, x, y+8, z, block)
    
    time.sleep(0.1)
```

You can stop an infinite loop with control+c in your terminal/shell.

#### CHALLENGE

- Snowman



