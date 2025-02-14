message = input('message? ')
message = message.lower()
message = message.strip()

if message[0:5] == 'hello':
    print('$0')
elif message[0] == 'h':
    print('$20')
else:
    print('$100')
