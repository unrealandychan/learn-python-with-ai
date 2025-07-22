
# Lesson 39: Solution

import asyncio
import aiohttp

async def fetch_post(session, post_id):
    url = f"https://jsonplaceholder.typicode.com/posts/{post_id}"
    async with session.get(url) as response:
        return await response.json()

async def main():
    async with aiohttp.ClientSession() as session:
        post1_task = fetch_post(session, 1)
        post2_task = fetch_post(session, 2)

        results = await asyncio.gather(post1_task, post2_task)
        print(results)

if __name__ == "__main__":
    asyncio.run(main())
