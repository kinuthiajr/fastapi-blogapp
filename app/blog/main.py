# Contain fastapi app and endpoints

from fastapi import FastAPI
from .routers import blog

app = FastAPI(title="Blog App")

app.include_router(blog.router)
