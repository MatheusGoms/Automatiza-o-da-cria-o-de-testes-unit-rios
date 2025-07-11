Exemplo de Implementação
Código Base
Vamos supor que o código fornecido seja o seguinte:

def soma(a, b):
    """Retorna a soma de dois números."""
    return a + b 


./Geração de Teste
O modelo de linguagem, com o suporte do LangChain, gera automaticamente um arquivo de teste, como este:

import pytest
from my_module import soma

def test_soma_com_numeros_positivos():
    assert soma(2, 3) == 5

def test_soma_com_numeros_negativos():
    assert soma(-2, -3) == -5

def test_soma_com_zero():
    assert soma(0, 5) == 5

def test_soma_com_mistos():
    assert soma(-2, 3) == 1


Pipeline com LangChain
Exemplo de como LangChain pode ser usado para estruturar a interação com o modelo da Azure:

from langchain.chat_models import AzureChatOpenAI
from langchain.prompts import ChatPromptTemplate

# Configuração do modelo
chat = AzureChatOpenAI(deployment_name="gpt-4", temperature=0.7)

# Prompt para geração de teste
prompt_template = ChatPromptTemplate.from_template("""
Você é um gerador de testes unitários. Analise a função abaixo e crie testes unitários para ela usando pytest.

Código:
{codigo}

Responda apenas com o código dos testes gerados.
""")

# Código de entrada
codigo_fonte = """
def soma(a, b):
    return a + b
"""

# Geração do prompt
prompt = prompt_template.format_prompt(codigo=codigo_fonte)

# Obtenção da resposta do modelo
resposta = chat(prompt.to_messages())
print(resposta.content)
