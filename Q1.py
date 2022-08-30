s = 'SUZANKA12345'
print(s.translate({ord(i): None for i in 'SUZAN'}))