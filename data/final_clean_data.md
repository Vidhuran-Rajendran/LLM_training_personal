# LINKED LIST

## Concept
A linked list is a data structure consisting of nodes where each node contains a value and a pointer to the next node. The last node points to null.

Linked lists maintain head and tail pointers to allow efficient insertion.

## Complexity
- Insertion → O(1)
- Deletion → O(n)
- Searching → O(n)

## Why Linked List?
- Dynamic size (no resizing required)
- No memory copy like arrays
- Efficient insertion at head and tail

---

## Linked List Deletion Cases

Deleting a node in a singly linked list involves:

1. List is empty  
2. Node is the only node  
3. Node is the head  
4. Node is the tail  
5. Node is in the middle  
6. Value not found  

---

## Reverse Traversal Issue

Reverse traversal in a singly linked list is inefficient because:
- No backward pointer  
- Must find previous node each time  

Time Complexity → O(n²)

---

## Doubly Linked List

A doubly linked list has:
- Next pointer  
- Previous pointer  

Advantage:
- Efficient forward and backward traversal  

---

# BINARY SEARCH TREE (BST)

## Concept
A Binary Search Tree is a tree where:
- Left subtree values < node value  
- Right subtree values ≥ node value  

This property holds recursively.

---

## Complexity

- Insertion → O(log n)
- Search → O(log n)
- Deletion → O(log n)

⚠ Only if tree is **balanced**

---

## BST Deletion Cases

1. Node is a leaf  
2. Node has only right subtree  
3. Node has only left subtree  
4. Node has both subtrees → replace with largest node in left subtree  

---

## BST Problem

BST can become **unbalanced**, causing:

→ O(n) time complexity  
→ behaves like a linked list  

---

## Tree Traversals

- Preorder → root → left → right  
- Postorder → left → right → root  
- Inorder → left → root → right (sorted output ✅)  
- Breadth-first → level by level using queue  

---

# AVL TREE

## Concept

AVL is a **self-balancing Binary Search Tree**

Rule:
- Height difference between left and right subtree ≤ 1  

---

## Why AVL?

Prevents BST problem:
- Always balanced  
- Guarantees O(log n) operations  

---

## Rotations

Used to maintain balance:
- Left rotation  
- Right rotation  
- Left-right rotation  
- Right-left rotation  

---

## AVL vs BST (IMPORTANT)

Binary Search Tree:
- Can become unbalanced  
- Worst case → O(n)

AVL Tree:
- Always balanced  
- Height difference ≤ 1  
- Worst case → O(log n)  

---

# HEAP (MIN HEAP)

## Concept

Heap is a tree-based structure (usually implemented using an array)

Min Heap property:
- Parent ≤ children  
- Root contains smallest value  

---

## Array Representation

Index relationships:
- Parent → (i - 1) / 2  
- Left child → 2i + 1  
- Right child → 2i + 2  

---

## Heap Insertion

Steps:

1. Insert at next available index  
2. Compare with parent  
3. If child < parent → swap  
4. Repeat upward (heapify)  

Time Complexity → O(log n)

---

## Heap Deletion

Steps:

1. Find node  
2. Replace with last element  
3. Restore heap order  

Time Complexity → O(log n)

---

## Heap Search

- Requires traversal → O(n)  

---

## Heap Use Cases

- Priority Queue  
- Sorting (Heap Sort)  

---

# SUMMARY

| Structure | Best Use |
|----------|--------|
| Linked List | Dynamic size, fast insertion |
| BST | Ordered data, fast search (if balanced) |
| AVL | Guaranteed balanced BST |
| Heap | Priority-based operations |