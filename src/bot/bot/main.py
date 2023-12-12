from telegram import Update, Bot
from telegram.ext import Dispatcher, CommandHandler, MessageHandler, Filters, ConversationHandler, CallbackQueryHandler
from django.conf import settings
import requests
from organization.models import Organization
from social.models import SocialPost, Social, SocialTypes, SocialPostStats
from utils.models import State
from datetime import datetime
import json


def run():
    bot.set_webhook(settings.HOST + '/bot/')


bot: Bot = Bot(token=settings.TOKEN)

dispatcher = Dispatcher(bot, None)


def get_channel_members(channel_username):
    url = f"https://api.telegram.org/bot{settings.TOKEN}/getChatMembersCount?chat_id=@{channel_username}"
    with requests.get(url) as f:
        resp = json.load(f)
    return int(resp['result'])


def channel_post(update: Update, context):
    print(update.channel_post)
    channel_username = update.channel_post.chat.username
    content = update.channel_post.text if update.channel_post.caption is None else update.channel_post.caption
    social_type = SocialTypes.objects.get(name='telegram')
    post_link, msg_id = update.channel_post.link, update.channel_post.message_id
    organization_ = Organization.objects.filter(username=channel_username)
    media_group_id = str(update.channel_post.media_group_id)
    if not organization_:
        return None
    organ_id = organization_.first()
    if not (media_group_id == 'None'):
        last_message = SocialPost.objects.filter(organization=organ_id, media_group_id=media_group_id,
                                                 social_type=social_type)
        if last_message:
            return None
    post_date = datetime.now().strftime("%Y-%m-%d %H:%M")
    new_post = SocialPost.objects.create(
        url=post_link,
        post_date=post_date,
        content=content[:255],
        post_id=msg_id,
        media_group_id=media_group_id,
        social_type=social_type,
        organization=organ_id,
        state=State.objects.first()
    )
    SocialPostStats.objects.create(
        post=new_post,
        views=1,
        followers=get_channel_members(channel_username),
        social=Social.objects.get(organization=organ_id, social_type=social_type)
    )
    return True


def group_post(update: Update, context):
    message_id = update.message.message_id
    forward_from_chat = update.message.forward_from_chat
    now = datetime.now()
    chat_id = 1122
    chat_username = update.message.chat.username
    organization_id = Social.objects.filter(tg_group=chat_username).first()
    if not organization_id:
        return False
    if forward_from_chat == None and not (update.message.reply_to_message is None):
        # print("COMMENT")
        reply_to_message = update.message.reply_to_message
        reply_message_id = reply_to_message.message_id
        reply_post = get_comment_message_id(reply_message_id)
        _ = insert_comment_message_id(chat_id, message_id, '1', now, reply_post[5], organization_id[0])
        update_post_stats(reply_post[5])
    else:
        # print("POST")
        channel_username = forward_from_chat.username
        forward_from_message_id = update.message.forward_from_message_id
        organization = get_organization_with_username(channel_username)
        post = get_last_post_with_message_id(organization[0], forward_from_message_id)
        _ = insert_comment_message_id(chat_id, message_id, '1', now, post[0], organization_id[0])
        return True


def message(update: Update, context):
    channel_msg = update.channel_post
    if channel_msg:
        return channel_post(update, context)
    else:
        return group_post(update, context)


all_handler = MessageHandler(Filters.all, message)
dispatcher.add_handler(all_handler)
