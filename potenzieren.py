#!/usr/bin/env python3

counter = 0
ergebnis = ''

basis = input('Zu welcher Basis soll im Anschluss potenziert werden? ')
limit = input('Wie viele Stufen sollen berechnet werden? ')

for number in range(int(limit)):
    counter += 1
    if counter < int(limit):
        ergebnis = str(ergebnis) + str(int(basis)**(number+1))+', '
    else:
        ergebnis = str(ergebnis) + str(int(basis)**(number+1))

print(ergebnis)
