# script
code = ('^&,*$,&),!@#,*#,!!^,(&,!!$,(%,$^,(%,*&,(&,!!$,!!%,(%,$^,(%,&),!!!,!!$,(%,$^,(%,&^,!)%,!)@,!)!,!@%')
message = []
for i in range(len(code)):
    if code[i] == '!': message.append('1')
    if code[i] == '@': message.append('2')
    if code[i] == '#': message.append('3')
    if code[i] == '$': message.append('4')
    if code[i] == '%': message.append('5')
    if code[i] == '^': message.append('6')
    if code[i] == '&': message.append('7')
    if code[i] == '*': message.append('8')
    if code[i] == '(': message.append('9')
    if code[i] == ')': message.append('0')
    if code[i] == ',': message.append('|')
ascii = ''.join(message).split('|')

# result
# ascii = ['67', '84', '7', '123', '83', '116', '97', '114', '95', '46', '95', '87', '97', '114', '115', '95', '46', '95', '70', '111', '114', '95', '46', '95', '76', '105', '102', '101', '125']

word = []
for i in range(len(ascii)):
    character = chr(int(ascii[i]))
    word.append(character)

print(''.join(word)) # finish


