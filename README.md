# Calculadora Inteligente EBAC
Calculadora simples criada durante as aulas para realizar operações básicas (Soma, Subtração, Divisão e Multiplicação) com números reais.

Recursos necessários: 
* Terminal Ubuntu 24.04
* GitHub

## Instalando o Ubuntu 24.04

1. Para instalar o terminal Linux (Ubuntu), será necessário que você abra o terminal do windows, o PowerShell. Para fazer isso basta ir na sua Barra de Tarefas, procurar pela caixa de pesquisa e digitar **Windows PowerShell**.

2. Execute-o no **modo de administrador** (Clique com o botão direito do mouse).

3. Com ele aberto, você digitará o seguinte comando:
```
wsl --install --distribution Ubuntu-24.04

```
**E pronto! Seu terminal Linux já está pronto para ser utilizado.**

## Criando um diretório e inserindo os arquivos baixados nele

1. Primeiramente crie um novo diretório através do comando: 
```
mkdir "nome do diretório"
````
2. Acesse o diretório: 
```
cd "nome do diretório"
```
3. Dentro do diretório digite o comando para acessá-lo no explorer e cole os arquivos (o script .sh e o arquivo em python .py):
```
explorer.exe .
```
**Com isso, seus arquivos já estarão no diretório prontos para serem utilizados!**

## Executando os arquivos

1. Para executar o arquivo sh. é necessário que abra o seu terminal Ubuntu, coloque-o no seu diretório e digite o seguinte comando para torná-lo executável:

```
chmod +x calculadora_script.sh
```
2. Utilize o comando para executar o arquivo: 

```
./calculadora_script.sh
```
3. Caso você queira definir as permissões de modo com que apenas o adminstrador possa executar, ler e editar o arquivo; enquanto os outros usuários possam apenas ler e executar, digite o seguinte comando:

```
chmod 755 calculadora_script.sh
```
**_Atente-se se você possui uma senha para executar a instalação, caso não tenha, é só apertar a tecla ENTER. Caso tenha uma senha e você não lembre, segue um tutorial de como redefinir._**

## Redefinindo a senha do terminal Ubuntu

1. Abra o PowerShell e veja a distribuição que você instalou.
```
wsl -l
```
2. Acesse o usuário root da distribuição, por padrão o “root” é o principal
```
wsl -d distribution --user root
``` 
**_`exemplo: wsl -d Ubuntu-24.04 --user root`_**

3. Digite passwd seguido do nome do usuário que você deseja resetar a senha
```
passwd username
``` 
**_`exemplo: passwd rodrigo`_**

4. Digite sua nova senha!

## Código Python Documentado

Para desenvolver a calculadora, utilizei as seguintes estruturas condicionais: 
* ### **While**
  O `while` é uma estrutura de repetição que executa um bloco de código enquanto uma condição for verdadeira.

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

<br/>

* ### **If**
  A estrutura `if` é usada para executar um bloco de código se uma condição for verdadeira.
```
if operacao in (1,2,3,4):

    n1 = float(input("Digite o primeiro número: "))
    n2 = float(input("Digite o segundo número: "))
```
*Aqui também utilizei a função `float` para que a variável fosse um número real, tendo mais possibilidades de resultados durante as operações.* 

<br/>

* ### **Elif**
  O `elif` é uma abreviação de "else if", e é usado quando você tem múltiplas condições a serem verificadas. Se a condição do if for falsa, o Python verifica a condição do elif.
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
*Utilizei a função `break` para que o usuário também possa sair da calculadora quando quiser.*

<br/>

* ### **Else**
  O `else` é usado para definir um bloco de código que será executado quando todas as condições anteriores (if ou elif) forem falsas.
```
 else:
    print('Não foi possível realizar a operação, tente novamente.')
```

<br/>

* Utilizei também a função de entrada de informações `input` para que o usuário consiga interagir com o programa. E a função `print` para imprimir todas as informações recebidas.





