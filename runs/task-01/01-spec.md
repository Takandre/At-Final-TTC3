# Especificação do Produto — task-01

## Objetivo

Criar um utilitário CLI simples em Python, `calc_cli.py`, capaz de executar as quatro operações aritméticas básicas entre dois números:

- soma;
- subtração;
- multiplicação;
- divisão.

O programa deve ser fácil de executar pela linha de comando e deve informar o resultado ou um erro compreensível quando a operação não puder ser realizada.

## Escopo funcional

### Entrada

O utilitário deve receber pela linha de comando:

1. o primeiro número;
2. a operação;
3. o segundo número.

A operação deve aceitar uma representação clara e documentada, preferencialmente os símbolos `+`, `-`, `*` e `/` (podendo também haver aliases textuais, se definidos na implementação).

Os números devem aceitar valores inteiros e decimais, incluindo valores negativos.

### Operações e saída

- `+`: retorna o primeiro número somado ao segundo;
- `-`: retorna o primeiro número subtraído do segundo;
- `*`: retorna o primeiro número multiplicado pelo segundo;
- `/`: retorna o primeiro número dividido pelo segundo.

O resultado deve ser escrito na saída padrão, sem exigir interação adicional. A implementação deve preservar precisão adequada para os valores fornecidos, usando o tipo numérico apropriado.

### Divisão por zero

Quando a operação for divisão e o segundo número for zero, o programa não deve lançar traceback nem produzir resultado inválido. Deve:

- exibir uma mensagem de erro clara na saída de erro;
- terminar com código de saída diferente de zero.

## Validação e erros

O CLI deve rejeitar entradas ausentes, operações desconhecidas e valores que não possam ser convertidos em números, apresentando mensagens compreensíveis e código de saída diferente de zero. A interface deve exibir ajuda/uso quando solicitada (por exemplo, com `--help`).

## Critérios de aceitação

1. `python calc_cli.py 2 + 3` produz `5` e termina com sucesso.
2. `python calc_cli.py 7 - 4` produz `3` e termina com sucesso.
3. `python calc_cli.py 6 '*' 5` produz `30` e termina com sucesso.
4. `python calc_cli.py 8 / 2` produz `4` (ou representação numérica equivalente) e termina com sucesso.
5. Uma divisão como `python calc_cli.py 8 / 0` informa divisão por zero e termina com código diferente de zero.
6. Valores decimais e negativos são aceitos, por exemplo `python calc_cli.py -2.5 '*' 4`.
7. Operação inválida e argumentos ausentes resultam em erro compreensível e código diferente de zero.
8. `python calc_cli.py --help` apresenta instruções de uso e as operações suportadas.
9. O código deve ser executável com Python 3, sem dependências externas obrigatórias.

## Fora do escopo

- interface gráfica ou web;
- histórico de operações;
- armazenamento de dados;
- cálculo com mais de dois operandos;
- variáveis, expressões arbitrárias ou avaliação de código;
- requisitos de empacotamento/publicação.

## Entregáveis esperados da implementação

- `calc_cli.py` na raiz do projeto;
- testes automatizados ou verificações equivalentes cobrindo as quatro operações, divisão por zero e validações principais;
- documentação breve de uso, se necessário para tornar a interface escolhida inequívoca.