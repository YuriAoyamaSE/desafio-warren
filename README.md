# Desafio de Programação – Warren Tech Academy

## INFORMAÇÕES E INSTRUÇÕES
A linguagem utilizada foi Python 3 (v 3.9.10), editada através do Visual Studio Code.

Houve um cuidado de seguir normas de boas práticas da linguagem, como uso de “snake case”, legibilidade do código, organização, entre outros recomendados pela comunidade Python.

Evitou-se a utilização de módulos externos, aplicando apenas aqueles já pertencentes à linguagem Python. Como os desafios foram simples, não houve necessidade de gerar complexidades como trabalhar com classes (orientação a objeto). Os códigos foram organizados em funções para melhor legibilidade e organização, permitindo também melhor controle para alterações e erros. Optou-se ainda por escrever de forma mais legível em vez de “economizar” em linhas de código.

Após baixar os arquivos, é necessário que a máquina possua o [Python]( https://www.python.org/downloads/) instalado para a execução. O código poderá ser executado pelo prompt (usando o comando python no arquivo), utilizando um editor (como VScode, PyCharm, etc) ou como se fosse um executável pelo python (bastando um clique duplo no arquivo).

O terceiro meio (executar diretamente o arquivo) é mais simples e rápido. Em vista disto, em todos os códigos foi adicionado um módulo com o único intuito de criar um atraso de 10 segundos na tela para que o usuário possa analisar o resultado (função “sleep” do módulo “time”). Sem isto, ao executar o arquivo, a janela aberta iria fechar logo que o código terminar.

## DESAFIO 01:
Alguns números inteiros positivos n possuem uma propriedade na qual a soma de n + reverso(n) resultam em números ímpares. Por exemplo, 36 + 63 = 99 e 409 + 904 = 1313. Considere que n ou reverso(n) não podem começar com 0. 

Existem 120 números reversíveis abaixo de 1000. 

Construa um algoritmo que mostre na tela todos os números n onde a soma de n + reverso(n) resultem em números ímpares que estão abaixo de 1 milhão.

### Observação:
Apesar de ser mais simples, foi o desafio que demorei mais para concluir por causa da interpretação do quesito. O primeiro parágrafo traz regras simples. O segundo já mostra uma amostra estranha ao determinar que “Existem 120 números reversíveis abaixo de 1000”. Considerando as regras passadas, haveria 440 números reversíveis. 
No terceiro parágrafo é dado o desafio em produzir o código com o limite em 1 milhão, mas não em relação aos números reversíveis, mas quanto a “soma de n + reverso(n) resultem em números ímpares”. Se esta interpretação for aplicada no segundo parágrafo, a contagem reduziria para 200 números, ainda bem acima de 120. 
Enviei dois e-mails para o suporte questionando se poderia ter havido algum erro de edição (já que houve a liberação do desafio antes da data e com erro de digitação sobre a data final de entrega). Todavia, não houve resposta. 
Válido ainda ressaltar que o terceiro parágrafo possui duplo sentido na expressão “que estão abaixo de 1 milhão”, pois pode se referir tanto aos “números ímpares” (soma) quanto a “números n”.
Assim, não havendo resposta dos e-mails e precisando entregar um código, decidi implementar o código seguindo as regras formalizadas no parágrafo primeiro e com os requisitos do parágrafo terceiro, ignorando a afirmação do segundo parágrafo. A interpretação usada no terceiro foi de que o limite de 1 milhão se refere ao objeto mais próximo: “números ímpares”.

### Sobre o código:
Todos os códigos irão iniciar pelo escopo de execução gerado pela estrutura: if __name__ == "__main__" (linha 22 do desafio_01).

Primeiro, cria-se um parâmetro para limitar o universo que será feita a verificação (limite = 1_000_000).

Uma lista é gerada para ser impressa como resposta do desafio, obtendo o resultado da função listar_reversiveis(), que é a função principal do programa, na qual um laço irá percorrer os números para fazer a checagem. 

Dentro do laço, haverá uma validação inicial do número, feita pela função valida_numero(), que irá confirmar que o número atual do laço não termina em “0” – se ele terminar em “0”, seu inverso irá começar com “0”, o que o torna inválido de acordo com as instruções do desafio.

Interessante destacar o fato de a linguagem Python não identificar números em strings como inteiros e que a utilização de string facilitará o manuseio dos procedimentos por ser iterável. Assim, usa-se a função str() para tal finalidade no código.

Caso não passe pela validação, o laço pula para o inteiro seguinte. Caso passe, se faz a soma com o seu inverso, que é obtido através da função reverte_numero(), que transformar a variável em string, faz um tratamento de inversão e o retorna. 

Passa-se para a validação final (soma com resultado ímpar) e adiciona os resultados válidos em uma lista, que será retornada para a impressão final do código. Uma vez que não houve a determinação de como deveria ser o output do programa, optou-se por devolver uma lista de números para que fosse uma visualização mais condensada, visto o número grande de resultados. Ademais, a utilização de uma lista para guardar o resultado é útil para manipular as informações mais facilmente (como contagem de elementos ou comparações).

## DESAFIO 02
Um professor de programação, frustrado com a falta de disciplina de seus alunos, decidi cancelar a  aula  se  menos  de x alunos  estiverem  presentes  quando  a  aula  for  iniciada.  O  tempo  de chegada varia entre: 

• Normal: tempoChegada <= 0 

• Atraso: tempoChegada > 0 

Construa  um  algoritmo  que  dado  o  tempo  de  chegada  de  cada  aluno  e  o  limite x de  alunos presentes, determina se a classe vai ser cancelada ou não ("Aula cancelada” ou “Aula normal”). 

Exemplo: 

Entrada de dados: 

x = 3 

tempoChegada = [-2, -1, 0, 1, 2] 

Saída de dados: 

Aula normal. 

Explicação: 

Os três primeiros alunos chegaram no horário. Os dois últimos estavam atrasados. O limite é de três alunos, portanto a aula não será cancelada.

### Sobre o código:
Assim como o anterior, a execução se inicia na linha 15. O código começa com o armazenamento das entradas que serão usadas como parâmetros.

A função input() do Python recebe a entrada como string. Assim, usa-se a função string_para_lista() para fazer um tratamento da variável e a transformar em uma lista de inteiros. Para isto, primeiro se remove os colchetes, separa os elementos pelas vírgulas e retorna a lista após transformar cada elemento em um inteiro (usando a função map()).

Com os parâmetros já readequados, usa-se a função validar_aula() para fazer a contagem dos alunos não atrasados e verificar se o mínimo exigido foi atingido. A contagem é feita com a estrutura sum([x <= 0 for x in tempo_chegada]), onde um laço irá ser feito com o tempo_chegada, verificando cada elemento e retornando um resultado booleano (True se o aluno não atrasou, False se atrasou). 

Já a função sum() irá fazer o somatório dos resultados booleanos, onde o Python reconhece True como 1 e False como 0. Assim, o sum() se torna um contador de resultados válidos (de alunos que não atrasaram) e é impressa resposta de acordo com tal verificação. É interessante destacar que não há retorno na função validar_aula() e que ela já executa a impressão.

## DESAFIO 03
Dado um vetor de números e um número n. Determine a soma com o menor número de elementos entre os números do vetor mais próxima de n e também mostre os elementos que compõem a soma. Para criar a soma, utilize qualquer elemento do vetor uma ou mais vezes. 

Exemplo: 

Entrada de dados: 

N = 10 

V = [2, 3, 4] 

Saída de dados: 

10 

[2, 4, 4] 

[3, 3, 4] 

Explicação: 

Se N = 10 e V = [2, 3, 4] você pode utilizar as seguintes soma: [2, 2, 2, 2, 2], [2, 2, 3, 3], [2, 4, 4] ou [3, 3, 4]. Como a quantidade de elementos em [2, 4, 4] e [3, 3, 4] é igual, os dois conjuntos devem ser mostrados

### Sobre o código:
Seguindo padrão, a execução se inicia na linha 29 e logo se pede as entradas do valor de N (já sendo transformado em uma variável de inteiro), bem como o vetor.


O vetor passa por um tratamento com a função string_para_lista(), igualmente ao Desafio 02 (inclusive é utilizada a mesma função). Além disso, é usada a função set(), para "limpar" o vetor de números repetidos. Por exemplo, se for passado um vetor [2,2,4] irá ser considerado como [2,4]. Casoisto não seja feito, quando gerar as combinações, poderá ser considerado que os elementos do vetor[0] e vetor[1] são diferentes, apesar de terem o mesmo valor. Assim, iria duplicar a quantidade de respostas imprimindo [2,4,4] duas vezes, uma para cada valor 2.

Com os parâmetros ajustados, executa-se a função elementos_mínimos(), que é a principal função do código.

São inicializadas duas variáveis, um contador e uma lista vazia que servirá para o retorno da função. Um laço while é criado, no qual será incrementado o contador e a cada etapa irá gerar combinações (com repetição de elementos) dos números do vetor de entrada. O contador irá servir como parâmetro para a quantidade de elementos das combinações possíveis em cada laço efetuado.

Para efetuar as combinações foi utilizada a função combinations_with_replacement() do módulo itertools.

Apesar de não ter sido exigido no desafio, foi criado uma função de validação chamada validar_combinacao(). Apesar do código funcionar sem ela, para evitar a ocorrência de um laço infinito, esta função irá verificar a possibilidade ou não de um retorno válido para o desafio de acordo com os parâmetros de entrada. Para isto, ela irá comparar o somatório dentro de cada combinação gerada. Caso todos os somatórios resultem um número superior ao valor N, temos que seria impossível obter o número N com a soma dos elementos do vetor (por exemplo, pode ser o caso de passar um vetor com todos os elementos maiores do que N ou o N ímpar e um vetor de apenas números pares). Assim, será levantado uma mensagem de erro e o programa se encerrará.

Passada a validação, um laço “for” é utilizado para percorrer cada combinação gerada e verificar se a soma é igual ao número N, adicionando a uma lista inicializada vazia. Se a lista for preenchida, irá ser retornada, partindo para a impressão dos dados de saída (linhas 34 e 35). Caso contrário, passa-se para o próximo laço do while, aumentado o contador e, assim, também se aumenta a quantidade de elementos a usar nas combinações. 
