from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from bot_commands import *
import datetime
from spy import *






async def hi_command(update: Update, context: ContextTypes.DEFAULT_TYPE) :
    log(update, context)
    await update.message.reply_text(f'hi {update.effective_user.first_name}')

async def time_command(update: Update, context: ContextTypes.DEFAULT_TYPE) :
    log(update, context)
    await update.message.reply_text(f'time {datetime.datetime.now().time()}')

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) :
    log(update, context)
    await update.message.reply_text(f'/hi\n/time\n/help\n/sum')

async def sum_command(update: Update, context: ContextTypes.DEFAULT_TYPE) :
    log(update, context)
    msg = update.message.text
    print(msg)
    items = msg.split()
    x = int(items[1])
    y = int(items[2])
    await update.message.reply_text(f'{x}+{y} = {x+y}')



async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE) :
    log(update, context)
    await update.message.reply_text(f'Я приветствую ВАС!!! {update.effective_user.first_name}')
    await update.message.reply_text(f'/hi\n/time\n/help\n/sum')









