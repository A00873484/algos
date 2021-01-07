# solution found removes consecutive nodes but not all nodes that are a part of a consecutive node.
# solution dosn't facter in all possible combinations and simply seeks to eliminate all nodes that lead to a sum of zero.

class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

def removeConsecutiveSumTo0(node):
  # Fill this in.
  if node.next:
    removeConsecutiveSumTo0(node.next)
  else:
    return None
  remainder = 0
  current = node.next
  while current:
      remainder += current.value
      if remainder is 0:
          node.next = current.next
          break
      current = current.next
  if not node.next:
    return node
  elif node.value + node.next.value is 0:
    return None
  return node
  

node = Node(10)
node.next = Node(-3)
node.next.next = Node(5)
node.next.next.next = Node(-3)
node.next.next.next.next = Node(1)
node.next.next.next.next.next = Node(4)
node.next.next.next.next.next.next = Node(-4)
node.next.next.next.next.next.next.next = Node(2)
node = removeConsecutiveSumTo0(node)
while node:
  print node.value,
  node = node.next
# 10

#Input: 10 -> -3 -> 5 -> -3 -> 1 -> 4 -> -4 -> 5
#Output: 10