class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        items, tables = [], []
        for a,b,c in orders:
            if int(b) not in tables:
                bisect.insort_left(tables, int(b))
            if c not in items:
                bisect.insort_right(items, c)
        
        item_dic = {item: index+1 for index, item in enumerate(items)}
        table_dic = {str(table): index+1 for index, table in enumerate(tables)}
        ans = [['Table'] + [el for el in items]]
        for i in range(len(tables)):
            temp = [str(tables[i])]
            temp.extend(['0' for _ in range(len(items))])
            ans.append(temp)
        for name, table, food in orders:
            ans[table_dic[table]][item_dic[food]] = str(int(ans[table_dic[table]][item_dic[food]]) + 1)
        print(items, tables)
        return ans

           
