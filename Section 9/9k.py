score = 0

print('Is England in Africa, America or Europe?')

answerQ1 = input()

while answerQ1 != 'Europe':
 print('Wrong, try again.')
 score = score - 1
 answerQ1 = input()

print('Well done, England is in Europe.')
score = score + 2
print('What is the capital city of England?')

answerQ2 = input()

while answerQ2 != 'London':
 print('Wrong, try again.')
 score = score - 1
 answerQ2 = input()

print('Excellent, London is the capital of England.')
score = score + 2
print('Is India in Asia, Europe or Africa?')

answerQ3 = input()

while answerQ3 != 'Asia':
 print('Wrong, try again!')
 score = score - 1
 answerQ3 = input()

print('Amazing! India is in Asia.')
score = score + 2
print('What is the capital city of India?')
answerQ4 = input()

while answerQ4 != 'New Dehli':
 print('Wrong, try again!')
 score = score - 1
 answerQ4 = input()

print('Amazing! The capital city of India is New Dehli.')
score = score + 2
print('What is the capital city of the USA?')

answerQ5 = input()

while answerQ5 != 'Washington DC':
 print('Wrong, try again!')
 score = score - 1
 answerQ5 = input()
print('Amazing! The capital of the USA is Washington DC.')
score = score + 2

print('You scored', score, 'points!')
