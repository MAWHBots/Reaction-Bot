from os import environ as env

class Telegram:
    API_ID = int(env.get("TG_API_ID", "20763817"))
    API_HASH = env.get("TG_API_HASH", "07186e8f2ffe607e99eedf7eaa5e630b")
    BOT_TOKEN = env.get("TG_BOT_TOKEN", "6788328207:AAEnHX9si_U9SBFLQL7RM_eTKMDpOjjqc3E")
    BOT_USERNAME = env.get("TG_BOT_USERNAME", "MAWH_Emoji_Bot")
    EMOJIS = [
        "👍", "❤", "🔥", 
        "🥰", "👏", "😁", "🤔",
        "🤯", "😱", "😢",
        "🎉", "🤩", "🤮", 
        "🙏", "👌", "🕊", "🤡",
        "😍", "🐳",
        "❤‍🔥", "🌚", "💯",
        "🤣", "⚡", "🏆",
        "💔", "🤨", "😐", "🍓",
        "🍾", "💋", "😈",
        "😴", "😭", "🤓", "👻",
        "👨‍💻", "👀", "🙈",
        "😇", "😨", "🤝", "✍",
        "🤗", "🫡", "🎅", "🎄",
        "☃", "💅", "🤪", "🗿",
        "🆒", "💘", "🙉", "🦄",
        "😘", "💊", "🙊", "😎",
        "👾", "🤷‍♂", "🤷", "🤷‍♀",
        "😡"
    ]

LOGGER_CONFIG_JSON = {
    'version': 1,
    'formatters': {
        'default': {
            'format': '[%(asctime)s][%(name)s][%(levelname)s] -> %(message)s',
            'datefmt': '%d/%m/%Y %H:%M:%S'
        },
    },
    'handlers': {
        'file_handler': {
            'class': 'logging.FileHandler',
            'filename': 'event-log.txt',
            'formatter': 'default'
        },
        'stream_handler': {
            'class': 'logging.StreamHandler',
            'formatter': 'default'
        }
    },
    'loggers': {
        'bot': {
            'level': 'INFO',
            'handlers': ['file_handler', 'stream_handler']
        },
        'pyrogram': {
            'level': 'INFO',
            'handlers': ['file_handler', 'stream_handler']
        }
    }
}
