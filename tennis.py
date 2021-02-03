def point(str score):
    point = [0,0]
    for i in range(len(score)):
        if score[i] == score[i+1]:
            point[0] += 1
        else:
            point[1] += 1
