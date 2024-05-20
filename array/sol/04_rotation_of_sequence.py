"""
03. 수열의 회전
정수 수열의 원소를 회전하고 싶습니다.
매개변수 nums에 길이가 n인 수열이 주어지고, 매개변수 k에 뒤로 이동시키고 싶은 원소의 개수가 주어지면 nums의 원소 중 앞 원소 k개를 수열의 뒤쪽으로 이동하고 난 후의 수열을 반환하는 프로그램을 작성하세요.

제한사항:
• nums의 길이 3 <= n <= 200,000
• 배열 nums의 원소는 정수입니다. -10,000 <= nums[i] <= 10,000 • 0 <= k <= nums의 길이
"""

from collections import deque 

def solution(nums, k):
    answer = []

    # 배열을 원소로 삽입
    # nums.append(nums[:k])

    # 시간 효율성 떨어짐
    # for i in range(k) :
    #     nums.append(nums[i])
    # nums[:k] = []
    # answer = nums

    # nums를 deque 자류구조로 변경 (이중 연결 리스트 이용)
    # 대신 반환할때 deque말고 list로 반환
    
    answer = deque(nums)
    for i in range(k) :
        # 앞에서 원소 하나 꺼내고 뒤에 삽입
        answer.append(answer.popleft())

    return list(answer)


print(solution([3, 7, 1, 5, 9, 2, 8], 3))
print(solution([2, 12, 2, 1, 3, 3, 9], 2))
print(solution([1, 2, 5, 4, 6, 7, 9], 6))
print(solution([1, 3, 6, 8, 14, 2, 1, 7], 5))