from random import choice

questions= ['why is the sky blue?: ',
            'why am I hungry?: ',
            'why does the dog have hair?: ']

question = choice(questions)
answer = input(question).strip().lower()

while answer != 'just because':
    answer = input('why?:').strip().lower()

print('Oh...Okay')
