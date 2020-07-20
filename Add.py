def add(a, b):
    # 1.先获取两个中最大的长度，然后将短进行补充，使长度一致
    a=str(a)
    b=str(b)
    max_len = len(a) if len(a) > len(b) else len(b)

    a = a.zfill(max_len)
    b = b.zfill(max_len)
    a = list(a)
    b = list(b)
    c = ''
    result = [0 for i in range(max_len + 1)]  # 这里加1主要是考虑到两数加起来可能比之前的数还多一位

    for i in range(max_len - 1, -1, -1):
        temp = int(a[i]) + int(b[i])
        if temp >= 10:
            # 这里result是i+1  是因为result的长度比max_len长度长
            result[i + 1] += temp % 10
            result[i] += temp // 10
        else:
            result[i + 1] += temp

    for i in range(0, len(result)):
        c += str(result[i])
    return int(c)


if __name__ == '__main__':
    print('请输入两个参数')
    str1 = input()
    str2 = input()
    if str1.isdigit() and str2.isdigit():
        res = add(str1, str2)
        print("add", res)