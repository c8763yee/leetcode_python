#
# @lc app=leetcode id=876 lang=python3
#
# [876] Middle of the Linked List
#
# https://leetcode.com/problems/middle-of-the-linked-list/description/
#
# algorithms
# Easy (76.93%)
# Likes:    10820
# Dislikes: 329
# Total Accepted:    1.6M
# Total Submissions: 2.1M
# Testcase Example:  '[1,2,3,4,5]'
#
# Given the head of a singly linked list, return the middle node of the linked
# list.
#
# If there are two middle nodes, return the second middle node.
#
#
# Example 1:
#
#
# Input: head = [1,2,3,4,5]
# Output: [3,4,5]
# Explanation: The middle node of the list is node 3.
#
#
# Example 2:
#
#
# Input: head = [1,2,3,4,5,6]
# Output: [4,5,6]
# Explanation: Since the list has two middle nodes with values 3 and 4, we
# return the second one.
#
#
#
# Constraints:
#
#
# The number of nodes in the list is in the range [1, 100].
# 1 <= Node.val <= 100
#
#
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        length = 0
        while node:
            length += 1
            node = node.next

        for _ in range(length // 2):
            head = head.next

        return head

# @lc code=end
