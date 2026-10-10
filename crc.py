
def crc(data, gen):
    a = list(map(int, data + '0' * (len(gen) - 1)))
    g = list(map(int, gen))
    for i in range(len(data)):
        if a[i]:
            for j in range(len(g)):
                a[i+j] ^= g[j]
    return ''.join(map(str, a[-len(g)+1:]))

data, gen = input("Data: "), input("Generator: ")
r = crc(data, gen)
frame = data + r
print("Transmitted frame:", frame)
print("Remainder:", crc(frame[:-len(r)] + frame[-len(r):], gen))
print("Error-free" if crc(frame, gen) == '0' * len(r) else "Error detected")
