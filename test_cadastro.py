from cadastro import valida_cep

def test_cep_sorocaba():
    assert valida_cep("18050-100", "Sorocaba") == True

def test_cep_capela():
    assert valida_cep("18195-000", "Capela do Alto") == True

def test_cep_sao_roque():
    assert valida_cep("18130-020", "Sao Roque") == True

def test_cep_votorantim_erro():
    assert valida_cep("19000-000", "Votorantim") == False
