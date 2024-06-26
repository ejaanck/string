from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID", "23770828"))
API_HASH = getenv("API_HASH", "2d3e87f244740e5c8286591940e24cd4")

BOT_TOKEN = getenv("BOT_TOKEN"," 7009082569:AAHwZgUZv1eN1W04N7-CeNzlQHhYjLScYes")
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://sorybang:1234@cluster0.ww8a9ut.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

OWNER_ID = int(getenv("OWNER_ID", "7149602071"))
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/mchimacha")
MUST_JOIN = getenv("MUST_JOIN", "thebrazzernew")
