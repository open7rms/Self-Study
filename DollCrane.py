def solution(board, moves):
    box = []
    delete = 0
    for se in moves :# selection 하는 sequence
        for po in range(len(board)): # pickup 하는 위치 탐색
            if board[po][se-1] != 0 :
                box.append(board[po][se-1])
                board[po][se-1] = 0 
                break
            if len(box) >= 2 and box[-1] == box[-2]:
                box=box[:-2]
                delete += 2
    return delete

board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]
print(solution(board,moves))
