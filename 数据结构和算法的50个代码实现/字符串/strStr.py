def strStr(str, need):
    if not need:
        return 0
    if not str:
        return -1
    for i in range(len(str)):
        cnt = 0
        while cnt < len(need):
            if str[i + cnt] == need[cnt]:
                cnt += 1
            else:
                break
        if cnt == len(need):
            return i
    return -1


if __name__ == '__main__':
    print(strStr('sundat', 'unda'))
