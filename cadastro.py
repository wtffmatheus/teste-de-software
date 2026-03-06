def valida_cep(cep: str, cidade: str) -> bool:
    faixas = {
        "Aluminio": (18125000, 18129999),
        "Ipero": (18560000, 18569999),
        "Aracariguama": (18147000, 18149999),
        "Aracoiaba da Serra": (18190000, 18194999),
        "Itu": (13300000, 13314999),
        "Mairinque": (18120000, 18124999),
        "Cabreuva": (13315000, 13319999),
        "Capela do Alto": (18195000, 18199999),
        "Salto": (13320000, 13329999),
        "Salto de Pirapora": (18160000, 18169999),
        "Sao Roque": (18130000, 18146999),
        "Sarapui": (18225000, 18229999),
        "Sorocaba": (18000000, 18109999),
        "Votorantim": (18110000, 18119999),
        "Porto Feliz": (18540000, 18549999),
    }
    cep_num = int(cep.replace("-", ""))
    if cidade in faixas:
        faixa = faixas[cidade]
        return faixa[0] <= cep_num <= faixa[1]
    return False
