''' This is to illustrate how join works '''

NAMES = ['farhan', 'danyal', 'noman']

for name in NAMES:
    print(' '.join(["Hi", name]))

print(', '.join(NAMES))
