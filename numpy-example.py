# ------------------------------------------------------------
    #         Numpy?
    # -> 다차원 배열을 효과적으로 처리할 수 있는 라이브러리.
    # -> Python의 기본 리스트에 비해 빠르고 강력함.
# ------------------------------------------------------------
# import library
import numpy as np
# ------------------------------------------------------------
# # 별칭

# list_data = [1, 2, 3]
# np_list_data = np.array(list_data)

# # print(list_data)
# print(np_list_data)
# print(np_list_data.size)    #데이터 갯수
# print(np_list_data.dtype)   #데이터 타입

#-----------------------------------------------------
# # << 다양한 배열 만들어 보기

# # 0, 1, 2, 3
# array1 = np.arange(4)
# print(array1)

# # 4x4크기의 0으로 초기화된 Matrix
# array2 = np.zeros((4, 4), dtype=float, order='C')
# print(array2)

# # 4x4크기의 1로 초기화된 Matrix
# array3 = np.ones((4, 4), dtype=int)
# print(array3)

# # 0부터 9까지 랜덤하게 초기화된 3x3 Matrix 만들기.
# array4 = np.random.randint(0, 10, (3, 3))
# print(array4)

# # 평균이 0이고, 표준편차가 1인 표준 정규를 띄는 배열.
# array5 = np.random.normal(0.0, 1.0, (3, 3))
# print(array5)
#-----------------------------------------------------
# # << 배열 모양 바꿔보기.

# # 배열 가로축 기준으로 합치기, concatenate 함수 사용.
# array1 = np.array([1, 2, 3])
# array2 = np.array([4, 5, 6])
# array3 = np.concatenate([array1, array2])

# print(array3)
# print(array3.shape)

# # 1차원 배열 -> 2차원 배열 변환, reshape함수 사용.
# array4 = np.array([1, 2, 3, 4])
# array5 = array4.reshape((2, 2))
# print(array5)

# # 배열 세로축 기준으로 합치기, concatenate 함수와 axis 속성 사용.
# array6 = np.arange(4).reshape(1, 4)
# array7 = np.arange(8).reshape(2, 4)
# array8 = np.concatenate([array6, array7], axis=0)
# print(array8)

# # 배열을 열 방향 기준으로 나누기, split 함수 사용.
# array9 = np.arange(8).reshape(2, 4) + 3
# l_arr, r_arr = np.split(array9, [2], axis=1)
# print(array9)

#     # shape 확인
# print(l_arr.shape)
# print(r_arr.shape)

#     # split 결과 출력.
# print(l_arr)
# print(r_arr)
#-----------------------------------------------------
# array = np.random.randint(1, 10, size = 4).reshape(2, 2)
# print(array)
# print(array * 2) # numpy의 상수 연산. 각 원소의 상수 연산한 결과와 같다.

# # 서로 다른 형태의 배열 연산
# # 2x2배열과 1x2배열의 합 연산을 한다고 했을 경우, 이론적으로는 불가능 하지만 numpy에서는
# # 1x2배열을 가지고 배열을 확장시켜서 연산을 수행한다.
# # ex)
# #     [8  9]
# #     [5  6]      +       [1  2]

# # =   [8  9]              [1  2]
# #     [5  6]      +       [1  2]

# # =   [9  11]
# #     [6  8]

# arr1 = np.random.randint(1, 10, size = 4).reshape(2, 2)
# arr2 = np.random.randint(1, 10, size = 2).reshape(1, 2)

# print('Example1. ')
# print(arr1)
# print(arr2)
# print('-------------------')
# print(arr1 + arr2)


# print('Example2. ')
# arr3 = np.arange(16).reshape(4, 4) + 1
# arr4 = np.arange(4).reshape(4, 1) + 1
# print(arr3)
# print(arr4)
# print('-------------------')
# print(arr3 + arr4)
# # 이처럼, 형태가 다른 배열을 연산할 수 있도록 배열의 형태를 동적으로 변환 하는것을 '브로드 캐스트(Broad cast)'이라고 한다.

# print('Example3. ')
# arr5 = np.arange(0, 8).reshape(2, 4)
# arr6 = np.arange(0, 8).reshape(2, 4)
# arr7 = np.concatenate([arr5, arr6], axis=0)
# arr8 = np.arange(0, 4).reshape(4, 1)

# print(arr5)
# print(arr6)
# print('--------------------------')
# print(arr7)
# print(arr8)
# print('--------------------------')
# print(arr7 + arr8)
#-----------------------------------------------------------------------------------------
# # << 마스킹 연산 >> 
# # : 각 배열의 원소가 조건에 부합하는지 체크하는 연산.

# ar1 = np.arange(0, 8).reshape(2, 4)
# ar2 = np.arange(0, 8).reshape(2, 4)
# ar3 = np.concatenate([ar1, ar2], axis=0)

# masking_matrix_ar3 = ar3 < 5
# print(masking_matrix_ar3)

# # ar3에 마스킹 연산을 한 matrix를 넣어주면 True값에 해당하는 원소에 대해서만 어떠한 연산을 하겠다는 뜻이다.
# # 앞으로, 반복문을 사용해 원소를 방문할 일 없이 마스킹 연산을 가지고 더욱 빠른 원소 접근이 가능하다.
# ar3[masking_matrix_ar3] = 10
# print(ar3)

# # << 최댓값, 최솟값, 합계, 평균값 >>
# arr = np.arange(0, 16).reshape(4, 4)
# print('최댓값 : ', np.max(arr))
# print('최솟값 : ', np.min(arr))
# print('합계 : ', np.sum(arr))
# print('평균값 : ', np.mean(arr))

# # << 특정 열에 대해서 집계함수를 사용하기 >>
# print('가로축 기준 합 : ', np.sum(arr, axis = 0))
# print('세로축 기준 합 : ', np.sum(arr, axis = 1))