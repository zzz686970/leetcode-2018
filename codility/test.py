import collections
def get_sec(time_str):
    h, m, s = time_str.split(':')
    return int(h) * 3600 + int(m) * 60 + int(s)

def solutions(S):
    from collections import defaultdict
    total_list= collections.defaultdict(list)
    for el in S.split('\n'):
        time, number = el.split(',')
        time_sec = get_sec(time)
        total_list[number].append(time_sec)

    cnt = 0
    total_sum = {key:sum(val) for key, val in total_list.items()}
    # need_remove = list(dict.keys())[0]
    total_sum2 = sorted(total_sum.items(), key=lambda x: (x[1],x[0]), reverse=True)
    remove_key, remove_val = total_sum2.pop(0)
    del total_list[remove_key]
    for key, vals in total_list.items():
        for val in vals:
            if val < 300:
                cnt += val * 3
            else:
                if val % 60 == 0:
                    cnt += val // 60 * 150
                if val % 300:
                    cnt += ((val // 60) + 1) * 150

    return cnt 

print(solutions("00:01:07,400-234-090\n00:05:01,701-080-080\n00:05:00,400-234-090"))