import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = int(getenv("API_ID", "28294093"))
API_HASH = getenv("API_HASH", "f24d982c45ab2f69a6cb8c0fee9630bd")

# Get your token from @BotFather on Telegram.
BOT_TOKEN = getenv("BOT_TOKEN", "7569306898:AAHYH63zVYJtl_qIw31Lvs87wXu69c3127I")

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://Riya9797:Riyamusiczxbot@cluster0.eyy5z.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 20000))

# Chat id of a group for logging bot's activities
LOGGER_ID = int(getenv("LOGGER_ID", -1002302799359))

# Get this value from @purvi_music_bot on Telegram by /id
OWNER_ID = int(getenv("OWNER_ID", 8142003954))

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/ifgovtjoftibcdjpvd8nfiokbfobffob0vrb8bd/mtv",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

API_URL = getenv("API_URL", 'https://api.thequickearn.xyz') #youtube song url
API_KEY = getenv("API_KEY", None) # youtube song api key, generate free key or buy paid plan from panel.thequickearn.xyz
COOKIES_URL=getenv("COOKIES_URL" , "https://gist.githubusercontent.com/sparrow9616/f29fc6588086a3c72d92dd9c03773350/raw/4229f3f4aab4a6693fc0794d136d30f54d67ae85/gistfile1.txt")

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/riya_network")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/Kittusupport")

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))


# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))


# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 1073741824))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from @king_string_session_bot on Telegram
STRING1 = getenv("STRING_SESSION", "BQGvu80AFK9sNjc9-kC9oAfpGJ9gif149I8z9RfqwreO8vUb0IsIQKJnxuNzEg6bwwNj5Nq5XpDMZYBnUxS1_IuggrTno-aZ_Hl2hzxCMu9BWe8mtGn3RLwvhWYap_FUGwTjsYkEvPd7f0YhnjXyBmDj5_PT-XtJQIym9k_kj_abjrtFOQRP1OxVjlAL9xJOLF7Z-uXFQxh7tg_3ItKU17g7scnP7fIz0SpDjGEkbNRR3-oHQRyEwoXArjqS-el1Yf5CMo_MAGKkik7BL2gRY2ODXrOP3Sqk1DhtaJF_7iKgmJIfoKjeaw-I7PE-ZLg9po5PhMs60lM5N1CjfCh3C_Q9uGftSAAAAAHKXA1NAA")
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL = getenv(
    "START_IMG_URL", "https://files.catbox.moe/f1zi29.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://files.catbox.moe/bdcf5x.jpg"
)
PLAYLIST_IMG_URL = "https://files.catbox.moe/bdcf5x.jpg"
STATS_IMG_URL = "https://files.catbox.moe/bdcf5x.jpg"
TELEGRAM_AUDIO_URL = "https://files.catbox.moe/bdcf5x.jpg"
TELEGRAM_VIDEO_URL = "https://files.catbox.moe/bdcf5x.jpg"
STREAM_IMG_URL = "https://files.catbox.moe/bdcf5x.jpg"
SOUNCLOUD_IMG_URL = "https://files.catbox.moe/bdcf5x.jpg"
YOUTUBE_IMG_URL = "https://files.catbox.moe/bdcf5x.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://files.catbox.moe/bdcf5x.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://files.catbox.moe/bdcf5x.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://files.catbox.moe/bdcf5x.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )
