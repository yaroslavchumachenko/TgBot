from telegram.ext import Updater, CommandHandler, MessageHandler, filters, Application, ContextTypes
from asyncio import Queue
from telegram import ForceReply, Update

my_queue = Queue()

# updater = Updater(bot=bot, update_queue=my_queue)

# updater = Updater("6464744415:AAE3CGNe4wZecrQ9DUMTlzC7E-zWJ-vjXkA", update_queue=my_queue)
# dispatcher = updater.dispatcher


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user
    await update.message.reply_html(
        rf"Hi {user.mention_html()}!",
        reply_markup=ForceReply(selective=True),
    )


# def echo(update, context):
#     context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)

# start_handler = CommandHandler('start', start)
# dispatcher.add_handler(start_handler)

application = Application.builder().token("6464744415:AAE3CGNe4wZecrQ9DUMTlzC7E-zWJ-vjXkA").build()
application.add_handler(CommandHandler("start", start))

# message_handler = MessageHandler(filters.text & ~filters.command, echo)
# dispatcher.add_handler(message_handler)

# application.run_polling()
application.run_polling(allowed_updates=Update.ALL_TYPES)
# application.idle()