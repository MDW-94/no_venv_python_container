import uvicorn;
from fastapi import FastAPI;

from dotenv import dotenv_values;

config = dotenv_values(".env")
app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "A unique response"}

if __name__ == "__main__":
    uvicorn.run(
        "main:app", 
        host=config['HOST'], 
        port=int(config['PORT']), 
        reload=True
    )
    
