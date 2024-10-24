import numpy as np
import matplotlib.pyplot as plt
import requests
from threading import Thread
from pprint import pprint


# matplotlib, numpy
class System_of_linear_algebraic_equations:

    def __init__(self, matrix_A, matrix_B):
        self.__matrix_A = np.array(matrix_A)
        self.__matrix_B = np.array(matrix_B)

    def get_matrix(self):
        print(f'Матрица A:\n {self.__matrix_A}')
        print(f'Матрица B: {self.__matrix_B}')


    '''Метод нахождения определителя'''
    def determinant(self, matrix=np.eye(3)):
        print(f'det = {matrix[0][0]} * {matrix[1][1]} * {matrix[2][2]} + '
              f'{matrix[1][0]} * {matrix[2][1]} * {matrix[0][2]} + '
              f'{matrix[0][1]} * {matrix[1][2]} * {matrix[2][0]} -'
              f'{matrix[2][0]} * {matrix[1][1]} * {matrix[0][2]} - '
              f'{matrix[1][0]} * {matrix[0][1]} * {matrix[2][2]} - '
              f'{matrix[2][1]} * {matrix[1][2]} * {matrix[0][0]} = '
              f'{round(np.linalg.det(matrix))}\n')


    '''Метод находит корни СЛАУ'''
    def solution(self):
        X = np.linalg.solve(self.__matrix_A, self.__matrix_B)
        print(f'Решение СЛАУ: {X}')


    '''Развернутое решение СЛАУ'''
    def complete_solution(self):
        print("Решение СЛАУ методом Крамера")
        print(f'{self.__matrix_A[0]}\n{self.__matrix_A[1]} = {self.__matrix_B}\n{self.__matrix_A[2]}\n')
        print("Находим определитель системы")
        self.determinant(self.__matrix_A)
        print("Остальные определители получим, заменяя столбец с коэффициентами соответствующей"
              " переменной (неизвестного) свободными членами:")
        list_det_fre = []
        for i in range(3):
            A_free = self.__matrix_A.copy()
            A_free[:, i] = self.__matrix_B
            print(f'{A_free[0]}\n{A_free[1]} = A{i + 1}\n{A_free[2]}')
            self.determinant(A_free)
            list_det_fre.append(round(np.linalg.det(A_free)))
        print('Корни СЛАУ:')
        for i in range(3):
            print(f'X{i+1} = {list_det_fre[i]}/{round(np.linalg.det(self.__matrix_A))} = '
                  f'{round(list_det_fre[i]/round(np.linalg.det(self.__matrix_A)), 5)}')


    '''Метод отображает матрицу'''
    def matrix_plot(self):
        plt.matshow(self.__matrix_A)
        # plt.colorbar()
        plt.show()


'''Пример'''
matrix = System_of_linear_algebraic_equations([[124, -2345, -453], [23, 2, -4], [2, 235, 0]], [1, 0, -1])
matrix.matrix_plot()
matrix.complete_solution()



# requests
THE_URL = 'https://binaryjazz.us/wp-json/genrenator/v1/genre/'
res= []

def resp(url):
    for i in range(5):
        response = requests.get(THE_URL)
        page_response = response.json()
        res.append(page_response)


thr_f = Thread(target=resp, args=(THE_URL, ))
thr_s = Thread(target=resp, args=(THE_URL, ))

thr_f.start()
thr_s.start()

thr_f.join()
thr_s.join()

# pprint(res)







