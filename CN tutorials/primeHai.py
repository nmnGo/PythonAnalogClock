
n = input(int())
prime = True
# n=50

for i in range(2, int(n/2+1)):
    if (n % i == 0):
        prime = False
        break

if prime:
    print("Prime Hai mubaarak")
else:
    print("Not Prime ")
