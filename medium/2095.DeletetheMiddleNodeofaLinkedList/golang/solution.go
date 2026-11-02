/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func deleteMiddle(head *ListNode) *ListNode {
	fast := &head
	slow := &head
	for *fast != nil && (*fast).Next != nil {
		fast = &((*fast).Next.Next)
		slow = &((*slow).Next)
	}
	*slow = (*slow).Next
	return head
}