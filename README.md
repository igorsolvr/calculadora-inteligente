# Calculadora Inteligente EBAC
  Calculadora simples criada durante as aulas para realizar operações básicas (Soma, Subtração, Divisão e Multiplicação) com números reais.

Recursos necessários: 
* Terminal Ubuntu 22.04
* GitHub

  Para executar o arquivo sh. é necessário que abra o seu terminal, coloque-o no seu diretório e em seguida digite o seguinte comando para torná-lo executável:

```
chmod +x calculadora_script.sh
```
  Após realizar isso, utilize o comando para executar o arquivo: 

```
./calculadora_script.sh
```
  Caso você queira definir as permissões de modo com que apenas o adminstrador possa executar, ler e editar o arquivo; enquanto os outros usuários possam apenas ler e executar, digite o seguindo comando:

```
chmod 755 calculadora_script.sh
```

## Código Python Documentado

Para desenvolver a calculadora, utilizei as seguintes estruturas condicionais: 
* ### **While**
  O while é uma estrutura de repetição que executa um bloco de código enquanto uma condição for verdadeira.

```
while True:
  print("Escolha uma operação:\n")
  print("1 - Soma")
  print("2 - Subtração")
  print("3 - Multiplicação")
  print("4 - Divisão")
  print("\n5 - SAIR")
  operacao = int(input(""))
```

* ### **If**
  A estrutura if é usada para executar um bloco de código se uma condição for verdadeira.
```
if operacao in (1,2,3,4):

    n1 = float(input("Digite o primeiro número: "))
    n2 = float(input("Digite o segundo número: "))
```
*Aqui também utilizei a função **float** para que a variável fosse um número real, tendo mais possibilidades de resultados durante as operações.* 

* ### **Elif**
  O elif é uma abreviação de "else if", e é usado quando você tem múltiplas condições a serem verificadas. Se a condição do if for falsa, o Python verifica a condição do elif.
```
if operacao == 1:
    print("\nO Resultado da soma é: ", n1 + n2)
  elif operacao == 2:
    print("\nO Resultado da subtração é: ", n1 - n2)
  elif operacao == 3:
    print("\nO Resultado da multiplicação é: ", n1 * n2)
  elif operacao == 4:
    print("\nO Resultado da divisão é: ", n1 / n2)
  elif operacao == 5:
    print("\nObrigado por utilizar a nossa calculadora!")
    break
```
*Nesse caso também utilizei a função **break** para que o usuário também possa sair da calculadora quando quiser.* 

* ### **Else**
  O else é usado para definir um bloco de código que será executado quando todas as condições anteriores (if ou elif) forem falsas.
```
 else:
    print('Não foi possível realizar a operação, tente novamente.')
```







