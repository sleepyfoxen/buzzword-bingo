import os
import csv
import json
import nltk

channel_files = []
for root, dirnames, file_names in os.walk('data'):
    for file_name in file_names:
        if file_name.endswith(('.json')):
            channel_files.append(os.path.join(root, file_name))

print(channel_files)

channels = {}


for channel_file in channel_files:
    print(channel_file)

    with open(channel_file, 'r') as f:
        channels[channel_file
                 .split('/')[1]
                 .split('.')[0]] = json.load(f)

messages = []
for channel in channels:
    print(channel)
    for event in channels[channel]:
        try:
            messages.append(event['text'])
        except KeyError: pass


print(len(messages))
l = len(messages) + 1

while True:
    l = len(messages)
    for message in messages:
        if 'has joined the channel' in message \
                or 'channel purpose' in message \
                or 'channel topic' in message:
            messages.remove(message)

    if len(messages) == l: break

print(len(messages))

corpus = ' '.join(messages)
tokens = nltk.word_tokenize(corpus)

with open('corpus_tokens.csv', 'w') as f:
    for token in tokens:
        f.write('{}\n'.format(token))