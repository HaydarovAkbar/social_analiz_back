import requests
from datetime import datetime, timedelta
from django.conf import settings


def tg_parse(msg_id, channel):
    try:
        URL = f"https://t.me/{channel}/{msg_id}?embed=1&tme_mode=1"
        site = requests.get(URL)
        txt = site.text
        start_with_count = txt.find('tgme_widget_message_views')
        end_with_count = txt.index('span', start_with_count, start_with_count + 500)
        start_with_time = txt.find('datetime')
        end_with_time = txt.index('datetime', start_with_time + 20, start_with_time + 100)

        count_v = {'K': 1000, "M": 1000000}
        view_count = txt[start_with_count + 27:end_with_count - 2]
        for key, value in count_v.items():
            if key in view_count:
                view_count = view_count.replace(key, '')
                view_count = float(view_count) * value
                break
        view_count = int(view_count)
        post_date = txt[start_with_time + 10:end_with_time - 9]
        post_date = datetime(year=int(post_date[:4]), month=int(post_date[5:7]), day=int(post_date[8:10]))
        days = (datetime.now() - post_date).days
        if days > settings.PARSE_DATE:
            return False
        return [view_count, post_date]
    except Exception:
        return []
