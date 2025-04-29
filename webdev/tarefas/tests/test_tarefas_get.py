from django.test import Client
from django.urls import reverse
import pytest
from pytest_django.asserts import assertContains

@pytest.fixture
def resposta(client):
                         # Nome do App: Nome da view
    resp = client.get(reverse('tarefas:home'))
    return resp

def test_status_code(resposta):
    return resposta.status_code == 200


def test_formulario_presente(resposta):
    assertContains(resposta, "<form")

def test_botao_salvar_present(resposta):
    assertContains(resposta, '<button type="submit"')
