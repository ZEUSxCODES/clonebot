#----------------------------------- https://github.com/m4mallu/clonebot --------------------------------------------#
import os
import logging

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

class Config(object):

    # Get a bot token from botfather
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "5578593608:AAH45CcyFDTVv2V5nhR7nWu8pXdqwPU8rHg")

    # Get from my.telegram.org
    APP_ID = int(os.environ.get("APP_ID", "26395818"))

    # Get from my.telegram.org
    API_HASH = os.environ.get("API_HASH", "0d8a3417bbe63641833b786d6e885703")

    # Generate a user session string
    TG_USER_SESSION = os.environ.get("TG_USER_SESSION", "AQGSxKoAu3i58vzlTvzftYp0P782Z3vlMOGAPYnmuMK88TaG3VbXWcOLOt-zGUl8snWtLu7T27kVtqmcXHu_qtsCY3F1da4MjSRGAjaLmKTe6a8bYJwkhYb-0Si8O_bEEnq7TTJsl_gAOgA2nfXsXza7K1qRtN0LM0xib3Ykhx7lPNXRQHfrbfpQb_oVeMozx0zoM_EijmX5vVCdPfv8cF1shMf3phPMWq2vnsol5wJ0eNG-8VNa1tPo4pv9S51BjV9578Cw7Fqdj34o0TZtcwdbEAUh6RNRsRWunJgzDM3yIGD_AX1CSD0Vscz1NqEt-vDTh7OZpXgLoofGRmd4t9nWaxwG1AAAAAFWVlv5AA")

    # Database URI
    DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://anmol0700:anmol0700@cluster0.rjjytvq.mongodb.net/?retryWrites=true&w=majority")


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
