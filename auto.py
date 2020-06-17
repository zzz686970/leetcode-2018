# -*- coding: utf-8 -*-
# @Author: zzz686970
# @Date:   2020-06-06 17:13:21
# @Last Modified by:   zzz686970
# @Last Modified time: 2020-06-15 18:49:06
# if __name__ == '__main__':
# 	num, file_name = sys.argv[0] sys.argv[1]
# 	with open(f"{file_name}.py", 'w') as f:
# 		f.write(f"""def {file_name}():
			
# 			""")


import pkg_resources
installed_packages = pkg_resources.working_set
installed_packages_list = sorted(["%s==%s" % (i.key, i.version)
     for i in installed_packages])
print(installed_packages_list)