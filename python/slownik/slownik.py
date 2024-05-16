
print ("jakie slowo chcesz przetlumaczyc")
slownik = {"pies":"police","trawa":"weed","wojtek":"monkey"}

while True:
	slowo=input()
	if slowo in slownik:
		print(slowo,":",slownik[slowo])

	else:
		print ("Nie ma takiego slowa")

