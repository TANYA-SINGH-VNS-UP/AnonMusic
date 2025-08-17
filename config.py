import re
import sys
from os import getenv
from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

def validate_env_var(var_name, required=True, cast_type=str, default=None):
    value = getenv(var_name, default)
    if required and (value is None or value == ""):
        sys.exit(f"[ERROR] - Required environment variable '{var_name}' is missing.")
    if cast_type:
        try:
            return cast_type(value)
        except ValueError:
            sys.exit(f"[ERROR] - Environment variable '{var_name}' must be of type {cast_type.__name__}")
    return value


API_ID = validate_env_var("API_ID", cast_type=int)
API_HASH = validate_env_var("API_HASH")
BOT_TOKEN = validate_env_var("BOT_TOKEN")
LOGGER_ID = validate_env_var("LOGGER_ID", cast_type=int)
OWNER_ID = validate_env_var("OWNER_ID", cast_type=int)
MONGO_DB_URI = getenv("MONGO_DB_URI")

# 🔐 Get your secret key from Scy — xD: @ScyxD | Get Free Key : @KeyMakerRoBot
# 📦 Make sure to add all required variables in your .env file.
BASE_API_URL = getenv("BASE_API_URL", "https://tgmusic.fallenapi.fun")
BASE_API_KEY = getenv("0be482_U2cunueLGetvX4eQKfOmmZw-64g71y_C")

# promotion website like : Api Docs etc etc..., Please Don't Change This
WEBSITE = getenv("WEBSITE", "https://tgmusic.fallenapi.fun")
COOKIES_URL = getenv("# Netscape HTTP Cookie File
# http://curl.haxx.se/rfc/cookie_spec.html
# This is a generated file!  Do not edit.

.youtube.com	TRUE	/	FALSE	1789141806	SID	g.a000zwj8AW-3PIlc0cyb6_nmKVSROFQQjhKUfTYeCCaf_QLFbt1S_FmDBTN8LszePLBL7IIUVQACgYKAZgSARESFQHGX2Mi26UuULXqxdiCVnZSMd5zcRoVAUF8yKotLmv40kf7a6UCNQCeDWA10076
.youtube.com	TRUE	/	TRUE	1789141806	__Secure-1PSID	g.a000zwj8AW-3PIlc0cyb6_nmKVSROFQQjhKUfTYeCCaf_QLFbt1S2N8kXcSwNUsZI0ilco41tgACgYKAfQSARESFQHGX2MigBm04qqJ03G_dmL0UhxSZxoVAUF8yKo8BI_jUxzrVY1odLD5IFkL0076
.youtube.com	TRUE	/	TRUE	1789141806	__Secure-3PSID	g.a000zwj8AW-3PIlc0cyb6_nmKVSROFQQjhKUfTYeCCaf_QLFbt1SgOkmXnnqJ3fbDCBmLCwkbgACgYKAXgSARESFQHGX2MidtqADyAV2p3NAyWsY5cRRxoVAUF8yKowPgoyc334xwl2V8rxeVVB0076
.youtube.com	TRUE	/	FALSE	1789141806	HSID	ADlHjuvnLBzf8UDs4
.youtube.com	TRUE	/	TRUE	1789141806	SSID	AigFGC8JflrSFkoO0
.youtube.com	TRUE	/	FALSE	1789141806	APISID	9jFRlzaoD6nwxdnk/AT5xlnaZQfXr7kk35
.youtube.com	TRUE	/	TRUE	1789141806	SAPISID	Y7u5_Y9n2yC3LJ5B/Au9nqW2EfjfsQcR_A
.youtube.com	TRUE	/	TRUE	1789141806	__Secure-1PAPISID	Y7u5_Y9n2yC3LJ5B/Au9nqW2EfjfsQcR_A
.youtube.com	TRUE	/	TRUE	1789141806	__Secure-3PAPISID	Y7u5_Y9n2yC3LJ5B/Au9nqW2EfjfsQcR_A
.youtube.com	TRUE	/	TRUE	1789141822	LOGIN_INFO	AFmmF2swRQIhAINtIWo-6hhxLx9lYlMRwCZmW2gJjead4QaYGEhukGkWAiB5XbHDDzwIuDPy0AY4MbFuUZmiUz7b8VWNsMulltntcQ:QUQ3MjNmejBmeHR3RnBqWWh3YzdXdWhNWTIwTG16aU8tdVdJZlBPOVdIR3d3bWFPVGs3NmFiX3BHbXZMQ0ZQWVBnWHJhNjAyeEhTX1I3YWhNOTZEblN0VE5mM3M3cVJ6OGRDZkZ1aVVmVWZsaGJJelFDOGxYbG5Xb1MxWWZqa0N6b1A0VGtuZjByd0g0VEVlTGlMS2RscDkta2MzVWl0UG9B
.youtube.com	TRUE	/	TRUE	1790024777	PREF	f6=80&f4=4000000&tz=Asia.Calcutta&f7=100
.youtube.com	TRUE	/	TRUE	1787000781	__Secure-1PSIDTS	sidts-CjEB5H03P2hyZu18OG_1aIc-VviHocHya6JrAQUdjR0yWNyTrEDkmzX7IEFnNYo98l4OEAA
.youtube.com	TRUE	/	TRUE	1787000781	__Secure-3PSIDTS	sidts-CjEB5H03P2hyZu18OG_1aIc-VviHocHya6JrAQUdjR0yWNyTrEDkmzX7IEFnNYo98l4OEAA
.youtube.com	TRUE	/	FALSE	1787000788	SIDCC	AKEyXzVMx3xGWrZ_6InJzXFvhMe3TphwrsA5AHsek3tCISWSXbvJ2IsXQ3EQrXXKqqRHvzTwVQ
.youtube.com	TRUE	/	TRUE	1787000788	__Secure-1PSIDCC	AKEyXzW1ordPrXCxZKnQE6fr-9lgas-ec46jk9Q6_gpe3yHkJ1hOD04prNNJQrIWEz4HOiNHn1Y
.youtube.com	TRUE	/	TRUE	1787000788	__Secure-3PSIDCC	AKEyXzW6KMXluL931J9LgVBMEU5st86QTPFdf1YHMaOkS8WEd28AeA_pdXd8txhhHthLJkwELjA
.youtube.com	TRUE	/	TRUE	1771016775	VISITOR_INFO1_LIVE	eYO2Bs18rco
.youtube.com	TRUE	/	TRUE	1771016775	VISITOR_PRIVACY_METADATA	CgJJThIEGgAgIQ%3D%3D
.youtube.com	TRUE	/	TRUE	1770995311	__Secure-ROLLOUT_TOKEN	CLLD4vKorKPr7gEQy7Ov0Yb5jgMY0PyL-Y-SjwM%3D
.youtube.com	TRUE	/	TRUE	0	YSC	hDVbfVyIEEc
")

DURATION_LIMIT_MIN = validate_env_var("DURATION_LIMIT", cast_type=int, default=300)

HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/TANYA-SINGH-VNS-UP/AnonMusic")
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "Master")
GIT_TOKEN = getenv("GIT_TOKEN")


SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/+frNpAnPayWplZDBl")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/+qaTcyac4_HhhNTk1")

AUTO_END_VC_STREAM = getenv("AUTO_END_VC_STREAM", "false").lower() in ("true", "1")
AUTO_LEAVING_ASSISTANT = getenv("AUTO_LEAVING_ASSISTANT", "false").lower() in ("true", "1")
ASSISTANT_LEAVE_TIME = validate_env_var("ASSISTANT_LEAVE_TIME", cast_type=int, default=6400)

SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "22b6125bfe224587b722d6815002db2b")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "c9c63c6fbf2f467c8bc68624851e9773")

PLAYLIST_FETCH_LIMIT = validate_env_var("PLAYLIST_FETCH_LIMIT", cast_type=int, default=25)

TG_AUDIO_FILESIZE_LIMIT = validate_env_var("TG_AUDIO_FILESIZE_LIMIT", cast_type=int, default=204857600)
TG_VIDEO_FILESIZE_LIMIT = validate_env_var("TG_VIDEO_FILESIZE_LIMIT", cast_type=int, default=2071824)

PRIVATE_BOT_MODE_MEM = validate_env_var("PRIVATE_BOT_MODE_MEM", cast_type=int, default=1)

CACHE_DURATION = validate_env_var("CACHE_DURATION", cast_type=int, default=86400)
CACHE_SLEEP = validate_env_var("CACHE_SLEEP", cast_type=int, default=3600)


STRING1 = getenv("STRING_SESSION")
STRING2 = getenv("STRING_SESSION2")
STRING3 = getenv("STRING_SESSION3")
STRING4 = getenv("STRING_SESSION4")
STRING5 = getenv("STRING_SESSION5")


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}
file_cache: dict[str, float] = {}


START_IMG_URL = getenv("START_IMG_URL", "https://files.catbox.moe/gtd7dg.jpg")
PING_IMG_URL = getenv("PING_IMG_URL", "https://files.catbox.moe/gtd7dg.jpg")

PLAYLIST_IMG_URL = "https://files.catbox.moe/gtd7dg.jpg"
STATS_IMG_URL = "https://files.catbox.moe/gtd7dg.jpg"
TELEGRAM_AUDIO_URL = "https://files.catbox.moe/gtd7dg.jpg"
TELEGRAM_VIDEO_URL = "https://files.catbox.moe/gy14qk.jpg"
STREAM_IMG_URL = "https://files.catbox.moe/gtd7dg.jpg"
SOUNCLOUD_IMG_URL = "https://files.catbox.moe/gtd7dg.jpg"
YOUTUBE_IMG_URL = "https://files.catbox.moe/gtd7dg.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://files.catbox.moe/gtd7dg.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://files.catbox.moe/gtd7dg.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://files.catbox.moe/gtd7dg.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))

DURATION_LIMIT = time_to_seconds(f"{DURATION_LIMIT_MIN}:00")

for url_name, url in [("SUPPORT_CHANNEL", SUPPORT_CHANNEL), ("SUPPORT_CHAT", SUPPORT_CHAT)]:
    if not re.match(r"^(?:http|https)://", url):
        sys.exit(f"[ERROR] - {url_name} is invalid. It must start with http:// or https://")
