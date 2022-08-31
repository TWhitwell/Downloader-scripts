try:
    file = open('failedcounter.txt', 'r')
    n = int(file.read())
    file.close()
except IOError:
    file = open('failedcounter.txt', 'w')
    file.write('1')
    file.close()
    n = 1
print(n)

n += 1

with open('failedcounter.txt', 'w') as file:
    file.write(str(n))
