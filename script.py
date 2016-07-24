import mcpi.minecraft as minecraft
mc = minecraft.Minecraft.create(address="199.96.85.3", name="seanybob")
#Replace "seanybob" with your name above

my_pos = mc.player.getPos()
print(my_pos)
