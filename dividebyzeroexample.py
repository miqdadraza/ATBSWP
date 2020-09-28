def div42by(divideBy):
    try:
        return 42/divideBy
    except ZeroDivisionError: #try and except can make exceptions so the other code continues on. If there is no ZeroDivisionError stated, it will catch all types of errors
        print("Error, trying to divide by 0")

print(div42by(2))
print(div42by(12))
print(div42by(0))
print(div42by(1))
print(div42by(33))
print(div42by(3))

print(div42by(33))


print(div42by(42))
print(div42by(54))
print("My name is miqdad")


