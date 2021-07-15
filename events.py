import os
import slack_sdk
from dotenv import load_dotenv
from flask import Flask
from slackeventsapi import SlackEventAdapter

env_path = os.path.join('.', '.env')
load_dotenv(dotenv_path=env_path)

app = Flask(__name__)
slack_event_adapter = SlackEventAdapter(
    os.environ['SLACK_SIGNING_SECRET'], '/slack/events', app
)

client = slack_sdk.WebClient(token=os.environ["SLACK_TOKEN"])
BOT_ID = client.api_call("auth.test")['user_id']


@slack_event_adapter.on('message')
def message(payload):
    event = payload.get('event', {})
    if is_greeting(event['text']) and not is_bot(event['user']):
        client.chat_postMessage(channel=event['channel'], text="Hello, welcome :tada:")
    return event


def is_greeting(message: str) -> bool:
    return message.lower() in ['hey', 'hello', 'hi']


def is_bot(user_id: int) -> bool:
    return user_id == BOT_ID


if __name__ == '__main__':
    app.run(debug=True)
