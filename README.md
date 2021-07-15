# Slack messaging via their API
## Port forwarding
Require ngrok to port-forward the localhost connection to a public IP, for macOS
we can install this using Homebrew through `brew install --cask ngrok`.

We can find the public IP through ngrok by running `ngrok http <port-number>`

## Sending messages
We need to provide the chat:write oauth scope to write to a particular channel, and once
you've installed it in the workspace you'll need to use the `SLACK_TOKEN` to authenticate your
requests

## Responding to events
In the event subscriptions we need to provide a callback url for slack to POST
the payload from a message, your bot will need to be subscribed to the message in the channel
the `message.channels` event name, after changing the scope you'll need to reinstall.