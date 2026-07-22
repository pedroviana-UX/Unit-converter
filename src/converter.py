CATEGORIA_DA_UNIDADE = {
    "metro": "comprimento", "centimetro": "comprimento", "quilometro": "comprimento",
    "quilograma": "peso", "grama": "peso", "libra": "peso",
    "celsius": "temperatura", "fahrenheit": "temperatura", "kelvin": "temperatura",
}


def converter_comprimento(valor, origem, destino):
    para_metro = {"metro": 1, "centimetro": 0.01, "quilometro": 1000}
    valor_em_metro = valor * para_metro[origem]
    return valor_em_metro / para_metro[destino]


def converter_peso(valor, origem, destino):
    para_grama = {"quilograma": 1000, "grama": 1, "libra": 453.592}
    valor_em_grama = valor * para_grama[origem]
    return valor_em_grama / para_grama[destino]


def converter_temperatura(valor, origem, destino):
    if origem == "fahrenheit":
        celsius = (valor - 32) * 5/9
    elif origem == "kelvin":
        celsius = valor - 273.15
    else:
        celsius = valor

    if destino == "fahrenheit":
        return celsius * 9/5 + 32
    elif destino == "kelvin":
        return celsius + 273.15
    else:
        return celsius


def converter(valor, origem, destino):
    categoria_origem = CATEGORIA_DA_UNIDADE[origem]
    categoria_destino = CATEGORIA_DA_UNIDADE[destino]

    if categoria_origem != categoria_destino:
        raise ValueError("As duas unidades precisam ser da mesma categoria.")

    if categoria_origem == "comprimento":
        return converter_comprimento(valor, origem, destino)
    elif categoria_origem == "peso":
        return converter_peso(valor, origem, destino)
    else:
        return converter_temperatura(valor, origem, destino)