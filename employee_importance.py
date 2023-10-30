"""
# Definition for Employee.
class Employee(object):
    def __init__(self, id, importance, subordinates):
    	#################
        :type id: int
        :type importance: int
        :type subordinates: List[int]
        #################
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution(object):
    def getImportance(self, employees, id):
        employee_id = {emp.id : emp for emp in employees}
        ret = 0

        def rect(id):
            
            ret = employee_id[id].importance
            if employee_id[id].subordinates:
                for sub_id in employee_id[id].subordinates:
                    ret += rect(sub_id)
            return ret
        
        return rect(id)