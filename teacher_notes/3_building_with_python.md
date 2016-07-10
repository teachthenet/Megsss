# Lesson 2 notes

#### Goal
Create a building programmatically

#### New Concepts

Variables can refer to each other, similar to algebra
```python
x = 10
x2 = x + 5
```
x2 now is 15

```python
mc.setBlocks(x, y, z, x2, y2, z2, block_id)
```

- There is a new function we can use called setBlocks.
- The setBlocks function takes as input the x/y/z coordinates of two opposite corners of a building.
- For example, if you were to imagine looking at your house from the street, the function would take as input the location of the bottom front right of your house AND the top back left.
- The function then sets every block inside the cuboid you defined as the block_id you passed in

#### Code
Open up script.py in a code editor. Delete everything in it, we'll be starting from scratch!

```python
import mcpi.minecraft as minecraft
mc = minecraft.Minecraft.create(address="199.96.85.3", name="seanybob")
```
The first 2 lines are similar to the previous lesson. Be sure to replace "seanybob" with your name!

```python
#Get the player's current position so we can build the pyramid there.
pos = mc.player.getPos()
x = pos.x
y = pos.y
z = pos.z
```

This position is the bottom front right of our building - let's put it where our user is standing, so we can find it easy!

```python
x2 = x + 10
y2 = y + 5
z2 = z + 8
```

- This position is the top back left of our building.
- Note that we are defining it in relationship to the x/y/z (bottom right front) of our building
- That is to say, the top back left's x value is the bottom right front's x value + 10.

```python
block_id = 4
```
This is the block id for cobbestone. Swap it to a different block ID if you'd like from [here](http://minecraft-ids.grahamedgecombe.com/).

```python
mc.setBlocks(x, y, z, x2, y2, z2, block_id)
```
The result of the above should give us a building that is 10 blocks by 5 blocks by 8 blocks

#### Terminal

Run the script like so:
```shell
python script.py
```

# CHALLENGES to do together

- Modify the script above, and change the block used to build the building
- Make the building twice as tall.
- Make it hollow:
```python
mystery_block_id = 0
mc.setBlocks(x+1, y+1, z+1, x2-1, y2-1, z2-1, mystery_block_id)
```
- Make a pyramid with layers

# Hint: Instead of thinking of the pyramid as one building, think of every layer of the pyramid as a separate building that is only 1 block high.

block = 24
# This is the block id for sandstone, which is good for a pyramid. Swap it to a different block ID if you'd like from [here](http://minecraft-ids.grahamedgecombe.com/).

#Get the player's current position so we can build the pyramid there.
pos = mc.player.getPos()
x = pos.x
y = pos.y
z = pos.z

x2 = x + 8 #Make it 8 blocks wide.
y2 = y + 0 #Make it only one block high, so don't add anything here.
z2 = z + 8 #Make it 8 blocks long.

mc.setBlocks(x, y, z, x2, y2, z2, block)

x = pos.x + 1
y = pos.y + 1 
z = pos.z + 1

x2 = x + 6 
z2 = z + 6 

mc.setBlocks(x, y, z, x2, y2, z2, block)

x = pos.x+2
y = pos.y+2 
z = pos.z+2

x2 = x + 4 
z2 = z + 4 

mc.setBlocks(x, y, z, x2, y2, z2, block)

x = pos.x + 3
y = pos.y + 3
z = pos.z + 3

x2 = x + 2
z2 = z + 2 

mc.setBlocks(x, y, z, x2, y2, z2, block)

x = pos.x + 4
y = pos.y + 4
z = pos.z + 4

x2 = x + 0
z2 = z + 0 

mc.setBlocks(x, y, z, x2, y2, z2, block)

######CHALLENGES FOR KIDS
- Make a swimming pool
- Make a house with a pyramid-like roof on top of it