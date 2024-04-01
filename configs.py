from os import path, getenv

class Config:
    API_ID = int(getenv("API_ID", "28436511"))
    API_HASH = getenv("API_HASH", "0114c36706aca2c07acc12046c15e3f6")
    BOT_TOKEN = getenv("BOT_TOKEN", "7000604952:AAEY-G6ieuK53EG-vPDBEu3-tINF-2XgiXM")
    FSUB = getenv("FSUB", "AnjaliWorldOfficialBot")
    CHID = int(getenv("CHID", "-1001970031336"))
    SUDO = list(map(int, getenv("SUDO").split()))
    MONGO_URI = getenv("MONGO_URI", "mongodb+srv://AnjaliWorld098:anjaliworld098@cluster0.2xwkwyi.mongodb.net/?retryWrites=true&w=majority")
    
cfg = Config()
