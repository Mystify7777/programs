// RemoveCycleLinkedList.java
public class RemoveCycleLinkedList {
    static class Node {
        int val;
        Node next;
        Node(int v) { val = v; }
    }

    // Detects if cycle exists
    public static boolean hasCycle(Node head) {
        Node slow = head, fast = head;
        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
            if (slow == fast) return true;
        }
        return false;
    }

    // Remove cycle if present
    public static void removeCycle(Node head) {
        if (head == null) return;
        Node slow = head, fast = head;
        boolean found = false;
        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
            if (slow == fast) { found = true; break; }
        }
        if (!found) return; // no cycle

        // Find start of cycle:
        slow = head;
        Node prev = null; // to keep track of node before the meeting point in the cycle
        while (slow != fast) {
            slow = slow.next;
            prev = fast;
            fast = fast.next;
        }
        // Now slow == fast == start of cycle. prev is the node just before start in the cycle
        // If prev is null, it means the cycle is at head and fast looped immediately — handle by moving to last node
        if (prev == null) {
            prev = fast;
            while (prev.next != fast) prev = prev.next;
        }
        prev.next = null; // break cycle
    }

    // Utility to print list up to some limit (to avoid infinite loop when testing bad cases)
    public static void printList(Node head) {
        Node cur = head;
        int i = 0;
        while (cur != null && i++ < 50) {
            System.out.print(cur.val + " -> ");
            cur = cur.next;
        }
        System.out.println(cur == null ? "null" : "...");
    }

    public static void main(String[] args) {
        // create list 1->2->3->4->5 and make cycle 5->3
        Node head = new Node(1);
        head.next = new Node(2);
        head.next.next = new Node(3);
        head.next.next.next = new Node(4);
        head.next.next.next.next = new Node(5);
        head.next.next.next.next.next = head.next.next; // cycle to node 3

        System.out.println("Has cycle before removal: " + hasCycle(head)); // true
        // avoid printList before removal (would loop)

        removeCycle(head);

        System.out.println("Has cycle after removal: " + hasCycle(head)); // false
        printList(head); // prints full list ending in null
    }
}
