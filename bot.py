import os
import slack_sdk
from dotenv import load_dotenv

env_path = os.path.join('.', '.env')
load_dotenv(dotenv_path=env_path)

client = slack_sdk.WebClient(token=os.environ["SLACK_TOKEN"])
client.chat_postMessage(channel="#test", text="Hello, welcome :tada:")
