def hello(name=''):
    return f'Hello, {name.title()}!' if name != '' else 'Hello, World!'


print(hello('aliSe'))
print(hello())
