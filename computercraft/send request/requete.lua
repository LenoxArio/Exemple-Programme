-- Script Lua pour CC: Tweaked avec menu interactif
local function sendRequest(path)
    local url = "http://192.168.1.100:80" .. path
    local response = http.get(url)

    if response then
        print("Requête envoyée avec succès : " .. path)
        response.close()
    else
        print("Échec de l'envoi de la requête : " .. path)
    end
end

while true do
    print("Menu:")
    print("1. Allumer la LED")
    print("2. Éteindre la LED")
    print("3. Quitter")
    local choice = read()

    if choice == "1" then
        sendRequest("/lighton?")
    elseif choice == "2" then
        sendRequest("/lightoff?")
    elseif choice == "3" then
        break
    else
        print("Choix invalide, veuillez réessayer.")
    end
end
