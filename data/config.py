from environs import Env

# environs kutubxonasidan foydalanish
env = Env()
env.read_env()
# .env fayl ichidan quyidagilarni o'qiymiz
BOT_TOKEN = env.str("BOT_TOKEN")  # Bot toekn
ADMINS = env.list("ADMINS")  # adminlar ro'yxati
IP = env.str("ip")  # Xosting ip manzili


CHANNELS = [
    ["КАНАЛ", "-1001894997355", "https://t.me/test_almatov"],
    ["КАНАЛ2", "-1001932056464", "https://t.me/testov_tes"]
]

NOT_SUB_MESSAGE = "Для доступа к боту, необходима подписаться на канал!"
QUALITY = "Выберите качеству на котором хотите скачать видео"