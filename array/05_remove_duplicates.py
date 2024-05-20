"""
05. 중복 제거
오름차순으로 정렬된 수열이 주어지면 중복된 값을 제거하고 유일값으로 구성된 내림차순 수 열을 만들고 싶습니다.
매개변수 nums에 길이가 n인 수열이 주어지면 중복된 값을 제거하고 유일값만으로 구성된 내 림차순 수열을 배열에 담아 반환하는 프로그램을 작성하세요.

제한사항:
• nums의 길이 3 <= n <= 200,000
• 배열 nums의 원소는 정수입니다. -10,000 <= nums[i] <= 10,000
"""

from collections import deque


def solution(nums):
    answer = deque()
    answer.appendleft(nums[0])

    for i in range(1, len(nums)):
        if nums[i-1] != nums[i] :
            answer.appendleft(nums[i])

    # answer = deque(nums)
    #
    # for x in answer :
    #     if x != answer[-1] :
    #         answer.append(answer.popleft())
    #     else :
    #         answer.popleft()

    return list(answer)


print(solution([0, 1, 1, 1, 2, 2, 2, 3]))
print(solution([1, 1, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 5]))
print(solution([0, 0, 0, 3, 3, 3, 5, 7, 7, 7]))
print(solution([1, 2, 3, 4, 5, 6, 7, 7, 7, 8, 9]))