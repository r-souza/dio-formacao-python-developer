<div align="center">
  <img src="images/logo.webp" alt="Bootcamp Logo" style="width: 200px" /> 
</div>

# Fundamentos de Python

Cursos da seção de `Fundamentos de Python` da [Formação Python Developer] da [DIO].

Instrutor: [Guilherme Carvalho]

<h2>Conteúdo</h2>

- [Fundamentos de Python](#fundamentos-de-python)
  - [Ambiente de Desenvolvimento e Primeiros Passos com Python](#ambiente-de-desenvolvimento-e-primeiros-passos-com-python)
    - [Introdução ao Python](#introdução-ao-python)
      - [Linha do tempo](#linha-do-tempo)
  - [Conhecendo a Linguagem de Programação Python](#conhecendo-a-linguagem-de-programação-python)
    - [Tipos de Dados](#tipos-de-dados)
      - [Tipos numéricos](#tipos-numéricos)
      - [Tipos booleanos](#tipos-booleanos)
      - [Strings](#strings)
    - [Modo Interativo](#modo-interativo)
      - [Dir e Help](#dir-e-help)
    - [Variáveis](#variáveis)
    - [Constantes](#constantes)
    - [Boas Práticas](#boas-práticas)
    - [Comentários](#comentários)
    - [Conversão de Tipos](#conversão-de-tipos)
    - [Funções de Entrada e Saída](#funções-de-entrada-e-saída)
  - [Tipos de Operadores](#tipos-de-operadores)
    - [Operadores Aritméticos](#operadores-aritméticos)
      - [Ordem de Precedência](#ordem-de-precedência)
    - [Operadores de Comparação](#operadores-de-comparação)
    - [Operadores de Atribuição](#operadores-de-atribuição)
    - [Operadores Lógicos](#operadores-lógicos)
    - [Operadores de Identidade](#operadores-de-identidade)
    - [Operadores de Associação](#operadores-de-associação)

## Ambiente de Desenvolvimento e Primeiros Passos com Python

### Introdução ao Python

Python nasceu em 1989, criada por Guido Van Rossum, na Holanda. O nome é uma homenagem ao grupo de comédia britânico Monty Python.

Fortemente influenciada pela linguagem ABC, Python foi pensada para ser uma linguagem de alto nível, de fácil leitura e de fácil aprendizado.

Python é uma linguagem de programação interpretada, de script, imperativa, orientada a objetos, funcional, de tipagem dinâmica e forte.

#### Linha do tempo

 - Em 1994 foi lançada a versão 1.0, que já continha classes com herança, funções, tratamento de exceções, além de tipos de dados como dicionários e listas.
 - Em 1995 Guido lança a versão 1.2, enquanto trabalhava no CWI. 
 - Em 2000 Guido e o time de desenvolvedores da BeOpen.com lançam a versão 2.0. Nessa versão foi adicionado o `List Comprehension` e uma melhoria no coletor de lixo para remoção de referências cíclicas.
 - Em 2001 nasce a Python Software Foundation, uma organização sem fins lucrativos para promover, desenvolver e divulgar a linguagem.
 - Em 2008 é lançada a versão 3.0, que **não é compatível** com as versões anteriores. Essa versão foi criada para corrigir alguns erros de design da linguagem e melhorou a performance.

## Conhecendo a Linguagem de Programação Python

### Tipos de Dados

Os tipos servem para definir as características e comportamentos de um valor (objeto) para o interpretador.

Os tipos built-in mais comuns são:


| Categoria | Tipos                        |
| --------- | ---------------------------- |
| Texto     | str                          |
| Numérico  | int, float, complex          |
| Sequência | list, tuple, range           |
| Mapa      | dict                         |
| Coleção   | set, frozenset               |
| Booleano  | bool                         |
| Binário   | bytes, bytearray, memoryview |


#### Tipos numéricos

Os números inteiros são representados pela classe `int`, e os números reais são representados pela classe `float`.

```python
# int
print(type(1)) # <class 'int'>

# float
print(type(1.0)) # <class 'float'>
```

#### Tipos booleanos

Os tipos booleanos são representados pela classe `bool` e podem assumir os valores `True` ou `False`. Em Python, o tipo booleano é uma subclasse de `int`, onde `True` é igual a `1` e `False` é igual a `0`.

```python
print(type(True)) # <class 'bool'>
print(1 == True) # True
print(0 == False) # True
print(True + True) # 2
print(True + False) # 1
print(1 + True) # 2
print(1 + False) # 1
```

#### Strings

Strings são sequências de caracteres delimitadas por aspas simples, duplas ou triplas. Em Python, strings são imutáveis.

```python
print(type('string')) # <class 'str'>
print(type(''string'') # <class 'str'>
print(type('''string''')) # <class 'str'>
print(type("string")) # <class 'str'>
print(type(""string"")) # <class 'str'>
print(type("""string""")) # <class 'str'>
```

### Modo Interativo

O modo interativo é uma forma de executar comandos Python diretamente no terminal. Para entrar no modo interativo, basta digitar `python` no terminal.

```python
$ python
Python 3.8.5 (default, Jan 27 2021, 15:41:15)
[GCC 9.3.0] on linux
Type "help", "copyright", ...
>>> print('Hello World!')
Hello World!
>>> 1 + 1
2
```

#### Dir e Help

O comando `dir` retorna uma lista de atributos e métodos disponíveis para um objeto. 

```python
>>> dir('string')
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
```

O comando `help` retorna a documentação de um objeto.

```python
>>> help('string'.capitalize)
Help on built-in function capitalize:
capitalize() method of builtins.str instance
    Return a capitalized version of the string.
    
    More specifically, make the first character have upper case and the rest lower case.
```

### Variáveis

Variáveis são espaços na memória do computador que armazenam valores. Em Python, as variáveis são criadas no momento em que são atribuídas, e não precisam ser declaradas previamente.

```python
>>> x = 1
>>> print(x)
1
>>> x + 10
11
```

```python
age = 35
name = 'Rodrigo de Souza'
print(f'My name is {name} and I am {age} years old.')
```

Também é possível atribuir valores a múltiplas variáveis em uma única linha.

```python
age, name = 35, 'Rodrigo de Souza'
print(f'My name is {name} and I am {age} years old.')
```

Em Python, os tipos de dados são definidos automaticamente de acordo com o valor atribuído à variável.

```python
>>> x = 1
>>> type(x)
<class 'int'>
>>> x = 1.0
>>> type(x)
<class 'float'>
>>> x = '1'
>>> type(x)
<class 'str'>
```

### Constantes

Constantes são variáveis cujos valores não podem ser alterados durante a execução do programa. Em Python, não existe um tipo de dado específico para constantes, mas por convenção, constantes são escritas em letras maiúsculas.

```python
PI = 3.14
STATES = ['São Paulo', 'Rio de Janeiro', 'Minas Gerais']
DEBUG = True
```

### Boas Práticas

- Use nomes em snake_case.
- Use nomes de variáveis descritivos, que façam sentido.
- Use nomes de variáveis em letras minúsculas.
- Use nome de constantes em letras maiúsculas.

Veja mais sobre no [PEP 8], que é o guia de estilo oficial do Python. 

### Comentários

Comentários são trechos de código que não são executados pelo interpretador Python. Em Python, comentários são escritos com o caractere `#`.

```python
# This is a comment
print('Hello World!') # This is another comment
```

### Conversão de Tipos

Em Python, é possível converter um tipo de dado em outro usando os construtores de tipos, como `int()`, `float()` e `str()`.

```python
>>> int(1.0)
1
>>> float(1)
1.0
>>> int('1')
1
>>> str(1)
'1'
```

### Funções de Entrada e Saída

Em Python, a função `input()` é usada para receber dados do usuário. Por padrão, a função `input()` retorna uma string, mas é possível converter o valor recebido para outros tipos de dados.

```python
>>> name = input('What is your name? ')
What is your name? Rodrigo
>>> print(f'Hello, {name}!')
Hello, Rodrigo!
```

Para receber um número do usuário, é necessário converter o valor recebido para o tipo `int` ou `float`.

```python
>>> age = int(input('How old are you? '))
How old are you? 35
>>> age = age + 10
>>> print(f'You are {age} years old.')
You are 45 years old.
```

A função `print()` é usada para exibir dados na tela. Ela recebe um argumento obrigatório do tipo varargs, que é uma lista de valores separados por vírgula. Além disso, a função `print()` também aceita 4 argumentos opcionais: `sep`, `end`, `file` e `flush`. Todos os objetos são convertidos para string, separados por `sep` e exibidos na tela, seguidos por `end`.

```python
>>> print('Hello', 'World', sep=', ', end='!')
Hello, World!
```

## Tipos de Operadores

### Operadores Aritméticos

| Operador | Descrição           |
| -------- | ------------------- |
| `+`      | Adição              |
| `-`      | Subtração           |
| `*`      | Multiplicação       |
| `/`      | Divisão             |
| `//`     | Divisão inteira     |
| `%`      | Resto da divisão    |
| `**`     | Exponenciação       |
| `()`     | Alterar precedência |

#### Ordem de Precedência

Assim como na matemática, em Python, a ordem de precedência dos operadores aritméticos é a seguinte:

1. Parênteses
2. Exponenciação
3. Multiplicação, Divisão, Divisão Inteira e Resto da Divisão
4. Adição e Subtração

```python
>>> 5 + 3 * 2
11
>>> (5 + 3) * 2
16
>>> 10 ** 2 * 2
200
>>> 10 ** (2 * 2)
10000
``` 

Quando dois operadores possuem a mesma precedência, a ordem de execução é da esquerda para a direita.

```python
>>> 10 / 2 * 3
15.0
>>> 2 * 3 / 10
0.6
```

### Operadores de Comparação

| Operador | Descrição          |
| -------- | ------------------ |
| `==`     | Igual              |
| `!=`     | Diferente          |
| `>`      | Maior que          |
| `<`      | Menor que          |
| `>=`     | Maior ou igual que |
| `<=`     | Menor ou igual que |

```python
>>> 10 == 10
True
>>> 10 != 10
False
>>> 10 > 10
False
>>> 10 < 10
False
>>> 10 >= 10
True
>>> 10 <= 10
True
```

### Operadores de Atribuição

| Operador | Descrição                     |
| -------- | ----------------------------- |
| `=`      | Atribuição                    |
| `+=`     | Adição e atribuição           |
| `-=`     | Subtração e atribuição        |
| `*=`     | Multiplicação e atribuição    |
| `/=`     | Divisão e atribuição          |
| `//=`    | Divisão inteira e atribuição  |
| `%=`     | Resto da divisão e atribuição |
| `**=`    | Exponenciação e atribuição    |

```python
>>> x = 10
>>> x += 1
>>> x
11
>>> x -= 1
>>> x
10
>>> x *= 2
>>> x
20
>>> x /= 2
>>> x
10.0
>>> x //= 2
>>> x
5.0
>>> x %= 2
```

### Operadores Lógicos

| Operador | Descrição |
| -------- | --------- |
| `and`    | E         |
| `or`     | Ou        |
| `not`    | Não       |

```python
>>> True and True
True
>>> True and False
False
>>> False and False
False
>>> True or True
True
>>> True or False
True
>>> False or False
False
>>> not True
False
>>> not False
True
```

Outros exemplos:

```python
>>> 10 > 5 and 10 > 15
False
>>> 10 > 5 or 10 > 15
True
>>> not 10 > 5
False
```


### Operadores de Identidade

| Operador | Descrição |
| -------- | --------- |
| `is`     | É         |
| `is not` | Não é     |

```python
>>> a = 10
>>> b = 10
>>> a is b
True
>>> 10 is not 10
False
>>> id(a)
140723983796240
>>> id(b)
140723983796240
```


### Operadores de Associação

| Operador | Descrição |
| -------- | --------- |
| `in`     | Em        |
| `not in` | Não em    |

```python
>>> classes = ['Python', 'Java', 'C#']
>>> 'Python' in classes
True
>>> fruits = ['Apple', 'Banana', 'Orange']
>>> 'Melon' not in fruits
True
>>> 'a' in 'aeiou'
True
>>> 'z' in 'aeiou'
False
```


[DIO]: https://dio.me
[Formação Python Developer]: https://web.digitalinnovation.one/track/formacao-python-developer
[Guilherme Carvalho]: https://github.com/guicarvalho
[PEP 8]: https://www.python.org/dev/peps/pep-0008/#naming-conventions