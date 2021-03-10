class Solution:
    def interpret1(self, command: str) -> str:
        return command.replace('()','o').replace('(al)','al')
        # return re.sub('\(\)', 'o', re.sub('\(al\)', 'al', command))

    
    def interpret(self, command: str) -> str:
        res = {'G':'G','(al)':'al','()':'o'}
        tmp, ans = "", ""
        for i, el in enumerate(command):
            tmp += command[i]
            if tmp in res:
                ans += res[tmp]
                tmp = ""
            
        return ans
