"""排队报数
	
[description]
""" 

def yueSeFu(m,n,k):
    arr = list(range(1, m+1))
    i = 0
    while len(arr) > m - n:
        i += (k - 1)
        if i >= len(arr):
            i -= len(arr)
        print(arr)
        print("{}号下船了".format(arr[i]))
        del arr[i]

if __name__ == '__main__':
    # 传入起始人数m，需要下船的人数n，数到多少下船的序号k
    yueSeFu(10,9,3)
