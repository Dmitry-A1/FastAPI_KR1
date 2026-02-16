from fastapi import FastAPI

my_awesome_api = FastAPI()

@my_awesome_api.get("/")
async def root():
    return {"message": "Авторелоад действительно работает"}


# ERROR:    Error loading ASGI app. Attribute "app" not found in module "app".
# WARNING:  WatchFiles detected changes in 'app.py'. Reloading...