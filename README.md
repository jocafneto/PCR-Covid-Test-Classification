# PCR-Covid-Test-Classification

## **Empresa:**

**PCR Covid Tester**


## **Qual o problema de negócio?**

O desafio consiste na construção de um modelo de aprendizado de máquina para realizar a discriminação dos dados espectrais de COVID-19 em relação ao grupo controle (casos positivos e negativos).


## **Sobre a Empresa?**

A PCR Covid Tester é uma empresa de biotecnologia que utiliza Inteligência Artificial para predizer se um funcionário de uma outra empresa está com Covid ou não, através de amostras extraídas dentro da própria empresa de origem usando técnica de **Espectroscopia do Infravermelho Próximo (NIR)**.


## **Objetivo do desafio?**

Ao final, devem ser apresentados os resultados obtidos explicando os critérios de decisão para a escolha do melhor modelo.


## **Sobre os Dados:**

A **espectroscopia do infravermelho próximo (NIR)** é uma técnica experimental que se baseia na utilização da luz para estudar a composição, a estrutura e as propriedades da matéria.
De forma prática, é emitido diversos feixes de luz no material, utilizando diversos
comprimentos de onda no espectro do infravermelho. **Como resultado**, temos a **resposta
dos diferentes comprimentos de onda para cada amostra**.

No total a base de **dados** contém **309 amostras** com **899 colunas**, sendo cada **coluna**
representada pela **quantidade de luz refletida por cada faixa de comprimento de onda**.
**Como rótulo**, existe uma **coluna indicando o resultado do teste RT-PCR para cada amostra**,
tendo **dois rótulos possíveis**: **“Controle”**, para os dados que obtiveram **resultado negativo**
para o **teste RT-PCR**, e a classe **“Covid”**, para as amostras que obtiveram **resultado positivo**
no teste.


## **Que tipos de perguntas devemos responder?**

**1)** Quais são as amostras que tiveram **resultado positivo** para o **teste RT-PCR**?

**2)** Quais tiveram **resultado negativo**?
