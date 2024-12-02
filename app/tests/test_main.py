import pytest
import httpx
from httpx import AsyncClient
from app.main import app

@pytest.mark.asyncio
async def test_get_filtered_posts():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/posts/filtered")
        assert response.status_code == 200
        posts = response.json()
        assert all(post["id"] > 30 for post in posts)
