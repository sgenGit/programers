from traceback import print_tb


def solution(id_list, report, k):

    answer = [0 for x in range(len(id_list))]
    answer2 = [[] for x in range(len(id_list))]

    for x in range(len(report)):

        who = (report[x].split())[0]
        to = (report[x].split())[1]
        print('---------'+who+'가 '+'--> ['+to+']'+'를 신고!'+'---------')
        print()

        #to의 인덱스번호 찾기
        for x in range(len(id_list)):
            if(id_list[x] == to):
                to_index = x

        #이미 동일인을 신고한 이력이있는지
        iss = 0
        for x in answer2[to_index]:
            if(x == who):
                iss = 1

        if(iss == 0):
            answer2[to_index].append(who)

        print("[ muzi | frodo | apeach | neo ]")
        print(answer2)
        print()

    for t in answer2:
        if(len(t) >= k):
            for y in range(len(t)):
                #t[y]  이 이름의 인덱스번호 찾기
                for x in range(len(id_list)):
                    if(id_list[x] == t[y]):
                        who_index = x
                answer[who_index] += 1
    return answer


if __name__ == '__main__':
    id_list = ["muzi", "frodo", "apeach", "neo"]
    report = ["muzi frodo", "apeach frodo",
              "frodo neo", "muzi neo", "apeach muzi"]
    k = 2
    answer = solution(id_list, report, k)
    print(answer)
