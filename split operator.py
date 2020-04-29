#returns a list of strings after breaking the given string by the specified separator
text = 'geeks for geeks'

# Splits at space
print(text.split())

word = 'geeks, for, geeks'

# Splits at ','
print(word.split(', '))

word = 'geeks:for:geeks'

# Splitting at ':'
print(word.split(':'))

word = 'CatBatSatFatOr'

# Splitting at 3
print([word[i:i + 3] for i in range(0, len(word), 3)])