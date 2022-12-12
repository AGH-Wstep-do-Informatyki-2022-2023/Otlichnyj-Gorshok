# Zadanie 9.
# Liczba półpierwsza to liczba, która jest iloczynem dwóch liczb pierwszych (niekoniecznie różnych).
# Stwórz funkcję, która przyjmuje pobraną od użytkownika liczbę N jako argument i zwraca dwie listy.
# Pierwsza to z liczbami półpierwszymi <N, które są iloczynem dwóch różnych liczb pierwszych,
# a druga z pozostałymi liczbami półpierwszymi <N.
# Wykorzystaj odwzorowanie list.

if __name__ == '__main__':
    # Użytkownik wprowadza N i program sprawdza czy N jest liczbą naturalną dodatnią
    while True:
        try:
            N = int(input("Podaj N (wprowadzona wartość ma być liczbą naturalną dodatnią):"))
            if N <= 0:
                raise ValueError
            else:
                break
        except ValueError:
            print("Wprowadzona wartość nie jest liczbą naturalną dodatnią, spróbuj ponownie.")
    polpierwsze_rozne = []
    polpierwsze_pozostale = []
    # Sito Erastostenesa - wyliczanie liczb pierwszych
    pierwsze = [i for i in range(0, N)]
    if N > 1:
        pierwsze[1] = 0
    #
    for i in range(2, N//2):
        for j in range(i*2, N, i):
            pierwsze[j] = 0
    # Usuwanie "0" - liczb niepierwszych
    pierwsze = [i for i in pierwsze if pierwsze[i] != 0]

    # Poniżej algorytm (usuwania "0") działający bez odwzorowania list
    # while True:
    #    try:
    #        pierwsze.remove(0)
    #    except ValueError:
    #        break

    # Wyliczanie liczb półpierwszych i rozdzielanie ich na poszczególne listy
    for i in pierwsze:
        if i > int((N+1) ** (1/2)):
            break
        for j in pierwsze:
            if j * i >= N:
                break
            elif j < i:
                continue
            elif i == j:
                polpierwsze_pozostale.append(i*j)
            else:
                polpierwsze_rozne.append(i*j)
    polpierwsze_rozne.sort()
    print("Lista liczb pierwszych mniejszych od N:", pierwsze)
    print("Lista liczb półpierwszych mniejszych od N, będących iloczynem dwóch różnych licz pierwszych:",
          polpierwsze_rozne)
    print("Lista pozostałych liczb półpierwszych mniejszych od N:", polpierwsze_pozostale)
