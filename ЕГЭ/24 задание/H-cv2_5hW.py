with open('H-cv2_5hW.txt') as f:
    num = f.readline().replace('AXMM', 'AXM_XMM').split('_')
    maxi = 0
    for i in range(len(num)):
        if len(num[i]) > maxi:
            maxi = len(num[i])
    print(maxi)
