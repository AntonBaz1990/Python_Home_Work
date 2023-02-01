from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from bot_commands import *
from spy import *


app = ApplicationBuilder().token("6199884361:AAEBc9DbG8_IvC64-69I0YffAIEeyfCby-Q").build()

app.add_handler(CommandHandler("hi", hi_command))
app.add_handler(CommandHandler("time", time_command))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("sum", sum_command))
app.add_handler(CommandHandler("start", start_command))


print('server start')
app.run_polling()
app.idle()








# from isOdd import isOdd

# print(isOdd(1)) 
# print(isOdd(4)) 


 


# import time
# from progress.bar import Bar

# bar = Bar('Processing', max=20)
# for i in range(20):
#     # Do some work
#     time.sleep(1)
#     bar.next()
# bar.finish()




# import emoji
# print(emoji.emojize('Python is :thumbs_up:'))







# import matplotlib.pyplot as plt
# import numpy as np

# Fixing random state for reproducibility
# np.random.seed(19680801)

# plt.rcdefaults()
# fig, ax = plt.subplots()

# # Example data
# people = ('Tom', 'Dick', 'Harry', 'Slim', 'Jim')
# y_pos = np.arange(len(people))
# performance = 3 + 10 * np.random.rand(len(people))
# error = np.random.rand(len(people))

# ax.barh(y_pos, performance, xerr=error, align='center')
# ax.set_yticks(y_pos, labels=people)
# ax.invert_yaxis()  # labels read top-to-bottom
# ax.set_xlabel('Performance')
# ax.set_title('How fast do you want to go today?')

# list = [1, 2, 3, 2, 7]
# plt.plot(list)

# plt.show()