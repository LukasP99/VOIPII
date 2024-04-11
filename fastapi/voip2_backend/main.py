from fastapi import FastAPI, HTTPException
#from fastapi.middleware.cors import CORSMiddleware
from .lib.schemas import ManagedCall
from .lib.ami import make_call


app = FastAPI()
#app.add_middleware(
#    CORSMiddleware,
#    allow_origins=["https://u54.vsb.lab"],
#    allow_credentials=True,
#    allow_methods=["*"],
#    allow_headers=["*"],
#)


@app.get("/")
async def root():
    return {"message": "voip 2"}


@app.post("/call")
async def create_call(call_details: ManagedCall):
    try:
        make_call(from_ext=call_details.from_ext, to_ext=call_details.to_ext)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to make call. {e}")
    return {"message": "Call created"}
