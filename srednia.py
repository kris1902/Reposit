import math
import myerror

def srednia(liczby):
	"""Oblicza srednia kwadratowa listy/krotki liczb."""
	if type(liczby) != list:
		raise myerror.IBeBack()
	for i in range(len(liczby)):
		liczby[i] = float(liczby[i]*liczby[i])
		print ""
	wynik = sum(liczby)
	wynik = math.sqrt(wynik/len(liczby))
	return wynik
