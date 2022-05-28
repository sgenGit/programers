def solution(lottos, win_nums):
    count = 0
    for x in win_nums:
        if x in lottos:
            count+=1
    zero = lottos.count(0)
    score = {6:1 , 5:2 , 4:3 , 3:4 , 2:5, 1:6, 0:6}
    return [score[count+zero],score[count]]

if __name__ == '__main__':
    lottos = [44, 1, 0, 0, 31, 25]
    win_nums = [31, 10, 45, 1, 6, 19]
    print(solution(lottos, win_nums))