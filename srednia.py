import math
import myerror

def srednia(liczby):
	if type(liczby) != list:
		raise myerror.IBeBack()
	for i in range(len(liczby)):
		liczby[i] = float(liczby[i]*liczby[i])
	wynik = sum(liczby)
	wynik = math.sqrt(wynik/len(liczby))
	return wynik
