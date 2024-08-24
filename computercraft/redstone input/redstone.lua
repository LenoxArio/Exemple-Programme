while true do --boucle infinit
    local rear = rs.getAnalogInput("back") --emplacement de la redstone (derrière)
    if rear == 15 then --si le niveau de redstone est à 15 (valeur max) alors
        print("hello") --écrire hello dans la console
        sleep(0.1) --attendre 0.1s
    end
end
