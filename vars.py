#🇳‌🇮‌🇰‌🇭‌🇮‌🇱‌
# Add your details here and then deploy by clicking on HEROKU Deploy button
import os
from os import environ

API_ID = int(environ.get("API_ID", "25403301"))
API_HASH = environ.get("API_HASH", "d700b4abe3d023165894291b6fcbd3a0")
BOT_TOKEN = environ.get("BOT_TOKEN", "7247251596:AAH557vA96a3Gbywpia1DnFWKhiwjEoL6hk")
OWNER = int(environ.get("OWNER", "1081310808"))
CREDIT = "𝄟⃝‌🐬🇳‌ɪᴋʜɪʟ𝄟⃝🐬"
AUTH_USER = os.environ.get('AUTH_USERS', '5680454765').split(',')
AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
if int(OWNER) not in AUTH_USERS:
    AUTH_USERS.append(int(OWNER))
  
#WEBHOOK = True  # Don't change this
#PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set
