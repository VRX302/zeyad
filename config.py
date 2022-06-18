## What's up Kangers

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "BQBHQ_q9CopdJE7YlsRl5KBN3J4stsBnc5BjWwZfgiEcAl7ltid0fGLdtjeQ3zPy39tqcskpiV9vZg7IRlkptbGuOWTA688d272uWKjftYjRchGklDEof1Qf9UQku8mS4wBixUR2qRfFvp6v1hZvU-301vMZXgs8SY1lcex3Dh7Vx3aYUdnPGDS4onDVvpWSOfo_vus470hAU91mUnCm_QGXztUugXWb90gaOe4ggWJfXG9zEJSmtvc6xX3O2c1VZXutVlcdrEWK_EW2dzerbArT2U7RytcCX_q5BGLtFud-sBAz1rVD50neBkSdhK4Gl56kj9Dp4Gtib23_UYzTN3yDfdemVgA")
BOT_TOKEN = getenv("BOT_TOKEN", "5472929430:AAHKcaZ-Bi0nSLw6LlHGXtsBnCGikBw1iuA")
BOT_NAME = getenv("BOT_NAME", "x1musicbot")
API_ID = int(getenv("API_ID", "13362395"))
API_HASH = getenv("API_HASH", "eb0c8cebc2bb6519cae55da08f37ebfe")
OWNER_NAME = getenv("OWNER_NAME", "ccfct")
OWNER_USERNAME = getenv("OWNER_USERNAME", "ccfct")
ALIVE_NAME = getenv("ALIVE_NAME", "زياد | 𝐙𝐞𝐲𝐚𝐝")
BOT_USERNAME = getenv("BOT_USERNAME", "x1musicbot")
OWNER_ID = getenv("OWNER_ID", "1198027583")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "x1ass")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "ccfct")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "ccfct")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("UPDATES_CHANNEL", "HEROKU_API_KEY")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "2111284822 1198027583").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://te.legra.ph/file/407ce4c57a645c11f65c0.jpg")
START_PIC = getenv("START_PIC", "https://te.legra.ph/file/7713b9828bced85d9b46e.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "10"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/muntazer995/ing")
IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/402c519808f75bd9b1803.jpg")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/c74686f70a1b918060b8e.jpg")
IMG_3 = getenv("IMG_3", "https://te.legra.ph/file/90e3b3aeb77e3e598d66d.jpg")
IMG_4 = getenv("IMG_4", "https://te.legra.ph/file/478f9fa85efb2740f2544.jpg")
IMG_5 = getenv("IMG_5", "https://te.legra.ph/file/2a726c634dbc3b9e8f451.jpg")
IMG_6 = getenv("IMG_6", "https://te.legra.ph/file/430dcf25456f2bb38109f.jpg")
