while True:
  try:
    f = float(input('Input Fahrenheit: '))
    print( '%.2f' % ((f - 32) / 1.8) )
  except:
    print('wrong input')
