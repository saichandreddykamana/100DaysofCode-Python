names = []
with open('./Input/Names/invited_names.txt') as names_file:
    for name in names_file.readlines():
        names.append(name.strip())

with open('./Input/Letters/starting_letter.txt') as letter_file:
    letter = letter_file.read()
    for name in names:
        new_content = letter.replace('[name]', name)
        file = open(f'./Output/ReadyToSend/letter_for_{name.replace(" ", "_")}.txt', 'w')
        file.write(new_content)
        file.close()
