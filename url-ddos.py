import aiohttp
import asyncio

async def consume_traffic(session, url):
    while True:
        try:
            async with session.get(url) as response:
                response.raise_for_status()
                data = await response.read()
                # 模拟处理数据（在这里可以是其他操作）
                print("Downloading...")
        except aiohttp.ClientError as e:
            print(f"Error downloading {url}: {e}")

async def main(url, num_tasks):
    async with aiohttp.ClientSession() as session:
        tasks = [consume_traffic(session, url) for _ in range(num_tasks)]
        await asyncio.gather(*tasks)

if __name__ == "__main__":
    url = input("Please enter the URL to consume traffic from: ")
    num_tasks = int(input("Please enter the number of concurrent tasks (threads): "))
    asyncio.run(main(url, num_tasks))
