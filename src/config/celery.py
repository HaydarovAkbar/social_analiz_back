import sys

sys.dont_write_bytecode = True

import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
import django

django.setup()
from decouple import config

import logging

TOKEN = config('TOKEN')

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

from methods.core.views import start, followers, sale_product, get_category, get_capacity, get_capacity_product, \
    get_color, get_memory, get_document, get_country, get_status, send_admin, change_language, choose_language, \
    report_admin, get_report
from methods.admin.views import admin, add_admin, get_admin_id, get_admins, delete_admin, get_users, add_data, get_data, \
    add_channel, get_channel_name, get_channel_url, get_channel_id, get_channels, delete_channel, get_reklama, \
    send_reklama

from methods.admin.message import KeyboardsAdmin as bt
from methods.core.texts import KeyboardsTexts as msg_txt

from states import States as st

from telegram.ext import CallbackContext, CommandHandler, ConversationHandler, MessageHandler, Filters, \
    CallbackQueryHandler, Updater

updater = Updater(token=TOKEN, use_context=True, workers=5000)

dispatcher = updater.dispatcher

all_handlers = ConversationHandler(
    entry_points=[
        CommandHandler('start', start),
        CommandHandler('admin', admin)],
    states={},
    fallbacks=[
        MessageHandler(Filters.all, start),
    ]
)

dispatcher.add_handler(all_handlers)
updater.start_polling()
updater.idle()
print('Bot is running...')
