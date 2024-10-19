# LC 206 - https://leetcode.com/problems/reverse-linked-list/description/
def reverse_ll(head):
  if not head:
    return []
  if not head.next:
    return head
  prev = None
  curr = head
  nxt = None
  while curr:
    nxt = curr.next
    curr.next = prev
    prev = curr
    curr = nxt
  return prev
