<div align="center">
  <img src="images/logo.webp" alt="Bootcamp Logo" style="width: 200px" /> 
</div>

# Aprendendo Estruturas de Dados com Python

Cursos da seção de `Aprendendo Estruturas de Dados com Python` da [Formação Python Developer] da [DIO].

Instrutor: [Guilherme Carvalho]

<h2>Conteúdo</h2>

- [Aprendendo Estruturas de Dados com Python](#aprendendo-estruturas-de-dados-com-python)
  - [Trabalhando com Listas em Python](#trabalhando-com-listas-em-python)
    - [Introdução](#introdução)

## Trabalhando com Listas em Python

### Introdução

Listas são estruturas de dados que permitem armazenar diversos valores em uma única variável, acessíveis por meio de um índice.

```python
# Criando uma lista
lista = [1, 3, 5, 7]

# Imprimindo a lista
print(lista) // [1, 3, 5, 7]
````

Para acessar um elemento específico da lista, basta informar o índice do elemento desejado entre colchetes.

```python
lista = [1, 3, 5, 7]

# Imprimindo o primeiro elemento da lista
print(lista[0]) // 1

# Imprimindo o último elemento da lista
print(lista[-1]) // 7
```

Exemplo de uma matriz 3x3:

```python
matriz = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
]

# Imprimindo o elemento da segunda linha e terceira coluna
print(matriz[1][2]) // 6
```




[DIO]: https://dio.me
[Formação Python Developer]: https://web.digitalinnovation.one/track/formacao-python-developer
[Guilherme Carvalho]: https://github.com/guicarvalho
[PEP 8]: https://www.python.org/dev/peps/pep-0008/#naming-conventions
[PEP 8 - Indentation]: https://www.python.org/dev/peps/pep-0008/#indentation