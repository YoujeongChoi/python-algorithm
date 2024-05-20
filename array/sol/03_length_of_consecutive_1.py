"""
03. 연속된 1의 길이
매개변수 nums에 0과 1로된 수열이 주어지면 1이 연속된 부분수열 중 가장 긴 부분수열의 길 이를 반환하는 프로그램을 작성하세요.

제한사항:
• nums의 길이 3 <= n <= 100,000
"""

def solution(nums):
    current_length = 0
    answer = 0

    for x in nums :
        if x == 1 :
            current_length += 1
        else :
            # if current_length > answer :
            #     answer = current_length
            answer = max(current_length, answer)
            current_length = 0

    """중요"""
    # 배열 끝에서 연속된 '1'의 길이를 확인
    if current_length > answer:
        answer = current_length


    # count = 0
    # temp = []
    # n = len(nums)
    #
    # for i in range(n):
    #     while nums[i] == 1:
    #         count += 1
    #     temp.append(count)
    #
    # for x in temp:
    # for x in temp:
    #     if x > answer :
    #         answer = x

    return answer


print(solution([1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1]))
print(solution([0, 0, 1, 0, 1, 0, 0]))
print(solution([1, 1, 1, 1, 1]))
print(solution([1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1]))