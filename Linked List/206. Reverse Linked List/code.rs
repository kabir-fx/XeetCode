// Definition for singly-linked list.
// #[derive(PartialEq, Eq, Clone, Debug)]
// pub struct ListNode {
//   pub val: i32,
//   pub next: Option<Box<ListNode>>
// }
// 
// impl ListNode {
//   #[inline]
//   fn new(val: i32) -> Self {
//     ListNode {
//       next: None,
//       val
//     }
//   }
// }

impl Solution {
    pub fn reverse_list(head: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
        let mut prev: Option<Box<ListNode>> = None;
        let mut cur = head;

        // If there is Some node found then -
        while let Some(mut node) = cur {
        // Create a temp. node, take() - Takes the value out of the option,leaving a None in its place.
            let temp = node.next.take();
            node.next = prev.take();        // Reverse the pointer
            prev = Some(node);              // Increment the prev pointer
            cur = temp;                     // Increment the current pointer
        }

        prev
    }
}
