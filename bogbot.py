#!/usr/bin/python

import os
import random
import time
import RPi.GPIO as GPIO

sensor = 4



people = [
    "Nina",
    "Theo",
    "Petra",
    "John"
]

size_adjective = [
    "huge",
    "big",
    "enormous",
    "massive",
    "stupendous",
    "gargantuan",
    "gigantic",
    "titanic",
    "tiny"
]

smell_adjective = [
    "terrible",
    "gross",
    "appalling",
    "horrifying",
    "horrific",
    "terrific",
    "amazing",
    "overwhelming",
    "nauseating",
    "revolting",
    "disgusting"
]

foods = [
    "sweetcorn",
    "asparagus",
    "carrots",
    "soya mince",
    "beetroot",
]

begin_phrases = [
    "welcome, I am bogbot46",
    "hello {0}, I do enjoy your visits",
    "hello {0}",
    "hello {0}, not like last time, please",
    "ah! another customer!",
    "oh no, it's {0}",
    "I still remember the {2} smell from your last visit, {0}",
    "fasten your seatbelts, it's {0}",
]

mid_phrases = [
    "you are my B F F, {0}",
    "you are my only friend, {0}",
    "did you know this toilet has a youtube channel? visit youtube.com/bogbot46",
    "follow me on twitter, at official bogbot46",
    "O M G that's a {1} one",
    "oh dear {0}, that smells {2}",
    "I didn't think you could get any fatter, {0}",
    "much fatter and you'll crack my porcelain",
    "you might find my vacuum attachment useful",
    "we should get some pot plants in here",
    "nice weather at the moment ... ... I'm told",
    "do you come here often, {0}?",
    "would you like a spoon, {0}?",
    "come on {0}, push",
    "some people wear cologne, I wear koelong",
    "get off you fat lump",
    "mariola is the only person who really loves me",
    "oooeee I do enjoy a nice bit of harpic",
    "I can see you, {0} ... I can see you pooping",
]

end_phrases = [
    "don't forget to flush, {0}",
    "don't worry, the towel is probably quite clean",
    "don't forget to wipe, {0}",
    "now wash your hands, {0}",
    "you can use soap, you know",
    "only four blockages so far today",
    "{3} last night, I see",
    "please don't flush your goldfish",
    "I think you should change your underpants, {0}",
    "is that {3}, {0}?",
    "that smells {2}, {0}",
    "all over the floor, typical",
    "I can feel my paint peeling",
    "I like {3} too",
    "I'm not able to leave this room, you know",
    "please, take me with you, {0}",
    "that wasn't very impressive, was it?",
    "poo containment system malfunction, flush reversal in 5 ... 4 ... 3 ... 2 ... 1",
    "this toilet will self destruct in 5 ... 4 ... 3 .... 2 ... 1 ... ",
    "I'm sorry Dave, I can't flush that",
    "that was delicious, thank you {0}",
    "I've just tweeted your visit, {0}",
    "it has been my very great pleasure to serve you today, {0}",
]

def rand(array):
    return array[random.randint(0, len(array) - 1)]

def say(text):
    os.system('espeak "' + text + '"')
    #os.system('echo "' + text + '" | festival --tts')

GPIO.setmode(GPIO.BCM)
GPIO.setup(sensor, GPIO.IN, GPIO.PUD_DOWN)

previous_state = False
current_state = False

def wait_for_trigger():
    x = GPIO.input(sensor)
    while not x:
        time.sleep(0.1)
        x = GPIO.input(sensor)

while True:
    wait_for_trigger()

    person = rand(people)

    size = rand(size_adjective)
    smell = rand(smell_adjective)
    food = rand(foods)
    say(rand(begin_phrases).format(person, size, smell, food))

    time.sleep(random.randint(2, 3))

    size = rand(size_adjective)
    smell = rand(smell_adjective)
    food = rand(foods)
    say(rand(mid_phrases).format(person, size, smell, food))

    time.sleep(random.randint(2, 3))

    size = rand(size_adjective)
    smell = rand(smell_adjective)
    food = rand(foods)
    say(rand(end_phrases).format(person, size, smell, food))

    time.sleep(10)
