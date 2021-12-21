

from pyrogram import Client, filters

TOKEN = "5097104342:AAEuKw3O5TekOID2qabNOj2y-SOmTOzQX9c"



app = Client(
        "mytester",
        bot_token=TOKEN)
        





@app.on_message(filters.private)
async def hello(client, message):
    await message.reply_text(f"Hello {message.from_user.mention}")


app.run()
