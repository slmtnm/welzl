# Welzl algorithm
Реализация [алгоритма Велцла](https://en.wikipedia.org/wiki/Smallest-circle_problem#Welzl's_algorithm) на Python.

Запуск программы:
```console
$ python3 ./main.py <путь к файлу с координатами точек>
```

Файл, который передается данной программе, содержит набор точек в виде
набора строк, каждая из которых состоит из двух чисел -- абсциссы и ординаты
точки.

Например:
```
0 0
2 0
1 1
```

Программа печатает несколько индексов точек исходного набора, по которым
определяется результирующая минимальная окружность, содержащая весь набор точек.

# Визуализация

Для визуализации результата необходимо установить Plotly
```console
$ python3 -m pip install plotly
```

И запустить скрипт visualize.py:
```console
$ python3 ./visualize.py
```

Он генерирует несколько случайных точек на плоскости и рисует
результирующий минимальный диск.