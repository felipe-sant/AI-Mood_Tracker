def traduzir(label):
    estrelas = int(label.split()[0])
    if estrelas <= 2:
        return "Negativo"
    elif estrelas == 3:
        return "Neutro"
    else:
        return "Positivo"