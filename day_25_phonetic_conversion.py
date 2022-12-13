import pandas

# letter,code
# A,Alfa
# B,Bravo
# C,Charlie
# D,Delta
# E,Echo
# F,Foxtrot
# G,Golf
# H,Hotel
# I,India
# J,Juliet
# K,Kilo
# L,Lima
# M,Mike
# N,November
# O,Oscar
# P,Papa
# Q,Quebec
# R,Romeo
# S,Sierra
# T,Tango
# U,Uniform
# V,Victor
# W,Whiskey
# X,X-ray
# Y,Yankee
# Z,Zulu

data = pandas.read_csv('nato_phonetic_alphabet.csv')
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}

user_input = input("Enter word : \n")

result = [phonetic_dict[letter.capitalize()] for letter in user_input]
print(result)
