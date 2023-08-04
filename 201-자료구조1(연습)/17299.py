def find_next_greater_frequency(arr):
    freq_dict = {}
    for num in arr:
        freq_dict[num] = freq_dict.get(num, 0) + 1

    ngf_list = [-1] * len(arr)
    stack = []

    for i in range(len(arr)):
        while stack and freq_dict[arr[stack[-1]]] < freq_dict[arr[i]]:
            idx = stack.pop()
            ngf_list[idx] = arr[i]
        stack.append(i)

    return ngf_list


# 입력 받기
N = int(input())
A = list(map(int, input().split()))

# 결과 출력
result = find_next_greater_frequency(A)
print(*result)
