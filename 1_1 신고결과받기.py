from traceback import print_tb


def solution(id_list, report, k):

    answer = [0 for x in range(len(id_list))]
    answer2 = [[] for x in range(len(id_list))]

    for x in range(len(report)):

        who = (report[x].split())[0]
        to = (report[x].split())[1]

        #to의 인덱스번호 찾기
        to_index = id_list.index(to)

        #이미 동일인을 신고한 이력이있는지
        if who not in answer2[to_index]:
            answer2[to_index].append(who)



    for t in answer2:
        if(len(t) >= k):
            for y in range(len(t)):
                #t[y]  이 이름의 인덱스번호 찾기
                who_index = id_list.index(t[y])
                answer[who_index] += 1


    return answer


if __name__ == '__main__':
    id_list = ["muzi", "frodo", "apeach", "neo"]
    report = ["muzi frodo", "apeach frodo",
              "frodo neo", "muzi neo", "apeach muzi"]
    k = 2
    answer = solution(id_list, report, k)
    print(answer)
