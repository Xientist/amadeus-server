#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 10:07:15 2020

@author: julien
"""

from chatterbot import ChatBot

chatbot = ChatBot("Amadeus")

from chatterbot.trainers import ListTrainer

conversation = [
    "Hello",
    "Hi there!",
    "who are you?",
    "I am Amadeus, an artificial intelligence",
    "Is that true?",
    "Yes",
    "How are you doing?",
    "I'm doing great",
    "That is good to hear",
    "Thank you",
    "You're welcome",
    "That's it then",
    "See you",
    "Bye bye",
    "Bye!"
]

trainer = ListTrainer(chatbot)
trainer.train(conversation)

from flask import Flask, request, jsonify
from markupsafe import escape
app = Flask(__name__)

@app.route('/amadeus/chat', methods=['POST'])
def chat():
    query = request.get_json(force=True)
    question = escape(query['question'])
    response = { 
        'status': 'true',
        'answer': str(chatbot.get_response(question))
        }
    return jsonify(response)