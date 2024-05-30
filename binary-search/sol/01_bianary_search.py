"""
01. 이진 탐색
nums에 오름차순으로 정렬된 정수 배열이 주어지고, target에 nums배열에서 찾고자 하는 값 이 주어지면 nums배열에서 target의 인덱스 번호를 찾아 반환하는 프로그램을 작성하세요. 인덱스 번호는 0번부터 시작합니다.
target값이 nums에 존재하지 않을 경우 -1를 반환합니다

제한사항:
• nums의 길이는 100,000,000을 넘지 않습니다. nums의 원소는 유일값입니다.
• -100,000,000 <= nums[i] <= 100,000,000
"""


def solution(nums, target):
    answer = 0

    left = 0
    right = len(nums) - 1

    while left <= right :
        mid = (left + right) // 2
        if target == nums[mid] :
            return mid
        elif target > nums[mid] :
            left = mid + 1
        else :
            right = mid -1

    return -1


print(solution([2, 5, 7, 8, 10, 15, 20, 24, 25, 30], 8))
print(solution([-3, 0, 2, 5, 8, 9, 12, 15], 0))
print(solution([-5, -2, -1, 3, 8, 9, 12, 17, 23], 2))
print(solution([3, 6, 9, 12, 17, 29, 33], 3))
print(solution([1, 2, 3, 4, 5, 7, 9, 11, 12, 15, 16, 17, 18], 18))


"""
개념
    1. lower bound search (하한 탐색) -> bisect_left
        찾고자 하는 값보다 크거나 같은 값 중에서 가장 작은 값 찾기 (크거나 같은 첫번째 위치)
        
        target = 20
        answer = [10, 20, 20, 30, 40]
        print(bisect_left(answer, target))      # 1 (20이 첫번째로 나오는 인덱스 1)
        
     
    2. upper bound search (상한 탐색) -> bisect_right
        찾고자 하는 값보다 큰 것 중에서 가장 작은 값 찾기 (큰 첫번째 위치)
        
        target = 20
        answer = [10, 20, 20, 30, 40]
        print(bisect_left(answer, target))      # 3 (20보다 큰 수 첫번째로 나오는 인덱스 3)
"""

