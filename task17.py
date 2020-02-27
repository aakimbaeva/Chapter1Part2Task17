hello = input()
offices = {1: 'google_germany.txt',
2: 'google_kazakhstan',
3: 'google_kyrgyzstan',
4: 'google_moscow',
5: 'google_paris',
6: 'google_san_francisco',
7: 'google_sweden',
8: 'google_uar'}
if hello.lower() == 'hello':
    print(offices)
choice = int(input('Hi! Please, choose a number from the listed offices here: '))

with open(offices[choice], 'w') as file:
    file.write(input('Now leave your message here: '))
    print(f'Your complain is successfully sent to the {offices[choice]}')




