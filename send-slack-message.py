#!/usr/bin/env python3

"""
send-slack-message.py
---
In case you haven't noticed, this send a message to Slack.

RELEASE: 0.1
"""

import argparse
import requests


def send_message(integration, destination, subject, message):
    hook = 'https://hooks.slack.com/services/{}'.format(integration)
    data = {
        'text': message,
        'channel': destination,
        'username': subject,
    }
    requests.post(hook, json=data)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--token',
                        type=str,
                        help="Slack Integration Token")
    parser.add_argument('-c', '--channel',
                        type=str,
                        default="#test",
                        help="Slack channel/person to send the message")
    parser.add_argument('-m', '--message',
                        type=str,
                        help="Message to be sent")
    parser.add_argument('-d', '--debug',
                        action='store_true',
                        help="Use only if DEBUG")

    args = parser.parse_args()
    if args.message and args.channel and args.message:
        if not args.debug and args.token:
            send_message(args.token, args.channel, args.message)
        else:
            print(args.token, args.channel, args.message)
