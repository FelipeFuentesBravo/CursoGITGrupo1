def potencia (base, exponente):
	resultado = 1.0
	while (exponente > 0):
		resultado = resultado * base
		exponente = exponente - 1
	while (exponente < 0):
		resultado = resultado / base
		exponente = exponente + 1
	return resultado
