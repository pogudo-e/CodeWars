def say_hello(name, city, state):
    return f'Hello, {" ".join([i for i in name])}! Welcome to {city}, {state}!'


# your code here


print(say_hello(['John', 'Smith'], 'Phoenix', 'Arizona'),
      'Hello, John Smith! Welcome to Phoenix, Arizona!')
print(say_hello(['Franklin', 'Delano', 'Roosevelt'], 'Chicago', 'Illinois'),
      'Hello, Franklin Delano Roosevelt! Welcome to Chicago, Illinois!')

# def say_hello(name, city, state):
# return "Hello, {}! Welcome to {}, {}!".format(" ".join(name), city, state)
