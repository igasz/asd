'''podaj/zaimlementuj algorytm znajdujący wartość optymalnego zbioru przedmiotów w dyskretnym problemie plecakowym. Algorytm
powinien działać w czasie wielomianowym względem liczby przedmiotów i sumy profitów'''

'''W dyskretnym problemie plecakowym (0/1 knapsack problem) mamy:
- n przedmiotów,
- każdy przedmiot i ma wagę w[i] i zysk p[i],
- pojemność plecaka to W.
Cel: wybrać podzbiór przedmiotów, aby suma wag nie przekroczyła W, a suma profitów była jak największa.'''

'''Złożoność czasowa: O(n*c)
Złożoność pamięciowa O(n* c)
1. Tworzę tablicę tab[n+1][c+1], gdzie tab[i][w] oznacza max wartość, jaką można osiągnąć, wybierając spośród pierwszych i przedmiotów przy pojemności w.
2. Wypełnia tablicę dynamicznie: Dla każdego przedmiotu i każdej możliwej pojemności, sprawdza: czy opłaca się włączyć ten przedmiot 
(jeśli się mieści)/czy lepiej go pominąć. Wybiera większą wartość.
3. Wartość tab[n][c] to wynik końcowy — maksymalna możliwa wartość dla całego plecaka.'''

def knapsack(c, weights, val): # c pojemnosc, weights, val - zysk
    n = len(val)
    tab = [[0]*(c+1) for _ in range(n+1)] #tab[i][w] Max wartość, jaką można uzyskać z pierwszych i przedmiotów, jeśli plecak ma pojemność w.

    for i in range(1, n+1):
        for w in range(c+1):
            if weights[i-1] <= w:
                include_item = val[i - 1] + tab[i - 1][w - weights[i - 1]]
                exclude_item = tab[i - 1][w]
                tab[i][w] = max(include_item, exclude_item)
            else:
                tab[i][w] = tab[i - 1][w]
    return tab[n][c]


def knapsack_items(capacity, weights, values):
    n = len(values)
    tab = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                include_item = values[i - 1] + tab[i - 1][w - weights[i - 1]]
                exclude_item = tab[i - 1][w]
                tab[i][w] = max(include_item, exclude_item)
            else:
                tab[i][w] = tab[i - 1][w]

    for row in tab:
        print(row)

    items_included = []
    w = capacity
    for i in range(n, 0, -1):
        if tab[i][w] != tab[i - 1][w]:
            items_included.append(i - 1)
            w -= weights[i - 1]

    print("\nItems included:", items_included)

    return tab[n][capacity]


values = [300, 200, 400, 500]
weights = [2, 1, 5, 3]
capacity = 10
print(knapsack(capacity, weights, values))
print(knapsack_items(capacity, weights, values))