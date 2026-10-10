
def checksum(data):
    s = sum(data)
    while s > 255:
        s = (s & 255) + (s >> 8)
    return (~s) & 255

data = list(map(int, input("Bytes (0-255): ").split()))
c = checksum(data)
print("Checksum:", c)
print("Error-free" if checksum(data + [c]) == 0 else "Error detected")
