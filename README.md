# FIAP - Faculdade de Informática e Administração Paulista

<p align="center">
<a href= "https://www.fiap.com.br/"><img src="assets/logo-fiap.png" alt="FIAP - Faculdade de Informática e Admnistração Paulista" border="0" width=40% height=40%></a>
</p>

<br>

# Nome do projeto

## Nome do grupo

## 👨‍🎓 Integrantes: 
- Kild Bezerra Fernandes
- Amandha Nery Cumplido de Souza Neves
- Daniel Pinto Barros
- Yuri Santana Cordeiro

## 👩‍🏫 Professores:
### Tutor(a) 
- <a href="https://www.linkedin.com/company/inova-fusca">Nome do Tutor</a>
### Coordenador(a)
- <a href="https://www.linkedin.com/company/inova-fusca">Nome do Coordenador</a>


## 📜 Descrição

## Projeto: Sistema de Gestão e Otimização da Colheita de Cana-de-Açúcar

   A cana-de-açúcar é uma das culturas mais importantes para a economia brasileira, posicionando o país como líder mundial na produção. Apesar dos sucessivos recordes de colheita, com cifras que ultrapassam 620 milhões de toneladas em algumas safras, as perdas durante o processo de colheita ainda representam um desafio significativo para os produtores. Estimativas indicam que essas perdas podem chegar a até 15% quando a colheita é realizada mecanicamente, contrastando com os menos de 5% de perdas na colheita manual. Esse cenário não apenas impacta a rentabilidade dos agricultores, mas também afeta a produtividade do setor e a arrecadação governamental.

   Diante desse contexto, apresentamos um sistema inovador de gestão da safra que visa reduzir as perdas na colheita de cana-de-açúcar e otimizar a qualidade do produto final. O programa proposto permite o registro detalhado de informações essenciais, como safra, tipo de cultura e talhão. Além disso, oferece funcionalidades para monitorar a incidência de pragas e o uso de defensivos agrícolas em cada área cultivada.

## Funcionalidades do Sistema:

 - Registro de Safra e Cultura: Permite ao produtor cadastrar informações específicas sobre cada safra e tipo de cultura, facilitando o acompanhamento e gerenciamento ao longo do ciclo produtivo.

 - Monitoramento de Talhões: O sistema possibilita o controle individualizado de cada talhão, permitindo a identificação de áreas com maior incidência de problemas e a tomada de decisões mais precisas.

 - Gestão de Pragas e Defensivos: Os produtores podem adicionar registros sobre pragas identificadas e os defensivos utilizados. Cada praga adicionada aumenta a pontuação da safra, indicando um potencial risco à qualidade. Por outro lado, o uso de defensivos apropriados diminui essa pontuação, refletindo as ações tomadas para mitigar os impactos.

 - Sistema de Pontuação Inteligente: A pontuação atribuída serve como um indicador da qualidade da safra. Pragas não tratadas também aumentam a pontuação, sinalizando um alerta crítico. Quanto menor a pontuação total, melhor a qualidade da safra, o que pode ser traduzido em produtos finais de maior valor no mercado.

## Benefícios do Sistema:

 - Melhoria na Qualidade da Safra: Ao fornecer um acompanhamento detalhado e em tempo real, o sistema auxilia os produtores a identificar rapidamente problemas e implementar soluções eficazes, resultando em uma safra de melhor qualidade.

 - Otimização dos Lucros: Mesmo com as perdas inevitáveis durante a colheita, a qualidade superior da safra pode justificar preços mais altos no mercado, compensando a porcentagem do lucro perdida. Produtos com menor pontuação tendem a ser mais valorizados, permitindo a recuperação do investimento e potencializando a rentabilidade.

 - Redução de Perdas na Colheita: Com informações precisas e estratégias bem definidas, os produtores podem otimizar o uso das colhedoras mecânicas, minimizando as perdas que atualmente chegam a até 15% da produção.

 - Planejamento Estratégico: O sistema facilita o planejamento desde o plantio até a colheita, incluindo a definição do momento ideal para cada etapa, alinhado com as melhores práticas agrícolas.

## Impacto no Setor Agrícola:

 - A implementação deste sistema pode significar uma transformação significativa no setor sucroalcooleiro brasileiro. Ao empoderar os produtores com ferramentas tecnológicas avançadas, não apenas se promove a eficiência operacional, mas também se contribui para a sustentabilidade econômica e ambiental do agronegócio. A redução das perdas e a melhoria na qualidade da safra têm o potencial de gerar ganhos expressivos, estimados em milhões de reais, beneficiando agricultores, investidores e a economia nacional como um todo.


## 📁 Estrutura de pastas

Dentre os arquivos e pastas presentes na raiz do projeto, definem-se:

- <b>.github</b>: Nesta pasta estão os arquivos de configuração específicos do GitHub que ajudam a gerenciar e automatizar processos no repositório.

- <b>assets</b>: Aqui estão os arquivos relacionados a elementos não-estruturados deste repositório, como imagens.

- <b>config</b>: Aqui estão arquivos de configuração que são usados para definir parâmetros e ajustes do projeto.

- <b>document</b>: Aqui estão todos os documentos do projeto que as atividades poderão pedir. Na subpasta "other", adicione documentos complementares e menos importantes.

- <b>scripts</b>: Aqui estão scripts auxiliares para tarefas específicas do seu projeto. Exemplo: deploy, migrações de banco de dados, backups.

- <b>src</b>: Todo o código fonte criado para o desenvolvimento do projeto ao longo das 7 fases.

- <b>README.md</b>: arquivo que serve como guia e explicação geral sobre o projeto (o mesmo que você está lendo agora).

## 🔧 Como executar o código

Pré-requisitos
Antes de iniciar a instalação, certifique-se de que sua máquina possui os seguintes softwares instalados:

Python 3.6 ou superior
Pip (gerenciador de pacotes do Python)
Virtualenv (opcional, mas recomendado)
Docker
Docker Compose
Git
Instalação
Siga os passos abaixo para configurar e executar o projeto em sua máquina local.

# 1. Clonar o Repositório
Abra o terminal e execute:

`git clone https://github.com/KildFernandes/FiapMsf`

Navegue até o diretório do repositório
cd FiapMsf

# 2. Instalar as Dependências
Instale as dependências necessárias usando o pip:

`pip install -r requirements.txt`

# 3. Configurar o Banco de Dados com Docker
Entre no diretório de scripts e inicie o banco de dados usando o Docker Compose:

Navegue até o diretório de scripts

`cd scripts`

Inicie o banco de dados em segundo plano

`docker-compose up -d`

# 4. Executar o Programa
Volte ao diretório raiz e navegue até o diretório src para executar o programa:

`cd ..`

## Navegue até o diretório src

`cd src`

## Execute o programa principal

`python3 main.py`

 Dica: Certifique-se de que o Docker está em execução e que todos os contêineres necessários estão ativos antes de executar o programa.

Uso
Após executar main.py, o programa iniciará e você poderá interagir com o sistema conforme as funcionalidades implementadas. As principais características incluem:

Cadastro de Safras e Culturas
Gerenciamento de Talhões
Monitoramento de Pragas e Defensivos
Visualização da Pontuação da Safra



## 📋 Licença

<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1"><p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/agodoi/template">MODELO GIT FIAP</a> por <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://fiap.com.br">Fiap</a> está licenciado sobre <a href="http://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">Attribution 4.0 International</a>.</p>


