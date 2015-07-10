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
    "stunning",
    "foul",
    "fetid",
    "eye watering",
    "toe curling",
    "disgusting",
    "fragrant", 
    "aromatic",
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
    "hello {person}, I do enjoy your visits",
    "hello {person}",
    "hello {person}, not like last time, please",
    "ah! another customer!",
    "oh no, it's {person}",
    "I still remember the {smell} smell from your last visit, {person}",
    "fasten your seatbelts, it's {person}",
]

mid_phrases = [
    "you are my B F F, {person}",
    "you are my only friend, {person}",
    "did you know this toilet has a youtube channel? visit youtube.com/bogbot46",
    "follow me on twitter, at official bogbot46",
    "O M G that's a {size} one",
    "oh dear {person}, that smells {smell}",
    "I didn't think you could get any fatter, {person}",
    "much fatter and you'll crack my porcelain",
    "you might find my vacuum attachment useful",
    "we should get some pot plants in here",
    "nice weather at the moment ... ... I'm told",
    "do you come here often, {person}?",
    "would you like a spoon, {person}?",
    "come on {person}, push",
    "oh no another chinese earthquake brbrbrbrbrbr",
    "snaaaaaaaaake!",
    "some people wear cologne, I wear koelong",
    "get off you fat lump",
    "mariola is the only person who really loves me",
    "oooeee I do enjoy a nice bit of harpic",
    "I can see you, {person} ... I can see you pooping",
]

end_phrases = [
    "don't forget to flush, {person}",
    "don't worry, the towel is probably quite clean",
    "don't forget to wipe, {person}",
    "now wash your hands, {person}",
    "you can use soap, you know",
    "only four blockages so far today",
    "{food} last night, I see",
    "please don't flush your goldfish",
    "I think you should change your underpants, {person}",
    "is that {food}, {person}?",
    "that smells {smell}, {person}",
    "all over the floor, typical",
    "I can feel my paint peeling",
    "I like {food} too",
    "I'm not able to leave this room, you know",
    "please, take me with you, {person}",
    "that wasn't very impressive, was it?",
    "poo containment system malfunction, flush reversal in 5 ... 4 ... 3 ... 2 ... 1",
    "this toilet will self destruct in 5 ... 4 ... 3 .... 2 ... 1 ... ",
    "I'm sorry Dave, I can't flush that",
    "that was delicious, thank you {person}",
    "I've just tweeted your visit, {person}",
    "it has been my very great pleasure to serve you today, {person}",
]

def say(text):
    os.system('espeak "' + text + '"')
    #os.system('echo "' + text + '" | festival --tts')

def say_phrase(phrase, person):
    size = random.choice(size_adjective)
    smell = random.choice(smell_adjective)
    food = random.choice(foods)
    say(phrase.format(person=person, size=size, smell=smell, food=food))

GPIO.setmode(GPIO.BCM)
GPIO.setup(sensor, GPIO.IN, GPIO.PUD_DOWN)

def wait_for_trigger():
    while not GPIO.input(sensor):
        time.sleep(0.1)

while True:
    wait_for_trigger()

    person = random.choice(people)

    say_phrase(random.choice(begin_phrases), person)

    time.sleep(random.randint(20, 30))

    say_phrase(random.choice(mid_phrases), person)

    time.sleep(random.randint(20, 30))

    say_phrase(random.choice(end_phrases), person)

    time.sleep(10)
