def solution(maps):
    answer = []
    maps.insert(0, "XXXXXXX") #.insert 맞는 지 의문듬
    temp = 0
    for i in maps:
        if temp == 0:
            temp += 1
            continue
        else:
            i.replace(i, "X" + i + "X") # 이 부분도
    
    maps.append("XXXXXXX")
    temp = 0
    current = 0
    firstNumber = True
    x = 1
    y = 1
    first_x = x
    first_y = y
    
    dic = {} #딕셔너리 선언 이거 맞는 지 의문
    
    
    mapH = len(maps) -2
    mapW = len(maps[0]) - 2 
    print(mapH, mapW)
    for i in range(1, mapH):
        for j in range(1, mapW):
            dic_name = (str(j) + "_" + str(i))
            dic[dic_name] = 0 #이런 식으로 할 수 있는 지
    while(True):
        if maps[y][x] != "X":
            if firstNumber == True:
                if dic[str(x) + "_" + str(y)] == 0:
                    answer.append(int(maps[y][x]))
                    dic[str(x) + "_" + str(y)] = 1
                    first_x = x 
                    first_y = y
                    firstNumber = False
                else:
                    x += 1
                    if x == mapW:
                        x = 1
                        y += 1
                    if y == mapH:
                        print("1번")
                        break
                    continue
            print("answer:" , answer[current], current)
            print(x, y, "숫자:", maps[y][x])
            if (maps[y][x-1] != "X") and (dic[str(x-1) + "_" + str(y)] == 0):
                        x -= 1
                        answer[current] += int(maps[y][x])
                        dic[str(x) + "_" + str(y)] = 1
            elif (maps[y][x+1] != "X") and (dic[str(x+1) + "_" + str(y)] == 0):
                        x += 1
                        answer[current] += int(maps[y][x])
                        dic[str(y) + "_" + str(x)] = 1
            elif (maps[y+1][x] != "X") and (dic[str(x) + "_" + str(y+1)] == 0):
                        y += 1
                        answer[current] += int(maps[y][x])
                        dic[str(x) + "_" + str(y)] = 1
            elif (maps[y-1][x] != "X") and (dic[str(x) + "_" + str(y-1)] == 0):
                        y -= 1
                        answer[current] += int(maps[y][x])
                        dic[str(x) + "_" + str(y)] = 1
            else:
                current += 1
                firstNumber = True
                x = first_x
                y = first_y
        else:
            if firstNumber == False:
                pass
            else:
                x += 1
                if x == mapW:
                    x = 1
                    y += 1
                if y == mapH:
                    print("2번")
                    break
                
                
            
    return answer

a = ["X591X","X1X5X","X231X", "1XXX1"]
result = solution(a)
print(result)