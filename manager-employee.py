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
        """This function """
        for entry in test_input:
            if entry['manager']not in self.relations:
                self.relations[entry['manager']] = Node(entry['manager'], entry['name'])
            else:
                self.relations[entry['manager']].employees.append(entry['name'])

    def findHierarchy(self):
        def __recursiveHelper(key_name, output, indent):
            if key_name in self.relations:
                # if key_name != None:
                #     output += str(key_name) + "\n"
                for employee in self.relations[key_name].employees:
                    output += "   "*indent+ str(employee) +"\n"
                    print(output)
                    __recursiveHelper(employee, output, indent+1)
            else:
                return output

                #two issues:
                #having trouble returning the concatenated output
                    #from the recursive function
                #the top of the hierarchy are people with 'None'
                    #as a manager and 'None' is being overwritten
                        #as there are two people at the top.


        output = ""
        indent = -1
        for relation in self.relations:
            if relation == None:
                __recursiveHelper(self.relations[relation].name, output, indent+1)

        return output


class Node():
    def __init__(self,name, employee):
        self.name = name
        self.employees = []
        self.employees.append(employee)


relationship = Relationships()
relationship.buildHierarchy(test_input)
# print(relationship.relations)
print(relationship.relations[None].employees)
print(relationship.findHierarchy())


"""
Printed output:


['Trey', 'Alex']
Trey

Trey
   Paul

Trey
   Paul
      Joe

Trey
   Paul
      Joe
      Larry

Trey
   Paul
      Joe
      Larry
         Moe

Trey
   Paul
   Peter

Trey
   Paul
   Peter
   Mary

Trey
Alex

Trey
Alex
   Jesse

Trey
Alex
   Jesse
   Henry


[Finished in 0.435s]

"""
