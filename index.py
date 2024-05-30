from fastapi import FastAPI
from routes.user import user  # Adjust this if the actual import path is different

app = FastAPI()  # Setting the Swagger UI path to /docsswagger

app.include_router(user)
# @app.get('/')
# async def read_root():
#     return {"Hello": "World"}

