from telegram.ext import Filters,Updater,MessageHandler,CommandHandler


#Bot Token
#Needed To interact With Bot
START_TEXT='Hi, I am POKÉMON FORWARD TAG REMOVER BOT \n\nJust Forward me messages or Files and I will Anonymize the sender and Remove Forward Tag.\n\nThis bot is specially for @POKEMONMODDER\n\nThis bot is made by @PokemonModder_Owner\n\nNote :- This bot is specially for @POKEMONMODDER but all can use it.'
HELP_TEXT='Just Forward me messages or Files and I will Anonymize the sender and Remove Forward Tag.'
token="1894604868:AAGXejSDO9kAUvm2O5SSlAFvoA2h8-7L0Wk"


#Start Message
def start_text(u,c):
	u.message.reply_text(START_TEXT)
	
#Help Message
def help_text(u,c):
	u.message.reply_text(HELP_TEXT)



#Send Document From User
def frwrd_file(u,c):
	u.message.reply_document(u.message.document.file_id)
	
#Send Video From User
def frwrd_media(u,c):
	u.message.reply_video(u.message.video.file_id)
	
#Send Photo From User
def frwrd_photo(u,c):
	u.message.reply_photo(u.message.photo[-1].file_id)

#Send Text From User
def frwrd_text(u,c):
	u.message.reply_text(u.message.text)
	
#Send Sticker From User
def frwrd_sticker(u,c):
	u.message.reply_sticker(u.message.sticker.file_id)
	
#Send Voice From User
def frwrd_voice(u,c):
	u.message.reply_voice(u.message.voice.file_id)
	
	

updater=Updater(token,use_context=True)

dp=updater.dispatcher



#Filtering Commands

dp.add_handler(CommandHandler('start',start_text))

dp.add_handler(CommandHandler('help',help_text))

#Filtering Files
dp.add_handler(MessageHandler(Filters.document,frwrd_file))

#Filtering Media
dp.add_handler(MessageHandler(Filters.video,frwrd_media))

#Filtering Photos
dp.add_handler(MessageHandler(Filters.photo,frwrd_photo))

#Filtering Text
dp.add_handler(MessageHandler(Filters.text,frwrd_text))

#Filtering Stickers
dp.add_handler(MessageHandler(Filters.sticker,frwrd_sticker))

#Filtering Voice
dp.add_handler(MessageHandler(Filters.voice,frwrd_voice))



updater.start_polling()

updater.idle()