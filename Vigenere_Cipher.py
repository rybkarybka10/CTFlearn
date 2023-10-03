word = 'gwox{RgqssihYspOntqpxs}'.lower()
key = 'blorpy'
tab = 'abcdefghijklmnopqrstuvwxyz'
answer = ''
back = 0

for i in range(0, len(word)):
    if word[i] in tab:
        letter = ord(word[i]) - ord(key[(i-back) % len(key)])
        answer = answer + tab[letter]
    else:
        answer = answer + word[i]
        back += 1
        
print(answer)
