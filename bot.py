
# bot.py

from telegram import Bot, Update
from telegram.ext import CommandHandler, Updater

# Replace with your bot token
TOKEN = '7825267743:AAF4LLHMD7Q8lhy9wRfpE0oFB2f9i7qPbZY'

# Replace with your source and target group chat IDs
SOURCE_GROUP_ID = '-1002167342551'
TARGET_GROUP_ID = '-1002043570167'

def transfer_members(update: Update, context):
    bot = context.bot
    source_members = bot.get_chat_administrators(SOURCE_GROUP_ID)

    for member in source_members:
        try:
            bot.add_chat_member(TARGET_GROUP_ID, member.user.id)
            update.message.reply_text(f"Added {member.user.username}")
        except Exception as e:
            update.message.reply_text(f"Failed to add {member.user.username}: {e}")

def start(update: Update, context):
    update.message.reply_text("Send /transfer to transfer members")

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('transfer', transfer_members))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
