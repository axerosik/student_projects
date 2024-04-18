#tworzenie zmiennej licznik
licznik=0
#pętla while do chwili aż licznik 5<
while licznik<5:
	print("wartosc licznika",licznik)
	licznik=licznik+1
	odpowiedz=input("czy chcesz kontynuowac tak/nie")
	if odpowiedz.lower()=="nie":
		break


print("koniec programu")

