import asyncio
import random
import datetime

class SensorAgent:
    async def monitor(self):
        disasters = ["Fire", "Flood", "Earthquake", "Landslide"]
        severity_levels = ["Low", "Medium", "High", "Critical"]

        print("📡 SensorAgent started monitoring environment...\n")

        while True:
            event = random.choice(disasters)
            severity = random.choice(severity_levels)
            time = datetime.datetime.now()

            log = f"[{time}] Event: {event} | Severity: {severity}"
            print(log)

            # save to log file
            with open("event_log.txt", "a") as file:
                file.write(log + "\n")

            await asyncio.sleep(5)  # every 5 seconds

async def main():
    agent = SensorAgent()
    await agent.monitor()

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nSensorAgent stopped.")
