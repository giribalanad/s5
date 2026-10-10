n = int(input("Number of routers: "))
g = [list(map(int, input().split())) for _ in range(n)]
s = int(input("Source router: "))
d, v = [float('inf')]*n, [False]*n
d[s] = 0

for _ in range(n):
    u = min((i for i in range(n) if not v[i]), key=lambda i: d[i])
    v[u] = True
    for j in range(n):
        if not v[j]:
            d[j] = min(d[j], d[u] + g[u][j])

print("Shortest distances:", *d)
