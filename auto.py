# -*- coding: utf-8 -*-
# @Author: zzz686970
# @Date:   2020-06-06 17:13:21
# @Last Modified by:   zzz686970
# @Last Modified time: 2020-06-18 13:11:03
# if __name__ == '__main__':
#   num, file_name = sys.argv[0] sys.argv[1]
#   with open(f"{file_name}.py", 'w') as f:
#       f.write(f"""def {file_name}():
            
#           """)


# import pkg_resources
# installed_packages = pkg_resources.working_set
# installed_packages_list = sorted(["%s==%s" % (i.key, i.version)
#      for i in installed_packages])
# print(installed_packages_list)
import csv

def process_all_lc():
    with open('raw_all.txt', 'r') as f:
        data = f.readlines()

    ans = [[] for _ in range(len(data))]
    i = 1
    for el in data:
        if str(i) == el.strip().replace('\t','').replace('\n',''):
            ans[i].append(str(i))
            i += 1
        else:
            ans[i-1].extend(el.strip().replace('\n','').split('\t'))

    ans = [[sub.strip() for sub in el if sub] for el in ans if el]
    print(ans)

    with open('full_lc.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerows(ans)

if __name__ == '__main__':
    with open('raw_unlocked.txt', 'r') as f:
        data = f.readlines()
    ans = [[]]
    unlocked_num =set()
    for el in data:
        if el.strip().isdigit():
            ans.insert(len(ans), [el.strip()])
            unlocked_num.add(int(el.strip()))
        else:
            if not el.strip().split('\t')[0].isdigit():
                ans[-1].extend(el.strip().split('\t'))

    ans = [[sub.strip() for sub in el] for el in ans if el]
    with open('unlocked_lc.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerows(ans)

    locked_num = list(sorted([i for i in range(1, max(unlocked_num) + 1) if i not in unlocked_num]))
    print(locked_num, '\n', len(locked_num))
