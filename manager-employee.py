test_input = [
    {'name': 'Trey', 'manager': None},
    {'name': 'Paul', 'manager': 'Trey'},
    {'name': 'Peter', 'manager': 'Trey'},
    {'name': 'Mary', 'manager': 'Trey'},
    {'name': 'Joe', 'manager': 'Paul'},
    {'name': 'Larry', 'manager': 'Paul'},
    {'name': 'Alex', 'manager': None},
    {'name': 'Jesse', 'manager': 'Alex'},
    {'name': 'Henry', 'manager': 'Alex'},
    {'name': 'Moe', 'manager': 'Larry'},
]
"""
Trey
    Paul
        Joe
        Larry
            Moe
    Peter
    Mary
Alex
    Jesse
    Henry
"""
# Given this test input, print out the manager to employee relationships like so.

class Relationships():
    def __init__(self):
        self.relations = {}

    def buildHierarchy(self, test_input):
        """This function builds a dictionary of managers to manager nodes.
        The keys are strings of the names of managers and the values are nodes:
        2 fields, the name of the manager and an array that that manager employs."""
        for entry in test_input:
            if entry['manager']not in self.relations:
                self.relations[entry['manager']] = Node(entry['manager'], entry['name'])
            else:
                self.relations[entry['manager']].employees.append(entry['name'])

    def findHierarchy(self):
        """This function recursively builds a string of manager to employee
        relationships starting from the managers that do not have managers."""
        def __recursiveHelper(key_name, output, indent):
            if key_name in self.relations:
                for employee in self.relations[key_name].employees:
                    output += "   " * indent + str(employee) +"\n"
                    return __recursiveHelper(employee, output, indent+1)
            else:
                return output


            #experimenting with Iter() and next() iterators/generators
            #and a while loop in the recursive function:

            # employees = iter(self.relations)
            # employee = next(employees, "stop")
            # while employees and employee != 'stop':
            #     print(employee)
            #     employee = next(employees, "stop")



        #only issue:
        #having trouble returning the concatenated output
            #from the recursive function

        output = ""
        indent = -1
        #   self.relations is a dictionary of manager-name string keys.
        #   The employees of None are the top-ranking managers.
        return __recursiveHelper(None, output, indent+1)


class Node():
    def __init__(self,name, employee):
        self.name = name
        self.employees = []
        self.employees.append(employee)


relationship = Relationships()
relationship.buildHierarchy(test_input)
print(relationship.findHierarchy())


"""
Printed output:

Trey
   Paul
      Joe

*Trey
   Paul
      Joe
      Larry
         Moe

Trey
   Paul
   Peter

Trey
   Paul
   *Peter
   *Mary

Trey
Alex
   Jesse

Trey
*Alex
   Jesse
   Henry

this should be the output:

*Trey
   Paul
      Joe
      Larry
         Moe
    *Peter
    *Mary
*Alex
   Jesse
   Henry



"""
