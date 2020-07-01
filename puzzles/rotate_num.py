"""排队报数
	
[description]
""" 
class people:
    def __init__(self):
        self.name = ' '
        self.next = None 

head = people()
heam.name = '1'
ptr = head 

for i in range(2, 31):
    new_people = people()
    new_people.name = i 
    ptr.next = new_people
    ptr = ptr.next 

## circle linked list
ptr.next = head 
debug = 0 
if debug:
    ptr = head 
    while True:
        print(ptr, ptr.name)
        ptr = ptr.next 
        if ptr == head:
            break 
        else:
            pass 
else:
    pass 

remain_people = 30
ptr = head
while remain_people != 15:
    for ii in range(1,8):
        ptr = ptr.next
    else:
        # 打印9号链表
        print(ptr,'{}号下船了'.format(ptr.next.name))
        # 删除9号链表
        ptr.next = ptr.next.next
        remain_people -= 1
        # 指针向前运动一次
        ptr = ptr.next


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
