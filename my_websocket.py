from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import websockets
import asyncio

driver = webdriver.Chrome()
driver.get("https://qat.srds.ai/")

# Example of Selenium interaction: clicking a button that triggers WebSocket communication
websocket_button = driver.find_element(By.ID, "start-websocket-btn")
websocket_button.click()

time.sleep(5)


async def test_websocket_connection():
    uri = "ws://127.0.0.1:8000/ws/lesson/fba10743-1741-4b85-9089-b1c53b7514ce/?course_id=162905&teacher_id=620657&token=37aaac78ab02f2c40b6979c1e9b9f3cd9517c207"

    try:
        async with websockets.connect(uri) as websocket:
            await websocket.send("Hello, Server!")
            print("Message sent to WebSocket server")

            response = await websocket.recv()
            print(f"Response from server: {response}")

    except Exception as e:
        print(f"Error: {e}")


asyncio.run(test_websocket_connection())

driver.quit()
