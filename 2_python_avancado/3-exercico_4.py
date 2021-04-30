def fizzBuzz(numero):
    if numero % 3 == 0 and numero % 5 == 0:
        return 'FizzBuzz'
    elif numero % 3 == 0:
        return 'Fizz'
    elif numero % 5 == 0:
        return 'Buzz'
    else:
        return 'Número invalido'


print(fizzBuzz(3))
print(fizzBuzz(5))
print(fizzBuzz(10))
print(fizzBuzz(15))

