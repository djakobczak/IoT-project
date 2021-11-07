from fastapi import FastAPI
import uvicorn

from app.api.api_v1.api import api_router
from app.models.crosswalk import Base
from app.db.database import engine


Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(api_router, prefix='/api/v1')


if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)  # !TODO create settings file / .env.cfg that share config with docker

