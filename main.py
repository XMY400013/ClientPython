from pyrogram import Client, filters
from Code_parse import parse_text

App = Client(
    session_name="Xm4000",
    workdir='Sessions'
)

@App.on_message(filters.text)
def text(Client, message):

    if message.from_user.id == 1481888673 :

        if text:= parse_text(message.text):

                App.send_message(
                    chat_id=message.chat.id,
                    text=text,
                    parse_mode='html'
                )

App.run()
