# import telebot
# import os
# import logging
# import importlib
# import importlib.util
# import sys
# from Model import storage

# logger = telebot.logger

# telebot.logger.setLevel(logging.INFO)
# API_TOKEN = os.environ.get("API_TOKEN")
# bot = telebot.TeleBot(API_TOKEN)

# sys.path.append(os.path.dirname(__file__))

# handlers_dir = os.path.join(os.path.dirname(__file__), 'handlers')

# for file in os.listdir(handlers_dir):
#     if file.endswith(".py") and file != "__init__.py":
#         module_name = f"handlers.{file[:-3]}"
#         spec = importlib.util.spec_from_file_location(module_name, os.path.join(handlers_dir, file))
#         module = importlib.util.module_from_spec(spec)
#         sys.modules[module_name] = module
#         spec.loader.exec_module(module)
#         if hasattr(module, 'register'):
#             module.register(bot)

# bot.infinity_polling()


import os
import sys
import importlib.util
from bale import Bot, Message

# Set your bot token
API_TOKEN = "906990267:lHfQAoo3mPnb32X9Q9v7cuwqyIuOHTt1dIGbAh3u"
bot = Bot(token=API_TOKEN)

# Dynamically load handlers from the 'handlers' directory
sys.path.append(os.path.dirname(__file__))
handlers_dir = os.path.join(os.path.dirname(__file__), "handlers")

if os.path.exists(handlers_dir):
    for file in os.listdir(handlers_dir):
        if file.endswith(".py") and file != "__init__.py":
            module_name = f"handlers.{file[:-3]}"
            module_path = os.path.join(handlers_dir, file)
            
            spec = importlib.util.spec_from_file_location(module_name, module_path)
            module = importlib.util.module_from_spec(spec)
            sys.modules[module_name] = module
            spec.loader.exec_module(module)
            
            if hasattr(module, "register"):
                module.register(bot)

# Start the bot
bot.run()
