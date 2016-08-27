def potencia (base, exponente):
	resultado = base
	while (exponente > 0):
		resultado = resultado * base
		exponente = exponente - 1
	return resultado
