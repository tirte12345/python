from source import data

print ("Teen Language Translator Beta")

text_input = raw_input("Please input your desired text: ")

for key, value in data.items():

    text_input = text_input.replace(key, value)

print "Translated text: " + text_input
