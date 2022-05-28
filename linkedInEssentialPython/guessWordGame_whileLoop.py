#---This Python while-loop additional is same as switch case: in Java


secret = 'nonoka'
pw = ''
auth = False
count = 0
max_attempt = 5

while pw != secret:
  count +=1
  if count > max_attempt: break
  #if count ==3: continue  #--->continue mean that, you skip this step to print out
  pw = input(f"{count}: what's secret word? ")
else:
  auth = True

print("Authorize" if auth else "Calling the FBI...")

"""
------Expected Result: when you guessing NOT correct word and eceed max_attempt---
1: what's secret word? non
2: what's secret word? password
3: what's secret word? Banana
4: what's secret word? xxx
5: what's secret word? Bear
Calling the FBI...
---------------------------------
"""



"""
------Expected Result: when you guessing CORRECT word---
1: what's secret word? nono
2: what's secret word? bear
3: what's secret word? xxx
4: what's secret word? fish
5: what's secret word? nonoka
Authorize
---------------------------------
"""