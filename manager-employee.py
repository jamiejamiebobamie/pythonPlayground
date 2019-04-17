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
        The keys are strings of the names of managers and the values are nodes
        2 fields, the name of the manager and an array that that manager employes."""
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
                    __recursiveHelper(employee, output, indent+1)
            else:
                print(output)

                #only issue:
                #having trouble returning the concatenated output
                    #from the recursive function


        output = ""
        indent = -1
        for relation in self.relations:
            #self.relations is a dictionary of manager-name string keys.
            #relation == None is the 'root' of the dictionary, the employees of
            #None are the top-ranking managers.
            #
            if relation == None:
                return __recursiveHelper(self.relations[relation].name, output, indent+1)

        return output


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
