#
# @lc app=leetcode id=234 lang=python3
#
# [234] Palindrome Linked List
#
# https://leetcode.com/problems/palindrome-linked-list/description/
#
# algorithms
# Easy (51.37%)
# Likes:    15581
# Dislikes: 839
# Total Accepted:    1.7M
# Total Submissions: 3.2M
# Testcase Example:  '[1,2,2,1]'
#
# Given the head of a singly linked list, return true if it is a palindrome or
# false otherwise.
#
#
# Example 1:
#
#
# Input: head = [1,2,2,1]
# Output: true
#
#
# Example 2:
#
#
# Input: head = [1,2]
# Output: false
#
#
#
# Constraints:
#
#
# The number of nodes in the list is in the range [1, 10^5].
# 0 <= Node.val <= 9
#
#
#
# Follow up: Could you do it in O(n) time and O(1) space?
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        length = 0
        node = head

        # get the length of the list
        while node:
            length += 1
            node = node.next

        node = head

        # go to the (second) middle node
        for _ in range((length + 1) // 2):
            node = node.next

        # reverse from the middle node to end of the list
        prev = next_node = None
        while node:
            next_node = node.next
            node.next = prev
            prev = node
            node = next_node

        # compare the last half of the list with the first half
        while prev:
            if prev.val != head.val:
                return False
            prev = prev.next
            head = head.next

        return True

# @lc code=end
