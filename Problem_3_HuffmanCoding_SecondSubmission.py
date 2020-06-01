import sys

class Node(object):
    def __init__(self, value = None):
        self.value = value
        self.left = None
        self.right = None

    def get_value(self):
        return self.value

    def set_char(self, value):
        self.value = value

    def set_left_child(self, node):
        self.left = node

    def set_right_child(self, node):
        self.right = node

    def get_left_child(self):
        return self.left

    def get_right_child(self):
        return self.right

    def has_left_child(self):
        return self.left != None

    def has_right_child(self):
        return self.right != None

class Tree():
    def __init__(self, node):
        self.root = node

    def get_root(self):
        return self.root

def huffman_encoding(data):

    letters = []
    char_list = []

    if not data:
        #Since your testing code need to have format(sys.getsizeof(int(encoded_data, base = 2))))
        #operation, if the output is None, there will be an error. We can resolve this issue in
        #another way if we made changes in the test code to allow for null return
        data = "There's no input! Please put something in again!"

    if len(data) == 1:
        new_node = Node(data)

    for char in data:
        if char not in letters:
            letters.append(char)
            freq = data.count(char)
            char_list.append([char, freq])

    char_list = sorted(char_list, key = lambda x: x[1])

    node_list = []

    for n in char_list:
        new_node = Node(n)
        node_list.append(new_node)

    node_list = sorted(node_list, key = lambda x: x.value[1])

    new_nodelist = huffman_treebuild(node_list)
    new_tree = Tree(new_nodelist[0])
    root = new_tree.get_root()
    new_list = []

    if root.left == None and root.right == None:
        root.value[1] = "0"
        bilist = root.value
        if bilist[0] in data:
            data = data.replace(bilist[0], bilist[1])
    else:
        root.value[1] = ""
        bilist = assign_bi(root, new_list)
        for code in bilist:
            if code[0] in data:
                data = data.replace(code[0], code[1])

    return data, new_tree

def assign_bi(tree_root, binary_list):

    if tree_root == None:
        return None

    current_node = tree_root


    if current_node.left:
        if len(current_node.left.value[0]) > 1:
            current_node.left.value[1] = current_node.value[1] + '0'
        elif len(current_node.left.value[0]) == 1:
            current_node.left.value[1] = current_node.value[1] + '0'
            binary_list.append(current_node.left.value)

    if current_node.right:
        if len(current_node.right.value[0]) > 1:
            current_node.right.value[1] = current_node.value[1] + '1'
        elif len(current_node.right.value[0]) == 1:
            current_node.right.value[1] = current_node.value[1] + '1'
            binary_list.append(current_node.right.value)

    assign_bi(current_node.left, binary_list)
    assign_bi(current_node.right, binary_list)

    return binary_list


def huffman_treebuild(node_list):

    if len(node_list) < 2:
        return node_list

    new_fre = node_list[0].value[1] + node_list[1].value[1]
    new_str = node_list[0].value[0] + node_list[1].value[0]
    new_list = [new_str, new_fre]
    new_node = Node(new_list)
    new_node.left = node_list[0]
    new_node.right = node_list[1]
    node_list = node_list[2:]
    node_list.append(new_node)
    node_list = sorted(node_list, key = lambda x: x.value[1])

    new_nodelist = huffman_treebuild(node_list)
    return new_nodelist


def huffman_decoding(data,tree):

    if data == None:
        return None

    root = tree.get_root()
    if len(data) <= 1:
        return root.value[0]

    decode = huffman_decoding_func(data, root, [])
    return "".join(decode)

def huffman_decoding_func(data, root_node , new_list):

    origin = root_node

    if (origin.left is None) and (origin.right is None):
        for char in data:
            new_list.append(origin.value[0])
    else:
        for char in data:
            if char == '0':
                origin = origin.left
                if len(origin.value[0]) == 1:
                    new_list.append(origin.value[0])
                    origin = root_node

            if char == '1':
                origin = origin.right
                if len(origin.value[0]) == 1:
                    new_list.append(origin.value[0])
                    origin = root_node

    return new_list



## Test case 1 - Edge Case
if __name__ == "__main__":
    codes = {}

    a_great_sentence = " "

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base = 2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))

## Test case 2 - Edge Case
if __name__ == "__main__":
    codes = {}

    a_great_sentence = ""

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base = 2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))

## Test case 3
if __name__ == "__main__":
    codes = {}

    a_great_sentence = "The bird is the word"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))
