class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    OWNER_ID = "1867106198"
    sudo_users = "1867106198", "1867106198"
    GROUP_ID = -1002122844139
    TOKEN = "6831954648:AAEZKaEyNzWqTVCD8_yO9oe8NkvEHAcEzVQ"
    mongo_url = "mongodb+srv://ATHIFA:ATHIFA@moviehub.ncpwndr.mongodb.net/?retryWrites=true&w=majority&appName=MOVIEHUB"
    PHOTO_URL = ["https://telegra.ph/file/b925c3985f0f325e62e17.jpg", "https://telegra.ph/file/4211fb191383d895dab9d.jpg"]
    SUPPORT_CHAT = "Collect_em_support"
    UPDATE_CHAT = "Collect_em_support"
    BOT_USERNAME = "Collect_Em_AllBot"
    CHARA_CHANNEL_ID = "-1001814139622"
    api_id = 26626068
    api_hash = "bf423698bcbe33cfd58b11c78c42caa2"

    
class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
