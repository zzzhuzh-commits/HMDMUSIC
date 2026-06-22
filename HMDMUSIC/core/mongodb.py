from HMDMUSIC.core.database import db

async def ping_db():
    await db.command("ping")
    return True
