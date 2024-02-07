from fastapi import FastAPI


api = FastAPI()


@api.get("/planets")
def x():
    return("hello")