import os
os.system('cls')

from telegram.ext import ApplicationBuilder, CommandHandler
from bot_commands import *

app = ApplicationBuilder().token("6199884361:AAEBc9DbG8_IvC64-69I0YffAIEeyfCby-Q").build()

app.add_handler(CommandHandler("start", start_command))
app.add_handler(CommandHandler("time", time_command))
app.add_handler(CommandHandler("new_year", new_year_command))
app.add_handler(CommandHandler("exit", exit_command))

print('server start')
app.run_polling()

