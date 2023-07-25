# N and k thingy
N = int(input("Input N(Range): "))
k = int(input("Input k(Iterations): "))
Eliminated = N/(2**k)
print("Eliminated:")
print(Eliminated)
print("Remaining:")
print(N - Eliminated)