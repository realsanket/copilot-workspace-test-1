from fastapi import FastAPI
import httpx
import logging

app = FastAPI()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.get("/")
def read_root():
    return {"message": "Hello World"}

@app.get("/posts/filtered")
async def get_filtered_posts():
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get("https://jsonplaceholder.typicode.com/posts")
            response.raise_for_status()
            posts = response.json()
            filtered_posts = [post for post in posts if post["id"] > 30]
            return filtered_posts
    except httpx.HTTPStatusError as exc:
        logger.error(f"HTTP error occurred: {exc}")
        return {"error": "Failed to fetch posts"}
    except Exception as exc:
        logger.error(f"An error occurred: {exc}")
        return {"error": "An unexpected error occurred"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
