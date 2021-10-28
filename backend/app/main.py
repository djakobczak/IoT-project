from fastapi import FastAPI
import uvicorn

from app.api.api_v1.api import api_router
from app.models.crosswalk import Base
from app.db.database import engine


Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(api_router, prefix='/api/v1')

uvicorn.run(app)

# if __name__ == '__main__':
#     # dash_app = create_dash_app()
#     # app.mount('/dash', WSGIMiddleware(dash_app.server))
    
