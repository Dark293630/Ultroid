# Ultroid - UserBot
# Copyright (C) 2021-2022 TeamUltroid
#
# This file is a part of < https://github.com/TeamUltroid/Ultroid/ >
# PLease read the GNU Affero General Public License in
# <https://github.com/TeamUltroid/pyUltroid/blob/main/LICENSE>.

import sys

from decouple import config

try:
    from dotenv import load_dotenv

    load_dotenv()
except ImportError:
    pass


class Var:
    # mandatory
    API_ID = (
        int(sys.argv[1]) if len(sys.argv) > 1 else config("API_ID","19191128", default=6, cast=int)
    )
    API_HASH = (
        sys.argv[2]
        if len(sys.argv) > 2
        else config("API_HASH","ce5798f52dc7ac5bcd38e892217d5fe2", default="eb06d4abfb49dc3eeb1aeb98ae0f581e")
    )
    SESSION = sys.argv[3] if len(sys.argv) > 3 else config("SESSION","BQBt_P6cdxAKsJSy7bzlt1JoKHeP2WRQBcxf5_q33189Zor4N_iLbNx2RHunfz9GgkdF9hkUJMLGgXmQS2Td1Dxyh62jXhRKdNKGaCJrG8xQQeAebmOQm4zKWeZB4A_jzmzJA18XAxK_oWIwKS4C9eY7ewDmjy4SXI8kMjugi19GuApzFx4jqLO_BX-HWKjK2RKHa5xDfDLGV8tztBB1s7yOT2XKQ7bsv9uUbfYBPkscNgB5q7kG0IpHowcxitYAlMBlEU-1xDbULPxf6wF5Sn4VxKXwIHbwNJJplTn4Eicnmvs8jnQuZ2CkjtHebNeolzTIyGi-uEIkhE0oKnSfipzuAAAAATiHqdIA", default=None)
    REDIS_URI = (
        sys.argv[4]
        if len(sys.argv) > 4
        else (config("REDIS_URI", default=None) or config("REDIS_URL","redis-13770.c284.us-east1-2.gce.cloud.redislabs.com:13770", default=None))
    )
    REDIS_PASSWORD = (
        sys.argv[5] if len(sys.argv) > 5 else config("REDIS_PASSWORD","O4IBZfN8CTdLPJio1ZIoDt20EKdtShHx", default=None)
    )
    # extras
    BOT_TOKEN = config("BOT_TOKEN","5744410348:AAFdYBiHJXg0ZgBAEy00KkttqI7CoFKcNQk", default=None)
    LOG_CHANNEL = config("LOG_CHANNEL","-1001797910328", default=0, cast=int)
    HEROKU_APP_NAME = config("HEROKU_APP_NAME", default=None)
    HEROKU_API = config("HEROKU_API", default=None)
    VC_SESSION = config("VC_SESSION", default=None)
    ADDONS = config("ADDONS", default=False, cast=bool)
    VCBOT = config("VCBOT", default=False, cast=bool)
    # for railway
    REDISPASSWORD = config("REDISPASSWORD", default=None)
    REDISHOST = config("REDISHOST", default=None)
    REDISPORT = config("REDISPORT", default=None)
    REDISUSER = config("REDISUSER", default=None)
    # for sql
    DATABASE_URL = config("DATABASE_URL", default=None)
    # for MONGODB users
    MONGO_URI = config("MONGO_URI", default=None)
