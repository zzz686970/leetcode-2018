# -*- coding: utf-8 -*-
# @Author: zzz686970
# @Date:   2020-06-06 17:13:21
# @Last Modified by:   zzz686970
# @Last Modified time: 2020-06-06 17:20:33
if __name__ == '__main__':
	num, file_name = sys.argv[0] sys.argv[1]
	with open(f"{file_name}.py", 'w') as f:
		f.write(f"""def {file_name}():
			
			""")