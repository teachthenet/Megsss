# Lesson 7 notes

### Summon snowmen with a bow/arrow
```
from mcpi import minecraft
import rcon_mc.rcon
import rcon_mc.lib.msocket

server_address = "199.96.85.3"
rcon_port = 25575
rcon_password = "pycraft"
raspberry_juice_port = 4711
my_player_name = "seanybob"

mc = minecraft.Minecraft.create(address=server_address, name=my_player_name)
rcon = rcon_mc.rcon.client(server_address, rcon_port, rcon_password)

rcon.send('scoreboard objectives add ID dummy')

rcon.send('give '+my_player_name+' minecraft:bow 1 0 {display:{Name:"Spell:Snowman",Lore:["Summon a snowman."]},ench:[{id:51,lvl:1},{id:34,lvl:100},{id:48,lvl:1}]}')

while True:

    try:

        rcon.send('scoreboard players set @e[type=Arrow] ID 1 {damage:3.0}') 
        response = rcon.send("execute @e[type=Arrow,score_ID_min=1,score_ID=1] ~ ~ ~ summon SnowMan")
        rcon.send("kill @e[type=Arrow,score_ID_min=1]")

    except:
    
        pass

```

### Summon lightning bolt (incomplete)
```
from mcpi import minecraft
import rcon_mc.rcon
import rcon_mc.lib.msocket

server_address = "199.96.85.3"
rcon_port = 25575
rcon_password = "pycraft"
raspberry_juice_port = 4711
my_player_name = "seanybob"

mc = minecraft.Minecraft.create(address=server_address, name=my_player_name)
rcon = rcon_mc.rcon.client(server_address, rcon_port, rcon_password)

rcon.send('scoreboard objectives add ID dummy')

rcon.send('give '+my_player_name+' minecraft:bow 1 0 {display:{Name:"Spell:Snowman",Lore:["Summon a snowman."]},ench:[{id:51,lvl:1},{id:34,lvl:100},{id:48,lvl:2}]}')

while True:

    try:

        rcon.send('scoreboard players set @e[type=Arrow] ID 2 {damage:3.5}') 
        response = rcon.send("execute @e[type=Arrow,score_ID_min=2,score_ID=2] ~ ~ ~ summon SnowMan")
        rcon.send("kill @e[type=Arrow,score_ID_min=1]")

    except:
    
        pass

```

### Summon explosion (incomplete)
```
from mcpi import minecraft
import rcon_mc.rcon
import rcon_mc.lib.msocket

server_address = "199.96.85.3"
rcon_port = 25575
rcon_password = "pycraft"
raspberry_juice_port = 4711
my_player_name = "seanybob"

mc = minecraft.Minecraft.create(address=server_address, name=my_player_name)
rcon = rcon_mc.rcon.client(server_address, rcon_port, rcon_password)

rcon.send('scoreboard objectives add ID dummy')

rcon.send('give '+my_player_name+' minecraft:bow 1 0 {display:{Name:"Spell:Snowman",Lore:["Summon a snowman."]},ench:[{id:51,lvl:1},{id:34,lvl:100},{id:48,lvl:3}]}')

while True:

    try:

        rcon.send('scoreboard players set @e[type=Arrow] ID 3 {damage:4.0}') 
        response = rcon.send("execute @e[type=Arrow,score_ID_min=3,score_ID=3] ~ ~ ~ summon SnowMan")
        rcon.send("kill @e[type=Arrow,score_ID_min=1]")

    except:
    
        pass

```

You can stop an infinite loop with control+c in your terminal/shell.

#### CHALLENGE

- The script above called `Summon lightning bolt (incomplete)` isn't working properly! Instead of summoning a LightningBolt, it is summoning a Snowman! Fix it by updating the name and lore of the bow, and then changing `summon SnowMan` to `summon LightningBolt`.

- The script above called `Summon explosion (incomplete)` isn't working properly! Instead of summoning an explosion, it is summoning a Snowman! Fix it by updating the name and lore of the bow, and then changing `summon SnowMan` to `summon Creeper ~ ~ ~ {ignited:1,Fuse:1}`.



