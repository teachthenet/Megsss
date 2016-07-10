```python
from mcpi import minecraft
import rcon_mc.rcon
import rcon_mc.lib.msocket

server_address = "199.96.85.3"
rcon_port = 25575
rcon_password = "???" #Ask the instructor for this password
raspberry_juice_port = 4711
my_player_name = "seanybob"

mc = minecraft.Minecraft.create(address=server_address, name=my_player_name)
rcon = rcon_mc.rcon.client(server_address, rcon_port, rcon_password)

rcon.send('scoreboard objectives add ID dummy')

#Grant player bows to trigger spells

#Spell:Teleport
rcon.send('give '+my_player_name+' minecraft:bow 1 0 {display:{Name:"Spell:Teleport",Lore:["Teleport to target location."]},ench:[{id:51,lvl:1},{id:34,lvl:100},{id:48,lvl:3}]}')

#Give player arrows to use with the bow
rcon.send('give '+my_player_name+' minecraft:arrow 1 0')

#Watch for spellcasts
while True:

    try:

        #Any arrows fired from the Teleport bow?
        rcon.send('scoreboard players set @e[type=Arrow] ID 3 {damage:4.0}') #Power 3 Enchantment
        response = rcon.send("testfor @e[type=Arrow,score_ID_min=3,score_ID=3]")
        if "Found Arrow" in response:
            orientation_y = mc.player.getRotation()
            orientation_x = mc.player.getPitch()
            if orientation_y < -180:
                orientation_y += 360
            if orientation_y > 180:
                orientation_y -= 360
            #effect <player> <effect> [seconds] [amplifier] [hideParticles]
            rcon.send("effect "+my_player_name+" minecraft:blindness 3 10 true")
            rcon.send("tp "+my_player_name+" @e[type=Arrow,score_ID_min=3,score_ID=3]")
            rcon.send("tp "+my_player_name+" ~ ~ ~ "+str(orientation_y)+" "+str(orientation_x))
            rcon.send("effect "+my_player_name+" clear")

        #Then remove the arrow.
        rcon.send("kill @e[type=Arrow,score_ID_min=1]")

    except:
        #if any errors occur from the server, ignore them
        pass



#CHALLENGE 1
# What other cool things can you do with this? Consider other effects you can apply based on an arrow, do some googling and find something cool, then build it!
