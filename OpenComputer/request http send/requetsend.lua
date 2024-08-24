local component = require("component")
local internet = require("internet")

local url = "http://example.com"
local reponse = ""

local result, reponse = pcall(internet.request, url)

if result then
    for chunk in reponse do
        print(chunk)
    end
else
    print("erreur de la requête")
end
