import os
import struct

"""
analyze a bmp file
文件头的结构按顺序如下：

两个字节：'BM'表示Windows位图，'BA'表示OS/2位图；
一个4字节整数：表示位图大小；
一个4字节整数：保留位，始终为0；
一个4字节整数：实际图像的偏移量；
一个4字节整数：Header的字节数；
一个4字节整数：图像宽度；
一个4字节整数：图像高度；
一个2字节整数：始终为1；
一个2字节整数：颜色数。

struct
>表示字节顺序是big-endian，也就是网络序，I表示4字节无符号整数, H：2字节无符号整数

"""

# s = b'BM\x18\xf1\x10\x00\x00\x00\x00\x006\x00\x00\x00(\x00\x00\x00\xd0\x02\x00\x00\x02\x02\x00\x00\x01\x00\x18\x00'

# s = b'\x42\x4d\x38\x8c\x0a\x00\x00\x00\x00\x00\x36\x00\x00\x00\x28\x00\x00\x00\x80\x02\x00\x00\x68\x01\x00\x00\x01\x00\x18\x00'
# print(struct.unpack('<ccIIIIIIHH', s))

"""bytes iterate
L = [bytes_obj[i:i+1] for i in range(len(bytes_obj))]
list(b'123'.iterbytes())

"""
def bmpinfo():
	path = "bmp-sample.bmp"
	if os.path.splitext(path)[1] =='.bmp':
		with open(path, 'rb') as f:
			s = f.read(30)
		if bytes([s[0]]) == b'B' and bytes([s[1]]) == b'M':
			# print("Yeah!")
			bmp_info =  struct.unpack('<ccIIIIIIHH', s)
			# print(bmp_info)
			print("BMP size:{}*{}".format(bmp_info[6], bmp_info[7]))
			print("Colors:{}".format(bmp_info[9]))

	else:
		print("Wrong path")

if __name__ == '__main__':
	bmpinfo()