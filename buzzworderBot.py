import os
import sys
import telebot
from random import randint


TOKEN = sys.argv[1]

bot = telebot.TeleBot(TOKEN)

def load_stuff():
	lists = []
	prefix = os.path.split(sys.argv[0])[0]
	source_types = ['phrases', 'nouns', 'verbs', 'adjectives', 'adverbs', 'bse', 'bse_start']
	sources = [os.path.join(prefix, 'resources', x+'.txt') for x in source_types]
	for i in range(len(sources)):
		lists.append([x.replace('\n', '') for x in open(sources[i]).readlines()])
	return lists

@bot.message_handler(commands=['phrase'])
def buzzwordyphrase(message):
	stuff = load_stuff()
	phrases = stuff[0]
	sub = stuff[1:]
	chosen_phrase = phrases[randint(0, len(phrases)-1)].split(" ")
	ret = []

	pattern = ["**NOUN**", "**VERB**", "**ADJ**", "**ADVERB**", "**BSE**", "**BSE_START**"]

	for word in chosen_phrase:
		for i in range(len(pattern)):
			word = word.replace(pattern[i], sub[i][randint(0, len(sub[i])-1)])
		ret.append(word)

	ret = ' '.join(ret)

	bot.reply_to(message, ret)

bot.polling()

while True:
	pass