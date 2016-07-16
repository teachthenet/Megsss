# Lesson 2 notes

#### Goal
Teleport your character to a point you define in code.

#### Print your x/y/z location
```python
import mcpi.minecraft as minecraft
mc = minecraft.Minecraft.create(address="199.96.85.3", name="seanybob")
#Replace "seanybob" with your name above

my_pos = mc.player.getPos()
print(my_pos)
```


#### Teleport Script 

```python
import mcpi.minecraft as minecraft
mc = minecraft.Minecraft.create(address="199.96.85.3", name="seanybob")
#Replace "seanybob" with your name above

x = 52
y = 52
z = -57

mc.player.setPos(x, y, z)
```

#### CHALLENGE

- Use the first script to get the X/Y/Z location of your home
- Use the second script to teleport back to your home

#### Things to think about

- Which parameter (x/y/z) controls the height?



