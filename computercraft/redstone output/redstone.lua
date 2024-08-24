while true do
    redstone.setOutput("back", 15) --envoyer à l'arrière de l'odinateur un signal de 15 de puissance de redstone (on)
    sleep(1)
    redstone.setOutput("back", 0)  --envoyer à l'arrière de l'odinateur un signal de 0 de puissance de redstone (off)
    sleep(1)

end