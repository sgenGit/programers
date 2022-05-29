def solution(new_id):
    new_id = new_id.lower()
    dele = list('~!@#$%^&*()=+[{]}:?,<>/')
    formatt = new_id.maketrans({
        x:'' for x in dele
    })
    print(new_id)
    new_id = new_id.translate(formatt)
    print(new_id)

    while '..' in new_id:
        new_id = new_id.replace('..', '.')
        print(new_id)

    new_id = new_id.strip('.')
    print(new_id)

    if(len(new_id)==0):
        new_id += 'a'

    if(len(new_id)>=16):
        new_id = new_id[0:15]
        new_id = new_id.strip('.')

    while(len(new_id)<=2):
        new_id += new_id[len(new_id)-1]

    answer = new_id
    return answer


if __name__ == '__main__':
    new_id = "...!@BaT#*..y.abcdefghijklm"
    solution(new_id)