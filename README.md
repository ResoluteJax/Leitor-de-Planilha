div align="center"
img src="![img2](https://github.com/ResoluteJax/Leitor-de-Planilha/assets/70527896/3bc269cc-e033-45f4-bcf9-09a1c897254a)
![img1](https://github.com/ResoluteJax/Leitor-de-Planilha/assets/70527896/7a6ea613-1164-4e0d-b0fa-35453071eb0d)" width="200px" /
/div

# Leitor-de-Planilha
Guia de Teste para a Aplicação de Análise de Planilhas Excel
Este guia fornecerá instruções passo a passo para testar com sucesso a aplicação de análise de planilhas Excel. Esta aplicação permite carregar arquivos Excel, processá-los e exibir os resultados em uma interface web.

Pré-requisitos
Antes de começar, certifique-se de que você tenha o seguinte:

Python 3.x instalado no seu sistema.
Um ambiente virtual configurado (recomendado).
Flask e pandas instalados no ambiente virtual. Você pode instalá-los usando pip install Flask pandas.
Passo 1: Clonar ou Baixar o Repositório
Clone este repositório do GitHub para o seu sistema ou faça o download como um arquivo ZIP e extraia-o em um diretório de sua escolha.

bash
git clone https://github.com/seuusuario/seurepositorio.git
Passo 2: Navegar até o Diretório do Projeto
Abra o terminal e navegue até o diretório do projeto:

bash
cd caminho/para/o/diretorio-do-projeto
Passo 3: Configurar o Ambiente Virtual (Opcional)
Se você estiver usando um ambiente virtual, ative-o:

bash
source nome-do-seu-ambiente-virtual/bin/activate
Passo 4: Executar a Aplicação
Execute a aplicação Flask:

bash
python app.py
Você verá uma mensagem indicando que a aplicação está em execução em um servidor local.

Passo 5: Acessar a Aplicação
Abra um navegador da web e acesse http://localhost:5000 para acessar a aplicação.

Passo 6: Testar a Aplicação
Aqui estão algumas etapas de teste:

Clique no botão "Escolher Arquivo" para selecionar um arquivo Excel válido (.xls ou .xlsx).
Certifique-se de que o arquivo Excel selecionado contenha as colunas necessárias, como "Hora 1" e "Hora 2".
Envie o arquivo selecionado para a aplicação.
A aplicação processará o arquivo e redirecionará você para a página de resultados.
Passo 7: Verificar Resultados
Na página de resultados, você verá uma tabela com os dados processados a partir do arquivo Excel. Além disso, as informações da coluna "B" da linha 1 e 2 (se necessário) estarão acima da tabela.

Passo 8: Encerrar a Aplicação
Para encerrar a aplicação, volte ao terminal onde a aplicação está sendo executada e pressione Ctrl + C.

Conclusão
Você concluiu com sucesso o teste da aplicação de análise de planilhas Excel. Agora você pode usar essa aplicação para carregar, processar e analisar planilhas Excel de acordo com suas necessidades. Certifique-se de ter um arquivo Excel válido e com as colunas corretas para obter resultados precisos. Se encontrar algum problema, verifique as mensagens de erro e assegure-se de que o arquivo Excel atenda aos requisitos esperados pela aplicação.
