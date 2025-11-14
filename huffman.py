import heapq

class Node:
    def _init_(self, ch, freq):
        self.ch = ch
        self.freq = freq
        self.left = self.right = None
    def _lt_(self, other):
        return self.freq < other.freq

def huffman_encoding(text):
    
    freq = {ch: text.count(ch) for ch in set(text)}
    heap = [Node(ch, f) for ch, f in freq.items()]
    heapq.heapify(heap)


    while len(heap) > 1:
        l = heapq.heappop(heap)
        r = heapq.heappop(heap)
        new = Node(None, l.freq + r.freq)
        new.left, new.right = l, r
        heapq.heappush(heap, new)


    codes = {}
    def gen_code(node, code=""):
        if node:
            if node.ch:
                codes[node.ch] = code
            gen_code(node.left, code + "0")
            gen_code(node.right, code + "1")
    gen_code(heap[0])
    return codes


text = input("Enter text: ")
codes = huffman_encoding(text)

print("\nHuffman Codes:")
for ch, code in codes.items():
    print(ch, ":", code)

encoded = ''.join(codes[ch] for ch in text)
print("\nEncoded Text:", encoded) 
