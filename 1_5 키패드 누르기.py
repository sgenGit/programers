from tkinter import E


def solution(numbers, hand):
    L_locate = '*'
    R_locate = '#'
    LL = ['1', '4', '7']
    RR = ['3', '6', '9']
    distance_dic = {'1': 11, '2': 12, '3': 13, '4': 21, '5': 22,
        '6': 23, '7': 31, '8': 32, '9': 33, '*': 41, '0': 42, '#': 43}
    result = ''
    for x in numbers:
        x = str(x)
        if (x in LL):
            result += 'L'
            L_locate = x
        elif (x in RR):
            result += 'R'
            R_locate = x
        elif (dist(distance_dic[L_locate], distance_dic[x]) < dist(distance_dic[R_locate], distance_dic[x])):
           #왼손위치와 누를위치의 거리 vs 오른손위치와 누를위치의 거리
            result += 'L'
            L_locate = x
        elif (dist(distance_dic[L_locate], distance_dic[x]) > dist(distance_dic[R_locate], distance_dic[x])):
            result += 'R'
            R_locate = x
        elif (hand=='left'):
            
            result += 'L'
            L_locate = x
        else:
            result += 'R'
            R_locate = x
        
    return result


def dist(L, R):
    L_1 = L//10
    L_2 = L % 10
    R_1 = R//10
    R_2 = R % 10
    return abs(L_1-R_1)+abs(L_2-R_2)


if __name__ == '__main__':
    numbers = [7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2]
    hand = "left"
    answer = solution(numbers, hand)
    print(answer)
