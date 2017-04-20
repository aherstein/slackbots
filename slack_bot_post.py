#!/home/adamhers/scripts/python/bin/python

import requests
from random import randint
import tokens

ENDPOINT = "slack.com/api/chat.postMessage"
CHANCE_TO_POST = 2  # Out of 100


def check_chance():
    test = randint(0, 100)
    return test < CHANCE_TO_POST


def post_message(messages, token):
    if check_chance():
        message = messages[randint(0, len(messages) - 1)]

        r = requests.post('https://' + ENDPOINT, {
            'token': token,
            'channel': '5288',
            'as_user': True,
            'text': message
        })
        data = r.json()

        if 'error' in data:
            print(data['error'])
            exit(1)

        return message
    else:
        return "Dice roll failed"


def ballmer():
    # Stock message
    points = randint(-20, 20)
    if points < 0:
        points_message = "DROPPED"
    else:
        points_message = "GAINED"

    extra_message = ""
    if points <= -15:
        extra_message = "I'M RUINED!!!!"

    messages = [
        "DEVELOPERS DEVELOPERS DEVELOPERS DEVELOPERS DEVELOPERS DEVELOPERS",
        "I LOVE THIS COMPANY YEEAAAAHHHHHHHH!!!!",
        "MY MICROSOFT ZUNE IS BROKEN!!!!",
        "WHO SAID SIT DOWN?!?!?!",
        "WINDOWS WINDOWS WINDOWS BABY!!!!",
        "MICROSOFT'S STOCK PRICE JUST {0} {1} POINTS!!!! {2}".format(points_message, abs(points), extra_message)
    ]

    message = post_message(messages, tokens.ballmer)

    print("Posted as ballmer: " + message)


def roy():
    messages = [
        "Have you tried turning it off and on again?",
        "Did you see that ludicrous display last night?"
    ]

    message = post_message(messages, tokens.roy)

    print("Posted as roy: " + message)


def bender():
    messages = [
        'Daffodil'
    ]

    message = post_message(messages, tokens.bender)

    print("Posted as bender: " + message)


ballmer()
roy()
bender()
