import asyncio

class BasicAgent:
    async def run(self):
        print("✅ Agent successfully started")
        while True:
            print("🤖 BasicAgent is active and running...")
            await asyncio.sleep(5)

async def main():
    agent = BasicAgent()
    await agent.run()

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Stopping agent...")
