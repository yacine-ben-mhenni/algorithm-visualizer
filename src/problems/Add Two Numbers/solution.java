class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        // Dummy node to simplify appending nodes to the result list
        ListNode dummy = new ListNode(0);
        ListNode current = dummy;
        int carry = 0;

        // Traverse both lists while at least one is non-null
        while (l1 != null || l2 != null) {
            // Get values from current nodes or use 0 if the node is null
            int val1 = (l1 != null) ? l1.val : 0;
            int val2 = (l2 != null) ? l2.val : 0;

            // Compute sum and carry
            int sum = val1 + val2 + carry;
            carry = sum / 10;

            // Add the current digit to the result list
            current.next = new ListNode(sum % 10);
            current = current.next;

            // Move to the next nodes in l1 and l2
            if (l1 != null) l1 = l1.next;
            if (l2 != null) l2 = l2.next;
        }

        // Handle any remaining carry
        if (carry > 0) {
            current.next = new ListNode(carry);
        }

        // Return the result list, skipping the dummy node
        return dummy.next;
    }
}