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

    def buildHierarchy(self,test_input):
        for entry in test_input:
            if entry['name'] not in self.relations:
                self.relations[entry['name']] = Node(entry['name'], entry['manager'])
            else:
                self.relations[entry['name']].manager = entry['manager']
            if entry['manager'] not in self.relations:
                self.relations[entry['manager']] = Node(entry['manager'])
            else:
                self.relations[entry['manager']].employees.append(entry['name'])

    def findHierarchy(self):
        def __recursiveHelper(key_name, output):
            for employee in self.relations[key_name].employees:
                output += str(employee) + "\n" + "   "
                # print(output)
                __recursiveHelper(employee, output)
                # return output

        output = ""
        for relation in self.relations:
            print(relation)
            if relation == None:
                __recursiveHelper(self.relations[relation].name, output)

        return output


class Node():
    def __init__(self,name,manager=None):
        self.name = name
        self.manager = manager
        self.employees = []


relationship = Relationships()

relationship.buildHierarchy(test_input)
print(relationship.findHierarchy())
