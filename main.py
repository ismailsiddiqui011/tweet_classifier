import uvicorn, os
if __name__ == "__main__":
    uvicorn.run("api:app", host="0.0.0.0", port=1411, workers=1, reload=False)