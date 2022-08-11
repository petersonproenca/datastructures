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
        return a
    def set_head(self, Node):
        self.head = Node
    def get_rear(self):
        a = self.head
        while a.get_link() is not None:
            a = a.get_link()
        self.rear = a
        return self.rear
    def set_rear(self, Node):
        self.rear = Node
    def __len__(self):
        i = 0
        a = self.head
        while a.get_link() is not None:
            a = a.get_link()
            i +=1
        return i
    def insert(self, Node):
        #inserir no FIM
        a = self.head
        while a.get_link() is not None:
            a = a.get_link()
        a.set_link(Node)
    def insert_bg(Node):
        prox_Node = self.head
        self.head = Node
        Node.set_link(prox_Node)
    def insert_ord(self, Node):
        a = self.head
        if Node.get_data() > self.get_rear().get_data():
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
    def pop(self):
        #remover o ULTIMO
        a = self.head
        if a is self.get_rear(): 
            self.head = None
            return a.get_data()
        while a is not self.get_rear():
            prev = a
            a = a.get_link()
        prev.set_link(None)
        return a.get_data()
    
    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.get_data())
            node = node.get_link()
        #nodes.append("None")
        return str(nodes)
    def __iter__(self):
        a = self.head
        while a.get_data() is not None:
            yield a.get_data()
            a = a.get_link()
            if not a:break

'''node1 = Node(1)
ll1 = LinkedList(node1)
print(ll1.get_rear().get_data())
node2 = Node(2)
ll1.insert(node2)
print(ll1.get_rear().get_data())
node3 = Node(4)
ll1.insert(node3)
print(ll1.get_rear().get_data())
print(ll1.get_head().get_data(),ll1.get_rear().get_data())
node4 = Node(5)
ll1.insert_ord(node4)
node5= Node(-1)
ll1.insert_ord(node5)
print(ll1)
print(ll1.get_head().get_data(),'= head.data\n',ll1.get_rear().get_data(),'= rear.data' )
for i in ll1:
    print(i)
nn0 = Node(284)
nn1=Node(2284022)
ll2 = LinkedList(nn1)
ll2.insert(nn0)
ll2.insert(Node(1238))
ll2.insert(Node(-1))
print(ll2)
print(ll2.pop());print(ll2);print(len(ll2))
print(ll2.pop());print(ll2);print(len(ll2))'''
