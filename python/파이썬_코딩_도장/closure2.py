def outer_func(): 
  msg = 'Hi'
  print('outer_func local variables :', locals())

  def inner_func():
    inner_var = 'Bye'
    print(msg)
    print('inner_func local variables :', locals())

  return inner_func

my_func = outer_func()
my_func()
print(my_func.__closure__)
print(my_func.__dir__())