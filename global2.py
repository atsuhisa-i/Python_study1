def f():
  global text
  text = 'Good bye'
  print('f():', text)

text = 'Hello'
f()
print(text)