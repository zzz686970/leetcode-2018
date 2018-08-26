"""
## reference to build a tree
class Solution:
    def getImportance(self, employees, id):
        """
        :type employees: Employee
        :type id: int
        :rtype: int
        """
        tree=self.build_tree(employees, id)
        return self.dfs(tree,id,False)

    def build_tree(self, data, id):
        root=None
        if data is None or len(data)==0:
            return None
        stack=[]        
        j=0
        while j<len(data):
            if data[j].id==id:
            # if data[j][0]==id:
                root=TreeNode(data[j].id,data[j].importance,None,None, data[j].subordinates)
                # root=TreeNode(data[j][0],data[j][1],None,None, data[j][2])
                del data[j]
                break
            j+=1

        stack.append(root)
        while len(stack)>0:
            cur=stack.pop()
            i=0

            if  cur.rawIds is None or len(cur.rawIds)==0:
                continue

            k=0
            while k<len(cur.rawIds):
                i=0
                while i<len(data):
                    # if len(cur.rawIds)>=1 and  data[i][0]==cur.rawIds[k]:
                    if len(cur.rawIds)>=1 and  data[i].id==cur.rawIds[k]:
                        node=TreeNode(data[i].id,data[i].importance,None,None,data[i].subordinates)
                        # node=TreeNode(data[i][0],data[i][1],None,None,data[i][2])
                        cur.under.append(node)
                        stack.append(node)
                        del data[i]
                    else:
                        i+=1
                k+=1
            
        return root
                
                    
    def dfs(self,node, startId, startCount):
        if node is None:
            return 0
        if node.id==startId:
            sm=node.val
            for i in node.under:
                sm+= self.dfs(i,startId, True)
            return sm
        elif startCount==False:
            for i in node.under:
                self.dfs(i,startId, False)
            return
        else:
            sm=node.val
            for i in node.under:
                sm+=self.dfs(i,startId, True)
            return sm

class TreeNode:
    def __init__(self, id, val, left, right, childrenIds):
        self.val=val
        self.id=id
        self.under=[]
        self.rawIds=childrenIds
"""

"""
# Employee info
class Employee:
	def __init__(self, id, importance, subordinates):
		# It's the unique id of each node.
		# unique id of this employee
		self.id = id
		# the importance value of this employee
		self.importance = importance
		# the id of direct subordinates
		self.subordinates = subordinates
"""
class Solution:
	def getImportance(self, employees, id):
		"""
		:type employees: Employee
		:type id: int
		:rtype: int
		""" 
		result = {employee.id : employee for employee in employees}
		
		def dfs(employee):
			return employee.importance + sum(dfs(result[sub]) for sub in employee.subordinates)

		return dfs(result[id])
	   