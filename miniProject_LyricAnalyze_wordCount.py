text = """
I'm Alive
Celine Dion

I get wings to fly
Oh, oh, I'm alive
When you call on me
When I hear you breathe
I get wings to fly
I feel that I'm alive
When you look at me
I can touch the sky
I know that I'm alive
When you bless the day
I just drift away
All my worries die
I'm glad that I'm alive
You've set my heart on fire
Filled me with love
Made me a woman on clouds above
I couldn't get much higher
My spirit takes flight
'Cause I am alive
When you call on me
When you call on me
When I hear you breathe
When I hear you breathe
I get wings to fly
I feel that I'm alive
I am alive
When you reach for me
When you reach for me
Raising spirits high
God knows that
That I'll be the one
Standing by through good and through trying times
And it's only begun
I can't wait for the rest of my life
When you call on me
When you call on me
When you reach for me
When you reach for me
I get wings to fly
I feel that
When you bless the day
When you bless, you bless the day
I just drift away
I just drift away
All my worries die
I know that I'm alive
I get wings to fly
God knows that I'm alive

"""

print("\n This is split text below: ")
print(text.split())  #---Split lyric into word/phrases

word_count = {}

for word in text.split():
  if word in word_count:
    word_count[word] = word_count[word] + 1
  else:
    word_count[word] = 1

print(word_count)


"""

-------Expected Result:------
 This is split text below: 
["I'm", 'Alive', 'Celine', 'Dion', 'I', 'get', 'wings', 'to', 'fly', 'Oh,', 'oh,', "I'm", 'alive', 'When', 'you', 'call', 'on', 'me', 'When', 'I', 'hear', 'you', 'breathe', 'I', 'get', 'wings', 'to', 'fly', 'I', 'feel', 'that', "I'm", 'alive', 'When', 'you', 'look', 'at', 'me', 'I', 'can', 'touch', 'the', 'sky', 'I', 'know', 'that', "I'm", 'alive', 'When', 'you', 'bless', 'the', 'day', 'I', 'just', 'drift', 'away', 'All', 'my', 'worries', 'die', "I'm", 'glad', 'that', "I'm", 'alive', "You've", 'set', 'my', 'heart', 'on', 'fire', 'Filled', 'me', 'with', 'love', 'Made', 'me', 'a', 'woman', 'on', 'clouds', 'above', 'I', "couldn't", 'get', 'much', 'higher', 'My', 'spirit', 'takes', 'flight', "'Cause", 'I', 'am', 'alive', 'When', 'you', 'call', 'on', 'me', 'When', 'you', 'call', 'on', 'me', 'When', 'I', 'hear', 'you', 'breathe', 'When', 'I', 'hear', 'you', 'breathe', 'I', 'get', 'wings', 'to', 'fly', 'I', 'feel', 'that', "I'm", 'alive', 'I', 'am', 'alive', 'When', 'you', 'reach', 'for', 'me', 'When', 'you', 'reach', 'for', 'me', 'Raising', 'spirits', 'high', 'God', 'knows', 'that', 'That', "I'll", 'be', 'the', 'one', 'Standing', 'by', 'through', 'good', 'and', 'through', 'trying', 'times', 'And', "it's", 'only', 'begun', 'I', "can't", 'wait', 'for', 'the', 'rest', 'of', 'my', 'life', 'When', 'you', 'call', 'on', 'me', 'When', 'you', 'call', 'on', 'me', 'When', 'you', 'reach', 'for', 'me', 'When', 'you', 'reach', 'for', 'me', 'I', 'get', 'wings', 'to', 'fly', 'I', 'feel', 'that', 'When', 'you', 'bless', 'the', 'day', 'When', 'you', 'bless,', 'you', 'bless', 'the', 'day', 'I', 'just', 'drift', 'away', 'I', 'just', 'drift', 'away', 'All', 'my', 'worries', 'die', 'I', 'know', 'that', "I'm", 'alive', 'I', 'get', 'wings', 'to', 'fly', 'God', 'knows', 'that', "I'm", 'alive']
{"I'm": 9, 'Alive': 1, 'Celine': 1, 'Dion': 1, 'I': 21, 'get': 6, 'wings': 5, 'to': 5, 'fly': 5, 'Oh,': 1, 'oh,': 1, 'alive': 9, 'When': 16, 'you': 17, 'call': 5, 'on': 7, 'me': 12, 'hear': 3, 'breathe': 3, 'feel': 3, 'that': 8, 'look': 1, 'at': 1, 'can': 1, 'touch': 1, 'the': 6, 'sky': 1, 'know': 2, 'bless': 3, 'day': 3, 'just': 3, 'drift': 3, 'away': 3, 'All': 2, 'my': 4, 'worries': 2, 'die': 2, 'glad': 1, "You've": 1, 'set': 1, 'heart': 1, 'fire': 1, 'Filled': 1, 'with': 1, 'love': 1, 'Made': 1, 'a': 1, 'woman': 1, 'clouds': 1, 'above': 1, "couldn't": 1, 'much': 1, 'higher': 1, 'My': 1, 'spirit': 1, 'takes': 1, 'flight': 1, "'Cause": 1, 'am': 2, 'reach': 4, 'for': 5, 'Raising': 1, 'spirits': 1, 'high': 1, 'God': 2, 'knows': 2, 'That': 1, "I'll": 1, 'be': 1, 'one': 1, 'Standing': 1, 'by': 1, 'through': 2, 'good': 1, 'and': 1, 'trying': 1, 'times': 1, 'And': 1, "it's": 1, 'only': 1, 'begun': 1, "can't": 1, 'wait': 1, 'rest': 1, 'of': 1, 'life': 1, 'bless,': 1}

-------------------------

"""