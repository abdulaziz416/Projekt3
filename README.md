# Projekt3
Jag började projektet med att skapa backend-delen med en FastAPI-baserad struktur. Backend är asynkron och använder Motor som MongoDB-driver. I main.py definieras FastAPI-applikationen samt API-endpoints för att lista, skapa och ta bort nyårslöften. För datavalidering och request-modeller används Pydantic via BaseModel.

Anslutningen till MongoDB hanteras i database.py. Där används AsyncIOMotorClient för att skapa en asynkron klient, och databas samt collection initieras vid applikationens start. Konfigurationsvärden som MongoDB-URI, databasnamn och collection-namn läses in från .env med hjälp av python-dotenv. Vid nedstängning av applikationen stängs databasanslutningen korrekt.

Backend är även konfigurerad med CORS-middleware för att tillåta anrop från frontend som körs lokalt via Vite.

Efter backend fortsatte jag med frontend-delen som är byggd med Vue och Vite. Frontend-koden ligger i frontend/src där App.vue fungerar som huvudkomponent och main.js startar applikationen. Kommunikation med backend sker via en separat api.js-fil som ansvarar för HTTP-anrop mot FastAPI-API:t. Projektet är uppdelat i komponenter och statiska resurser för att hålla strukturen tydlig och lätt att vidareutveckla.

Tillsammans bildar backend och frontend en enkel fullstack-applikation där användaren kan lista, skapa och ta bort nyårslöften via ett REST-API.
