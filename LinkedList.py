class Node():
    def __init__(self, data, link= None):
        self.data = data
        self.link = link
    def get_data(self):
        return self.data
    def set_data(self, d):
        self.data = d
    def get_link(self):
        return self.link
    def set_link(self, l):
        self.link = l
        
class LinkedList(Node):
    #herda os parametros e metodos de Node
    def __init__(self, head = None):
        #head é um Node, first Node
        self.head = head
    def get_head(self):
        a = self.head
        return a.get_data()
    def get_rear(self):
        a = self.head
        while a.get_link() is not None:
            a = a.get_link()
        return a.get_data()
    def insert(self, Node):
        #inserir no FIM
        a = self.head
        while a.get_link() is not None:
            a = a.get_link()
        a.set_link(Node)
    def insert_bg(Node):
        #inserir no COMEÇO
        pass
    def insert_ord(self, Node):
        a = self.head
        if Node.get_data() > self.get_rear():
            return self.insert(Node)
        elif a.data <= Node.get_data():
            while a.get_link().get_data() < Node.get_data():
                a = a.get_link()
            prox_Node = a.get_link()
            a.set_link(Node)
            Node.set_link(prox_Node)
        elif a.data >= Node.get_data():
            prox_Node = self.head
            self.head = Node
            Node.set_link(prox_Node)
    def remove(self, Node):
        pass
    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.get_link()
        nodes.append("None")
        return str(nodes)
    def __iter__(self):
        a = self.head
        while a.data is not None:
            yield a.data
            a = a.get_link()
'''node1 = Node(1)
ll1 = LinkedList(node1)
print(ll1.get_rear())
node2 = Node(2)
ll1.insert(node2)
print(ll1.get_rear())
node3 = Node(4)
ll1.insert(node3)
print(ll1.get_rear())
print(ll1.get_head(),ll1.get_rear())
node4 = Node(5)
ll1.insert_ord(node4)
node5= Node(-1)
ll1.insert_ord(node5)
print(ll1)
print(ll1.get_head(),ll1.get_rear())
for i in ll1:
    print(i)'''
        
