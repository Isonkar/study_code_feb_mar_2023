n = int(input()) # ввод размера матрицы
lst = [[0] * n for i in range(n)] # создание нулевой матрицы
i = 0  # i - строка (равен нулю потому, что цикл начинает свой обход с верхней строки)
j = 0  # j - столбец (равен нулю потому, что цикл начинает свой обход с левого столбца)
di = 0  # di - смещениe строки (равен нулю потому, что  обход начинается слева направо в  одной строке)
dj = 1  # dj - смещениe столбца (равен единице потому, что обход начинается  в пределах одной строки слева направо)

for k in range(n**2):  # цикл обходит все ЗНАЧЕНИЯ матрицы-вывода
    lst[i][j] = k + 1  # присваение значения в выбранную ячейку
    if lst[(i + di) % n][(j + dj) % n]:
        """
        Если следующая ячейка равна положительному числу, то выполняется код ниже.
        Деление индекса по остатку на длину матрицы нужно во избежание IndexError,
        когда текущая ячейка явлется последней в своей последовательности(т.е. следующей не существует).
        Тогда этой ячейкой будет являться ранее заполненая(первой ячейкой текущей ряда или столбца).
        """
        di, dj = dj, -di
        """
        происходит изменение вектора движение "курсора" по ЧАСОВОЙ стрелке,
        в этом можно убедиться на примере:
        di = 0 => di = 1 => di = 0  => di = -1 => di = 0    пара вернулась
        dj = 1 => dj = 0 => dj = -1 => dj = 0  => dj = 1    к начальнем значениям
        вправо => вниз   => влево   => вверх   => вправо    это вектор движения
        """
    i = i + di  # строка следующей ячейки
    j = j + dj  # столбец следующей ячейки

for line in lst: # просто вывод готовой матрицы
    print(*line)
    
    
 # next var
	
arr = [list('0' * n) for i in range(n)]  # заполнение списка нулями
k = 0  # переменная для выравнивания, т. е. сужения круга (когда один пройден, увеличение k на 1)
index = 1  # счётчик
while index < n * n:
    for j in range(k,n-k):  # движение вправо (прямо по индексу j)
        arr[k][j] = index
        index += 1
    for i in range(k+1,n-k):  # вниз (прямо по индексу i)
        arr[i][n-k-1] = index
        index += 1
    for j in range(n-k-2,k-1,-1):  # влево (обратно по индексу j)
        arr[n-k-1][j] = index
        index += 1
    for i in range(n-k-2,k,-1):  # вверх (обратно по индексу i)
        arr[i][k] = index
        index += 1
    k += 1  # круг пройден, увеличиваем k
if arr[n // 2][n // 2] == '0':  # при нечётных n список не заполняет 0 в середине индексом, так что делаем проверку
    arr[n // 2][n // 2] = n * n
#[print(*i) for i in arr]  # вывод
for i in arr:
    for j in i:
        print(str(j).ljust(4), end='')
    print()

# next var


