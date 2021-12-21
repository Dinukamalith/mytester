
from pyrogram import Client

app = Client("5097104342:AAEuKw3O5TekOID2qabNOj2y-SOmTOzQX9c")

with app:

    app.send_message("haskell", "hi")
    
    app.run()
