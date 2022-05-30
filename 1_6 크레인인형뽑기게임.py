import numpy as np
import pandas as pd
def solution(board, moves):    
    values = board
    index = [str(x)+'행' for x in range(1,len(board)+1)]
    columns = [str(x)+'열' for x in range(1,len(board)+1)]    
    df = pd.DataFrame(values, index=index, columns=columns)
    # print(df)

    # print('1열의 값들')
    # print(df['1열'])
    # print(df['1열'].values)
    # print(type(df['1열'].values))
    # print(type(df['1열'].values.tolist()))
    baguni = []
    count = 0
    print('[moves의 상황]')
    print(moves)
    print()
    for x in moves: #x열에 접근(x열에 있는 인형을 뽑음)
        print()
        print('[데이터 프레임 상황]')
        print(df)
        print('[바구니의 상황]')
        print(baguni)
        print('                      ---->'+str(x)+'열에서 뽑음')
        data = df[str(x)+'열'].values.tolist()
        print('                      ---->'+str(x)+'열의 데이터 : ')
        print(data)
        for index,y in enumerate(data):
            if(y!=0): #최초로 제일위에있는 인형에 접근
                print('                      ---->'+'뽑을 인형 : '+str(y))
                # if(ba)
                
                if(len(baguni)!=0 and baguni[-1]==y): #2개가 같아져서 펑
                    baguni.pop()
                    count+=2
                    df.at[str(index+1)+'행', str(x)+'열'] = 0
                        
                else : #같은게 없다
                    baguni.append(y)
                    df.at[str(index+1)+'행', str(x)+'열'] = 0
                    
                break
    return count


if __name__ == '__main__':
    board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]	
    moves = [1,5,3,5,1,2,1,4]
    count = solution(board, moves)
    print(count)