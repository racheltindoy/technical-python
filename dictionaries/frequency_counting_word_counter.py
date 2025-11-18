# Goal: Practice using a dictionary to count the frequency of elements in a list or string (a very common Python use case).

"""
Task: Write a function word_frequency(text) that takes 
a string of text, converts it to lowercase, splits it into words, 
and returns a dictionary where keys are the words and values 
are the number of times that word appears. 
Ignore punctuation for this exercise.
"""
from collections import defaultdict


sentence = 'The young fox was very quick, and the lazy brown fox was quick to jump over the fence. The quick fox often found a quick way around any obstacle. ! ! !'


def word_frequency(text):
	words = text.split()
	word_counter = defaultdict(int)

	for word in words:
		clean_word = word.strip('.,?!:;"()').lower()
		
		if clean_word.isalpha():
			word_counter[clean_word] += 1

	return dict(word_counter)

print('--- Final Word Counts ---')
word_counter = word_frequency(sentence)
for word, count in word_counter.items():
	print(f'{word}: {count}')