from environs import Env

# environs kutubxonasidan foydalanish
env = Env()
env.read_env()
# .env fayl ichidan quyidagilarni o'qiymiz
BOT_TOKEN = env.str("5689175199:AAGqxdlr1Bne-qUcqv0eNnTNFV7tUkuvGis")  # Bot toekn
ADMINS = env.list("5631918839")  # adminlar ro'yxati
IP = env.str("ip")  # Xosting ip manzili
