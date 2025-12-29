# Data kelurahan Pondok Aren tahun 2024
data = [
    {"Kelurahan": "Pondok Betung", "RT": 72, "RW": 8, "Jumlah": 80},
    {"Kelurahan": "Pondok Karya", "RT": 70, "RW": 10, "Jumlah": 80},
    {"Kelurahan": "Jurangmangu Barat", "RT": 96, "RW": 15, "Jumlah": 111},
    {"Kelurahan": "Jurangmangu Timur", "RT": 93, "RW": 13, "Jumlah": 106},
    {"Kelurahan": "Pondok Aren", "RT": 86, "RW": 13, "Jumlah": 99},
    {"Kelurahan": "Pondok Jaya", "RT": 29, "RW": 7, "Jumlah": 36},
    {"Kelurahan": "Pondok Pucung", "RT": 102, "RW": 17, "Jumlah": 119},
    {"Kelurahan": "Parigi", "RT": 91, "RW": 25, "Jumlah": 116},
    {"Kelurahan": "Parigi Baru", "RT": 30, "RW": 7, "Jumlah": 37},
    {"Kelurahan": "Pondok Kacang Timur", "RT": 114, "RW": 13, "Jumlah": 127},
    {"Kelurahan": "Pondok Kacang Barat", "RT": 61, "RW": 10, "Jumlah": 71}
]
# Definisikan item: weight = RW, value = RT
items = [(d["RW"], d["RT"], d["Kelurahan"]) for d in data]

capacity = 50  # batas RW yang bisa dipilih
n = len(items)

# DP table
dp = [[0]*(capacity+1) for _ in range(n+1)]

for i in range(1, n+1):
    w, v, name = items[i-1]
    for c in range(capacity+1):
        if w <= c:
            dp[i][c] = max(dp[i-1][c], dp[i-1][c-w] + v)
        else:
            dp[i][c] = dp[i-1][c]

# Nilai maksimum
max_value = dp[n][capacity]
print("Manfaat maksimum Dynamic Programming (RT):", max_value)

# Backtrack untuk cari kelurahan terpilih
selected = []
c = capacity
for i in range(n, 0, -1):
    if dp[i][c] != dp[i-1][c]:
        w, v, name = items[i-1]
        selected.append(name)
        c -= w

print("Kelurahan terpilih (Dynamic Programming):", selected)
print("-------------------------------------------------------------------------------------------------------------------------s")

# Greedy: pilih kelurahan dengan rasio RT/RW terbesar
items_sorted = sorted(items, key=lambda x: x[1]/x[0], reverse=True)

capacity = 50
selected_greedy = []
total_value = 0
total_weight = 0

for w, v, name in items_sorted:
    if total_weight + w <= capacity:
        selected_greedy.append(name)
        total_weight += w
        total_value += v

print("Manfaat maksimum Greedy (RT):", total_value)
print("Kelurahan terpilih (Greedy):", selected_greedy)
