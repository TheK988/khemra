from fastapi import FastAPI, Depends, HTTPException, Header
app = FastAPI()
def api_key_auth(api_key: str = Header(...)):
    valid_api_key ="apikey+secure"
    if api_key != valid_api_key:
        raise HTTPExeption(
            status_code=401,
            detail="Unauthorized: Invalid API Key",)
    return True
@app.get("/private_data", dependencies = [Depends(api_key_auth)])
async def private_data():
    return {"message": "This is sensitive information accessible only with a valid API key."}
