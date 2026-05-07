
## **Chapter 2** 

## **Linked Lists** 

Linked lists can be thought of from a high level perspective as being a series of nodes. Each node has at least a single pointer to the next node, and in the last node’s case a null pointer representing that there are no more nodes in the linked list. 

In DSA our implementations of linked lists always maintain head and tail pointers so that insertion at either the head or tail of the list is a constant time operation. Random insertion is excluded from this and will be a linear operation. As such, linked lists in DSA have the following characteristics: 

1. Insertion is _O_ (1) 

2. Deletion is _O_ ( _n_ ) 

3. Searching is _O_ ( _n_ ) 

Out of the three operations the one that stands out is that of insertion. In DSA we chose to always maintain pointers (or more aptly references) to the node(s) at the head and tail of the linked list and so performing a traditional insertion to either the front or back of the linked list is an _O_ (1) operation. An exception to this rule is performing an insertion before a node that is neither the head nor tail in a singly linked list. When the node we are inserting before is somewhere in the middle of the linked list (known as random insertion) the complexity is _O_ ( _n_ ). In order to add before the designated node we need to traverse the linked list to find that node’s current predecessor. This traversal yields an _O_ ( _n_ ) run time. 

This data structure is trivial, but linked lists have a few key points which at times make them very attractive: 

1. the list is dynamically resized, thus it incurs no copy penalty like an array or vector would eventually incur; and 

2. insertion is _O_ (1). 

## **2.1 Singly Linked List** 

Singly linked lists are one of the most primitive data structures you will find in this book. Each node that makes up a singly linked list consists of a value, and a reference to the next node (if any) in the list. 

9 

_CHAPTER 2. LINKED LISTS_ 

10 

Figure 2.1: Singly linked list node 

**==> picture [55 x 46] intentionally omitted <==**

Figure 2.2: A singly linked list populated with integers 



In general when people talk about insertion with respect to linked lists of any form they implicitly refer to the adding of a node to the tail of the list. When you use an API like that of DSA and you see a general purpose method that adds a node to the list, you can assume that you are adding the node to the tail of the list not the head. 

Adding a node to a singly linked list has only two cases: 

   1. _head_ = _∅_ in which case the node we are adding is now both the _head_ and _tail_ of the list; or 

   2. we simply need to append our node onto the end of the list updating the _tail_ reference appropriately. 

- 1) **algorithm** Add( _value_ ) 

- 2) **Pre:** _value_ is the value to add to the list 

- 3) **Post:** _value_ has been placed at the tail of the list 

- 4) _n ←_ node( _value_ ) 

- 5) **if** _head_ = _∅_ 

- 6) _head ← n_ 

- 7) _tail ← n_ 

- 8) **else** 

- 9) _tail_ .Next _← n_ 10) _tail ← n_ 

- 11) **end if** 

- 12) **end** Add 

As an example of the previous algorithm consider adding the following sequence of integers to the list: 1, 45, 60, and 12, the resulting list is that of Figure 2.2. 

## **2.1.2 Searching** 

Searching a linked list is straightforward: we simply traverse the list checking the value we are looking for with the value of each node in the linked list. The algorithm listed in this section is very similar to that used for traversal in _§_ 2.1.4. 


## **2.1.3 Deletion** 

Deleting a node from a linked list is straightforward but there are a few cases we need to account for: 

1. the list is empty; or 

2. the node to remove is the only node in the linked list; or 

3. we are removing the head node; or 

4. we are removing the tail node; or 

5. the node to remove is somewhere in between the head and tail; or 

6. the item to remove doesn’t exist in the linked list 

The algorithm whose cases we have described will remove a node from anywhere within a list irrespective of whether the node is the _head_ etc. If you know that items will only ever be removed from the _head_ or _tail_ of the list then you can create much more concise algorithms. In the case of always removing from the front of the linked list deletion becomes an _O_ (1) operation. 




## **2.1.4 Traversing the list** 

Traversing a singly linked list is the same as that of traversing a doubly linked list (defined in _§_ 2.2). You start at the head of the list and continue until you come across a node that is _∅_ . The two cases are as follows: 

1. _node_ = _∅_ , we have exhausted all nodes in the linked list; or 

2. we must update the _node_ reference to be _node_ .Next. 

The algorithm described is a very simple one that makes use of a simple _while_ loop to check the first case. 

_CHAPTER 2. LINKED LISTS_ 



## **2.1.5 Traversing the list in reverse order** 

Traversing a singly linked list in a forward manner (i.e. left to right) is simple as demonstrated in _§_ 2.1.4. However, what if we wanted to traverse the nodes in the linked list in reverse order for some reason? The algorithm to perform such a traversal is very simple, and just like demonstrated in _§_ 2.1.3 we will need to acquire a reference to the predecessor of a node, even though the fundamental characteristics of the nodes that make up a singly linked list make this an expensive operation. For each node, finding its predecessor is an _O_ ( _n_ ) operation, so over the course of traversing the whole list backwards the cost becomes _O_ ( _n_[2] ). 

Figure 2.3 depicts the following algorithm being applied to a linked list with the integers 5, 10, 1, and 40. 


This algorithm is only of real interest when we are using singly linked lists, as you will soon see that doubly linked lists (defined in _§_ 2.2) make reverse list traversal simple and efficient, as shown in _§_ 2.2.3. 

## **2.2 Doubly Linked List** 

Doubly linked lists are very similar to singly linked lists. The only difference is that each node has a reference to both the next and previous nodes in the list. 

_CHAPTER 2. LINKED LISTS_ 

14 

**==> picture [318 x 389] intentionally omitted <==**

Figure 2.3: Reverse traveral of a singly linked list 

Figure 2.4: Doubly linked list node 

_CHAPTER 2. LINKED LISTS_ 

15 

The following algorithms for the doubly linked list are exactly the same as those listed previously for the singly linked list: 

1. Searching (defined in _§_ 2.1.2) 

2. Traversal (defined in _§_ 2.1.4) 

## **2.2.1 Insertion** 

The only major difference between the algorithm in _§_ 2.1.1 is that we need to remember to bind the previous pointer of _n_ to the previous tail node if _n_ was not the first node to be inserted into the list. 



Figure 2.5 shows the doubly linked list after adding the sequence of integers defined in _§_ 2.1.1. 

**==> picture [394 x 44] intentionally omitted <==**

Figure 2.5: Doubly linked list populated with integers 

## **2.2.2 Deletion** 

As you may of guessed the cases that we use for deletion in a doubly linked list are exactly the same as those defined in _§_ 2.1.3. Like insertion we have the added task of binding an additional reference ( _Previous_ ) to the correct value. 



## **2.2.3 Reverse Traversal** 

Singly linked lists have a forward only design, which is why the reverse traversal algorithm defined in _§_ 2.1.5 required some creative invention. Doubly linked lists make reverse traversal as simple as forward traversal (defined in _§_ 2.1.4) except that we start at the tail node and update the pointers in the opposite direction. Figure 2.6 shows the reverse traversal algorithm in action. 

_CHAPTER 2. LINKED LISTS_ 

17 

**==> picture [394 x 44] intentionally omitted <==**

Figure 2.6: Doubly linked list reverse traversal 

- 1) **algorithm** ReverseTraversal( _tail_ ) 

- 2) **Pre:** _tail_ is the tail node of the list to traverse 

- 3) **Post:** the list has been traversed in reverse order 4) _n ← tail_ 5) **while** _n ̸_ = _∅_ 6) **yield** _n_ .Value 7) _n ← n_ .Previous 

8) **end while** 9) **end** ReverseTraversal 

## **2.3 Summary** 

Linked lists are good to use when you have an unknown number of items to store. Using a data structure like an array would require you to specify the size up front; exceeding that size involves invoking a resizing algorithm which has a linear run time. You should also use linked lists when you will only remove nodes at either the head or tail of the list to maintain a constant run time. This requires maintaining pointers to the nodes at the head and tail of the list but the memory overhead will pay for itself if this is an operation you will be performing many times. 

What linked lists are not very good for is random insertion, accessing nodes by index, and searching. At the expense of a little memory (in most cases 4 bytes would suffice), and a few more read/writes you could maintain a _count_ variable that tracks how many items are contained in the list so that accessing such a primitive property is a constant operation - you just need to update _count_ during the insertion and deletion algorithms. 

Singly linked lists should be used when you are only performing basic insertions. In general doubly linked lists are more accommodating for non-trivial operations on a linked list. 

We recommend the use of a doubly linked list when you require forwards and backwards traversal. For the most cases this requirement is present. For example, consider a token stream that you want to parse in a recursive descent fashion. Sometimes you will have to backtrack in order to create the correct parse tree. In this scenario a doubly linked list is best as its design makes bi-directional traversal much simpler and quicker than that of a singly linked 

_CHAPTER 2. LINKED LISTS_ 18 

list. 

## **Chapter 3** 

## **Binary Search Tree** 

Binary search trees (BSTs) are very simple to understand. We start with a root node with value _x_ , where the left subtree of _x_ contains nodes with values _< x_ and the right subtree contains nodes whose values are _≥ x_ . Each node follows the same rules with respect to nodes in their left and right subtrees. 

BSTs are of interest because they have operations which are favourably fast: insertion, look up, and deletion can all be done in _O_ ( _log n_ ) time. It is important to note that the _O_ ( _log n_ ) times for these operations can only be attained if the BST is reasonably balanced; for a tree data structure with self balancing properties see AVL tree defined in _§_ 7). 

In the following examples you can assume, unless used as a parameter alias that _root_ is a reference to the root node of the tree. 

**==> picture [148 x 170] intentionally omitted <==**

**----- Start of picture text -----**<br>
23<br>14 31<br>7 17<br>9<br>**----- End of picture text -----**<br>


Figure 3.1: Simple unbalanced binary search tree 

19 

_CHAPTER 3. BINARY SEARCH TREE_ 

20 

## **3.1 Insertion** 

As mentioned previously insertion is an _O_ ( _log n_ ) operation provided that the tree is moderately balanced. 



The insertion algorithm is split for a good reason. The first algorithm (nonrecursive) checks a very core base case - whether or not the tree is empty. If the tree is empty then we simply create our root node and finish. In all other cases we invoke the recursive _InsertNode_ algorithm which simply guides us to the first appropriate place in the tree to put _value_ . Note that at each stage we perform a binary chop: we either choose to recurse into the left subtree or the right by comparing the new value with that of the current node. For any totally ordered type, no value can simultaneously satisfy the conditions to place it in both subtrees. 



## **3.2 Searching** 

Searching a BST is even simpler than insertion. The pseudocode is self-explanatory but we will look briefly at the premise of the algorithm nonetheless. 

We have talked previously about insertion, we go either left or right with the right subtree containing values that are _≥ x_ where _x_ is the value of the node we are inserting. When searching the rules are made a little more atomic and at any one time we have four cases to consider: 


## **3.3 Deletion** 

Removing a node from a BST is fairly straightforward, with four cases to consider: 

1. the value to remove is a leaf node; or 

2. the value to remove has a right subtree, but no left subtree; or 

3. the value to remove has a left subtree, but no right subtree; or 

4. the value to remove has both a left and right subtree in which case we promote the largest value in the left subtree. 

There is also an implicit fifth case whereby the node to be removed is the only node in the tree. This case is already covered by the first, but should be noted as a possibility nonetheless. 

Of course in a BST a value may occur more than once. In such a case the first occurrence of that value in the BST will be removed. 

**==> picture [225 x 163] intentionally omitted <==**

**----- Start of picture text -----**<br>
#4: Right subtree<br>23<br>      and left subtree<br>#3: Left subtree<br>14 31<br>      no right subtree<br>#2: Right subtree 7<br>      no left subtree<br>#1: Leaf Node 9<br>**----- End of picture text -----**<br>


Figure 3.2: binary search tree deletion cases 

The _Remove_ algorithm given below relies on two further helper algorithms named _FindParent_ , and _FindNode_ which are described in _§_ 3.4 and _§_ 3.5 respectively. 

_CHAPTER 3. BINARY SEARCH TREE_ 


24 

## **3.4 Finding the parent of a given node** 

The purpose of this algorithm is simple - to return a reference (or pointer) to the parent node of the one with the given value. We have found that such an algorithm is very useful, especially when performing extensive tree transformations. 

1) **algorithm** FindParent( _value_ , _root_ ) 

2) **Pre:** _value_ is the value of the node we want to find the parent of 3) _root_ is the root node of the BST and is ! = _∅_ 

4) **Post:** a reference to the parent node of _value_ if found; otherwise _∅_ 

5) **if** _value_ = _root_ .Value 6) **return** _∅_ 7) **end if** 8) **if** _value < root_ .Value 9) **if** _root_ .Left = _∅_ 10) **return** _∅_ 11) **else if** _root_ .Left.Value = _value_ 12) **return** _root_ 13) **else** 14) **return** FindParent( _value_ , _root_ .Left) 15) **end if** 16) **else** 17) **if** _root_ .Right = _∅_ 18) **return** _∅_ 19) **else if** _root_ .Right.Value = _value_ 20) **return** _root_ 21) **else** 22) **return** FindParent( _value_ , _root_ .Right) 23) **end if** 24) **end if** 25) **end** FindParent 

A special case in the above algorithm is when the specified value does not exist in the BST, in which case we return _∅_ . Callers to this algorithm must take account of this possibility unless they are already certain that a node with the specified value exists. 

## **3.5 Attaining a reference to a node** 

This algorithm is very similar to _§_ 3.4, but instead of returning a reference to the parent of the node with the specified value, it returns a reference to the node itself. Again, _∅_ is returned if the value isn’t found. 

_CHAPTER 3. BINARY SEARCH TREE_ 

25 

1) **algorithm** FindNode( _root_ , _value_ ) 2) **Pre:** _value_ is the value of the node we want to find the parent of 3) _root_ is the root node of the BST 4) **Post:** a reference to the node of _value_ if found; otherwise _∅_ 5) **if** _root_ = _∅_ 6) **return** _∅_ 7) **end if** 8) **if** _root_ .Value = _value_ 9) **return** _root_ 10) **else if** _value < root_ .Value 11) **return** FindNode( _root_ .Left, _value_ ) 12) **else** 13) **return** FindNode( _root_ .Right, _value_ ) 14) **end if** 15) **end** FindNode 

Astute readers will have noticed that the _FindNode_ algorithm is exactly the same as the _Contains_ algorithm (defined in _§_ 3.2) with the modification that we are returning a reference to a node not _true_ or _false_ . Given _FindNode_ , the easiest way of implementing _Contains_ is to call _FindNode_ and compare the return value with _∅_ . 

## **3.6 Finding the smallest and largest values in the binary search tree** 

To find the smallest value in a BST you simply traverse the nodes in the left subtree of the BST always going left upon each encounter with a node, terminating when you find a node with no left subtree. The opposite is the case when finding the largest value in the BST. Both algorithms are incredibly simple, and are listed simply for completeness. 

The base case in both _FindMin_ , and _FindMax_ algorithms is when the Left ( _FindMin_ ), or Right ( _FindMax_ ) node references are _∅_ in which case we have reached the last node. 

- 1) **algorithm** FindMin( _root_ ) 

2) **Pre:** _root_ is the root node of the BST 3) _root_ = _∅_ 4) **Post:** the smallest value in the BST is located 5) **if** _root_ .Left = _∅_ 6) **return** _root_ .Value 7) **end if** 8) FindMin( _root_ .Left) 9) **end** FindMin 

_CHAPTER 3. BINARY SEARCH TREE_ 

26 

1) **algorithm** FindMax( _root_ ) 2) **Pre:** _root_ is the root node of the BST 3) _root_ = _∅_ 4) **Post:** the largest value in the BST is located 5) **if** _root_ .Right = _∅_ 6) **return** _root_ .Value 7) **end if** 8) FindMax( _root_ .Right) 9) **end** FindMax 

## **3.7 Tree Traversals** 

There are various strategies which can be employed to traverse the items in a tree; the choice of strategy depends on which node visitation order you require. In this section we will touch on the traversals that DSA provides on all data structures that derive from _BinarySearchTree_ . 

## **3.7.1 Preorder** 

When using the preorder algorithm, you visit the root first, then traverse the left subtree and finally traverse the right subtree. An example of preorder traversal is shown in Figure 3.3. 

- 1) **algorithm** Preorder( _root_ ) 

- 2) **Pre:** _root_ is the root node of the BST 

3) **Post:** the nodes in the BST have been visited in preorder 4) **if** _root_ = _∅_ 5) **yield** _root_ .Value 6) Preorder( _root_ .Left) 7) Preorder( _root_ .Right) 8) **end if** 9) **end** Preorder 

## **3.7.2 Postorder** 

This algorithm is very similar to that described in _§_ 3.7.1, however the value of the node is yielded after traversing both subtrees. An example of postorder traversal is shown in Figure 3.4. 

- 1) **algorithm** Postorder( _root_ ) 

2) **Pre:** _root_ is the root node of the BST 

3) **Post:** the nodes in the BST have been visited in postorder 4) **if** _root_ = _∅_ 5) Postorder( _root_ .Left) 6) Postorder( _root_ .Right) 7) **yield** _root_ .Value 8) **end if** 9) **end** Postorder 

_CHAPTER 3. BINARY SEARCH TREE_ 

27 

**==> picture [345 x 278] intentionally omitted <==**

**----- Start of picture text -----**<br>
23 23 23<br>14 31 14 31 14 31<br>7 17 7 17 7 17<br>9 9 9<br>(a) (b) (c)<br>23 23 23<br>14 31 14 31 14 31<br>7 17 7 17 7 17<br>9 9 9<br>(d) (e) (f)<br>**----- End of picture text -----**<br>


Figure 3.3: Preorder visit binary search tree example 

_CHAPTER 3. BINARY SEARCH TREE_ 

28 

**==> picture [345 x 278] intentionally omitted <==**

**----- Start of picture text -----**<br>
23 23 23<br>14 31 14 31 14 31<br>7 17 7 17 7 17<br>9 9 9<br>(a) (b) (c)<br>23 23 23<br>14 31 14 31 14 31<br>7 17 7 17 7 17<br>9 9 9<br>(d) (e) (f)<br>**----- End of picture text -----**<br>


Figure 3.4: Postorder visit binary search tree example 

_CHAPTER 3. BINARY SEARCH TREE_ 

29 

## **3.7.3 Inorder** 

Another variation of the algorithms defined in _§_ 3.7.1 and _§_ 3.7.2 is that of inorder traversal where the value of the current node is yielded in between traversing the left subtree and the right subtree. An example of inorder traversal is shown in Figure 3.5. 

**==> picture [345 x 279] intentionally omitted <==**

**----- Start of picture text -----**<br>
23 23 23<br>14 31 14 31 14 31<br>7 17 7 17 7 17<br>9 9 9<br>(a) (b) (c)<br>23 23 23<br>14 31 14 31 14 31<br>7 17 7 17 7 17<br>9 9 9<br>(d) (e) (f)<br>**----- End of picture text -----**<br>


Figure 3.5: Inorder visit binary search tree example 

- 1) **algorithm** Inorder( _root_ ) 

- 2) **Pre:** _root_ is the root node of the BST 

- 3) **Post:** the nodes in the BST have been visited in inorder 4) **if** _root_ = _∅_ 5) Inorder( _root_ .Left) 6) **yield** _root_ .Value 7) Inorder( _root_ .Right) 8) **end if** 9) **end** Inorder 

One of the beauties of inorder traversal is that values are yielded in their comparison order. In other words, when traversing a populated BST with the inorder strategy, the yielded sequence would have property _xi ≤ xi_ +1 _∀i_ . 

_CHAPTER 3. BINARY SEARCH TREE_ 

30 

## **3.7.4 Breadth First** 

Traversing a tree in breadth first order yields the values of all nodes of a particular depth in the tree before any deeper ones. In other words, given a depth _d_ we would visit the values of all nodes at _d_ in a left to right fashion, then we would proceed to _d_ + 1 and so on until we hade no more nodes to visit. An example of breadth first traversal is shown in Figure 3.6. 

Traditionally breadth first traversal is implemented using a list (vector, resizeable array, etc) to store the values of the nodes visited in breadth first order and then a queue to store those nodes that have yet to be visited. 

**==> picture [345 x 278] intentionally omitted <==**

**----- Start of picture text -----**<br>
23 23 23<br>14 31 14 31 14 31<br>7 17 7 17 7 17<br>9 9 9<br>(a) (b) (c)<br>23 23 23<br>14 31 14 31 14 31<br>7 17 7 17 7 17<br>9 9 9<br>(d) (e) (f)<br>**----- End of picture text -----**<br>


Figure 3.6: Breadth First visit binary search tree example 

_CHAPTER 3. BINARY SEARCH TREE_ 

31 

1) **algorithm** BreadthFirst( _root_ ) 2) **Pre:** _root_ is the root node of the BST 3) **Post:** the nodes in the BST have been visited in breadth first order 4) _q ←_ queue 5) **while** _root_ = _∅_ 6) **yield** _root_ .Value 7) **if** _root_ .Left = _∅_ 8) _q_ .Enqueue( _root_ .Left) 9) **end if** 10) **if** _root_ .Right = _∅_ 11) _q_ .Enqueue( _root_ .Right) 12) **end if** 13) **if** ! _q_ .IsEmpty() 14) _root ← q_ .Dequeue() 15) **else** 16) _root ←∅_ 17) **end if** 18) **end while** 19) **end** BreadthFirst 

## **3.8 Summary** 

A binary search tree is a good solution when you need to represent types that are ordered according to some custom rules inherent to that type. With logarithmic insertion, lookup, and deletion it is very effecient. Traversal remains linear, but there are many ways in which you can visit the nodes of a tree. Trees are recursive data structures, so typically you will find that many algorithms that operate on a tree are recursive. 

The run times presented in this chapter are based on a pretty big assumption - that the binary search tree’s left and right subtrees are reasonably balanced. We can only attain logarithmic run times for the algorithms presented earlier when this is true. A binary search tree does not enforce such a property, and the run times for these operations on a pathologically unbalanced tree become linear: such a tree is effectively just a linked list. Later in _§_ 7 we will examine an AVL tree that enforces self-balancing properties to help attain logarithmic run times. 

## **Chapter 4** 

## **Heap** 

A heap can be thought of as a simple tree data structure, however a heap usually employs one of two strategies: 

1. min heap; or 

2. max heap 

Each strategy determines the properties of the tree and its values. If you were to choose the min heap strategy then each parent node would have a value that is _≤_ than its children. For example, the node at the root of the tree will have the smallest value in the tree. The opposite is true for the max heap strategy. In this book you should assume that a heap employs the min heap strategy unless otherwise stated. 

Unlike other tree data structures like the one defined in _§_ 3 a heap is generally implemented as an array rather than a series of nodes which each have references to other nodes. The nodes are conceptually the same, however, having at most two children. Figure 4.1 shows how the tree (not a heap data structure) (12 7(3 2) 6(9 )) would be represented as an array. The array in Figure 4.1 is a result of simply adding values in a top-to-bottom, left-to-right fashion. Figure 4.2 shows arrows to the direct left and right child of each value in the array. 

This chapter is very much centred around the notion of representing a tree as an array and because this property is key to understanding this chapter Figure 4.3 shows a step by step process to represent a tree data structure as an array. In Figure 4.3 you can assume that the default capacity of our array is eight. 

Using just an array is often not sufficient as we have to be up front about the size of the array to use for the heap. Often the run time behaviour of a program can be unpredictable when it comes to the size of its internal data structures, so we need to choose a more dynamic data structure that contains the following properties: 

1. we can specify an initial size of the array for scenarios where we know the upper storage limit required; and 

2. the data structure encapsulates resizing algorithms to grow the array as required at run time 

32 

_CHAPTER 4. HEAP_ 

33 

**==> picture [205 x 33] intentionally omitted <==**

Figure 4.1: Array representation of a simple tree data structure 

**==> picture [205 x 33] intentionally omitted <==**

Figure 4.2: Direct children of the nodes in an array representation of a tree data structure 

1. Vector 

2. ArrayList 

3. List 

Figure 4.1 does not specify how we would handle adding null references to the heap. This varies from case to case; sometimes null values are prohibited entirely; in other cases we may treat them as being smaller than any non-null value, or indeed greater than any non-null value. You will have to resolve this ambiguity yourself having studied your requirements. For the sake of clarity we will avoid the issue by prohibiting null values. 

Because we are using an array we need some way to calculate the index of a parent node, and the children of a node. The required expressions for this are defined as follows for a node at _index_ : 

1. ( _index −_ 1)/2 (parent index) 

2. 2 _∗ index_ + 1 (left child) 

3. 2 _∗ index_ + 2 (right child) 

In Figure 4.4 a) represents the calculation of the right child of 12 (2 _∗_ 0 + 2); and b) calculates the index of the parent of 3 ((3 _−_ 1)/2). 

## **4.1 Insertion** 

Designing an algorithm for heap insertion is simple, but we must ensure that heap order is preserved after each insertion. Generally this is a post-insertion operation. Inserting a value into the next free slot in an array is simple: we just need to keep track of the next free index in the array as a counter, and increment it after each insertion. Inserting our value into the heap is the first part of the algorithm; the second is validating heap order. In the case of min-heap ordering this requires us to swap the values of a parent and its child if the value of the child is _<_ the value of its parent. We must do this for each subtree containing the value we just inserted. 

_CHAPTER 4. HEAP_ 

34 

**==> picture [92 x 84] intentionally omitted <==**

**==> picture [92 x 83] intentionally omitted <==**

**==> picture [93 x 199] intentionally omitted <==**

Figure 4.3: Converting a tree data structure to its array counterpart 

_CHAPTER 4. HEAP_ 

35 

**==> picture [205 x 33] intentionally omitted <==**

Figure 4.4: Calculating node properties 

The run time efficiency for heap insertion is _O_ ( _log n_ ). The run time is a by product of verifying heap order as the first part of the algorithm (the actual insertion into the array) is _O_ (1). 

Figure 4.5 shows the steps of inserting the values 3, 9, 12, 7, and 1 into a min-heap. 

_CHAPTER 4. HEAP_ 

36 

**==> picture [333 x 351] intentionally omitted <==**

Figure 4.5: Inserting values into a min-heap 

_CHAPTER 4. HEAP_ 

37 

1) **algorithm** Add( _value_ ) 2) **Pre:** _value_ is the value to add to the heap 3) Count is the number of items in the heap 4) **Post:** the value has been added to the heap 5) _heap_ [Count] _← value_ 6) Count _←_ Count +1 7) MinHeapify() 8) **end** Add 

- 1) **algorithm** MinHeapify() 

2) **Pre:** Count is the number of items in the heap 3) _heap_ is the array used to store the heap items 4) **Post:** the heap has preserved min heap ordering 5) _i ←_ Count _−_ 1 6) **while** _i >_ 0 **and** _heap_ [ _i_ ] _< heap_ [( _i −_ 1)/2] 7) Swap( _heap_ [ _i_ ], _heap_ [( _i −_ 1)/2] 8) _i ←_ ( _i −_ 1)/2 9) **end while** 10) **end** MinHeapify 

The design of the _MaxHeapify_ algorithm is very similar to that of the _MinHeapify_ algorithm, the only difference is that the _<_ operator in the second condition of entering the while loop is changed to _>_ . 

## **4.2 Deletion** 

Just as for insertion, deleting an item involves ensuring that heap ordering is preserved. The algorithm for deletion has three steps: 

1. the index of the value to delete 

2. put the last value in the heap at the index location of the item to delete 

3. verify heap ordering for each subtree which used to include the value 

_CHAPTER 4. HEAP_ 

38 

1) **algorithm** Remove( _value_ ) 2) **Pre:** _value_ is the value to remove from the heap 3) _left_ , and _right_ are updated alias’ for 2 _∗ index_ + 1, and 2 _∗ index_ + 2 respectively 4) Count is the number of items in the heap 5) _heap_ is the array used to store the heap items 6) **Post:** _value_ is located in the heap and removed, true; otherwise false 7) // step 1 8) _index ←_ FindIndex( _heap_ , _value_ ) 9) **if** _index <_ 0 10) **return false** 11) **end if** 12) Count _←_ Count _−_ 1 13) // step 2 14) _heap_ [ _index_ ] _← heap_ [Count] 15) // step 3 16) **while** _left <_ Count **and** _heap_ [ _index_ ] _> heap_ [ _left_ ] **or** _heap_ [ _index_ ] _> heap_ [ _right_ ] 17) // promote smallest key from subtree 18) **if** _heap_ [ _left_ ] _< heap_ [ _right_ ] 19) Swap( _heap_ , _left_ , _index_ ) 20) _index ← left_ 21) **else** 22) Swap( _heap_ , _right_ , _index_ ) 23) _index ← right_ 24) **end if** 25) **end while** 26) **return true** 27) **end** Remove 

Figure 4.6 shows the _Remove_ algorithm visually, removing 1 from a heap containing the values 1, 3, 9, 12, and 13. In Figure 4.6 you can assume that we have specified that the backing array of the heap should have an initial capacity of eight. 

Please note that in our deletion algorithm that we don’t default the removed value in the _heap_ array. If you are using a heap for reference types, i.e. objects that are allocated on a heap you will want to free that memory. This is important in both unmanaged, and managed languages. In the latter we will want to null that empty hole so that the garbage collector can reclaim that memory. If we were to not null that hole then the object could still be reached and thus won’t be garbage collected. 

## **4.3 Searching** 

Searching a heap is merely a matter of traversing the items in the heap array sequentially, so this operation has a run time complexity of _O_ ( _n_ ). The search can be thought of as one that uses a breadth first traversal as defined in _§_ 3.7.4 to visit the nodes within the heap to check for the presence of a specified item. 

_CHAPTER 4. HEAP_ 

39 

**==> picture [274 x 34] intentionally omitted <==**

**==> picture [274 x 54] intentionally omitted <==**

**==> picture [274 x 34] intentionally omitted <==**

**==> picture [274 x 54] intentionally omitted <==**

Figure 4.6: Deleting an item from a heap 

_CHAPTER 4. HEAP_ 

40 

1) **algorithm** Contains( _value_ ) 2) **Pre:** _value_ is the value to search the heap for 3) Count is the number of items in the heap 4) _heap_ is the array used to store the heap items 5) **Post:** _value_ is located in the heap, in which case true; otherwise false 6) _i ←_ 0 7) **while** _i <_ Count **and** _heap_ [ _i_ ] = _value_ 8) _i ← i_ + 1 9) **end while** 10) **if** _i <_ Count 11) **return true** 12) **else** 13) **return false** 14) **end if** 15) **end** Contains 

The problem with the previous algorithm is that we don’t take advantage of the properties in which all values of a heap hold, that is the property of the heap strategy being used. For instance if we had a heap that didn’t contain the value 4 we would have to exhaust the whole backing heap array before we could determine that it wasn’t present in the heap. Factoring in what we know about the heap we can optimise the search algorithm by including logic which makes use of the properties presented by a certain heap strategy. 

Optimising to deterministically state that a value is in the heap is not that straightforward, however the problem is a very interesting one. As an example consider a min-heap that doesn’t contain the value 5. We can only rule that the value is not in the heap if 5 _>_ the parent of the current node being inspected and _<_ the current node being inspected _∀_ nodes at the current level we are traversing. If this is the case then 5 cannot be in the heap and so we can provide an answer without traversing the rest of the heap. If this property is not satisfied for any level of nodes that we are inspecting then the algorithm will indeed fall back to inspecting all the nodes in the heap. The optimisation that we present can be very common and so we feel that the extra logic within the loop is justified to prevent the expensive worse case run time. 

The following algorithm is specifically designed for a min-heap. To tailor the algorithm for a max-heap the two comparison operations in the **else if** condition within the inner **while** loop should be flipped. 

_CHAPTER 4. HEAP_ 

41 

1) **algorithm** Contains( _value_ ) 2) **Pre:** _value_ is the value to search the heap for 3) Count is the number of items in the heap 4) _heap_ is the array used to store the heap items 5) **Post:** _value_ is located in the heap, in which case true; otherwise false 6) _start ←_ 0 7) _nodes ←_ 1 8) **while** _start <_ Count 9) _start ← nodes −_ 1 10) _end ← nodes_ + _start_ 11) _count ←_ 0 12) **while** _start <_ Count **and** _start < end_ 13) **if** _value_ = _heap_ [ _start_ ] 14) **return true** 15) **else if** _value >_ Parent( _heap_ [ _start_ ]) **and** _value < heap_ [ _start_ ] 16) _count ← count_ + 1 17) **end if** 18) _start ← start_ + 1 19) **end while** 20) **if** _count_ = _nodes_ 21) **return false** 22) **end if** 23) _nodes ← nodes ∗_ 2 24) **end while** 25) **return false** 26) **end** Contains 

The new _Contains_ algorithm determines if the _value_ is not in the heap by checking whether _count_ = _nodes_ . In such an event where this is true then we can confirm that _∀_ nodes _n_ at level _i_ : _value >_ Parent( _n_ ), _value < n_ thus there is no possible way that _value_ is in the heap. As an example consider Figure 4.7. If we are searching for the value 10 within the min-heap displayed it is obvious that we don’t need to search the whole heap to determine 9 is not present. We can verify this after traversing the nodes in the second level of the heap as the previous expression defined holds true. 

## **4.4 Traversal** 

As mentioned in _§_ 4.3 traversal of a heap is usually done like that of any other array data structure which our heap implementation is based upon. As a result you traverse the array starting at the initial array index (0 in most languages) and then visit each value within the array until you have reached the upper bound of the heap. You will note that in the search algorithm that we use _Count_ as this upper bound rather than the actual physical bound of the allocated array. _Count_ is used to partition the conceptual heap from the actual array implementation of the heap: we only care about the items in the heap, not the whole array—the latter may contain various other bits of data as a result of heap mutation. 

_CHAPTER 4. HEAP_ 

42 

**==> picture [120 x 67] intentionally omitted <==**

Figure 4.7: Determining 10 is not in the heap after inspecting the nodes of Level 2 

**==> picture [205 x 55] intentionally omitted <==**

Figure 4.8: Living and dead space in the heap backing array 

If you have followed the advice we gave in the deletion algorithm then a heap that has been mutated several times will contain some form of default value for items no longer in the heap. Potentially you will have at most _LengthOf_ ( _heapArray_ ) _− Count_ garbage values in the backing heap array data structure. The garbage values of course vary from platform to platform. To make things simple the garbage value of a reference type will be simple _∅_ and 0 for a value type. 

Figure 4.8 shows a heap that you can assume has been mutated many times. For this example we can further assume that at some point the items in indexes 3 _−_ 5 actually contained references to live objects of type _T_ . In Figure 4.8 subscript is used to disambiguate separate objects of _T_ . 

From what you have read thus far you will most likely have picked up that traversing the heap in any other order would be of little benefit. The heap property only holds for the subtree of each node and so traversing a heap in any other fashion requires some creative intervention. Heaps are not usually traversed in any other way than the one prescribed previously. 

## **4.5 Summary** 

Heaps are most commonly used to implement priority queues (see _§_ 6.2 for a sample implementation) and to facilitate heap sort. As discussed in both the insertion _§_ 4.1 and deletion _§_ 4.2 sections a heap maintains heap order according to the selected ordering strategy. These strategies are referred to as min-heap, 

_CHAPTER 4. HEAP_ 

43 

and max heap. The former strategy enforces that the value of a parent node is less than that of each of its children, the latter enforces that the value of the parent is greater than that of each of its children. 

When you come across a heap and you are not told what strategy it enforces you should assume that it uses the min-heap strategy. If the heap can be configured otherwise, e.g. to use max-heap then this will often require you to state this explicitly. The heap abides progressively to a strategy during the invocation of the insertion, and deletion algorithms. The cost of such a policy is that upon each insertion and deletion we invoke algorithms that have logarithmic run time complexities. While the cost of maintaining the strategy might not seem overly expensive it does still come at a price. We will also have to factor in the cost of dynamic array expansion at some stage. This will occur if the number of items within the heap outgrows the space allocated in the heap’s backing array. It may be in your best interest to research a good initial starting size for your heap array. This will assist in minimising the impact of dynamic array resizing. 

## **Chapter 5** 

## **Sets** 

A set contains a number of values, in no particular order. The values within the set are distinct from one another. 

Generally set implementations tend to check that a value is not in the set before adding it, avoiding the issue of repeated values from ever occurring. 

This section does not cover set theory in depth; rather it demonstrates briefly the ways in which the values of sets can be defined, and common operations that may be performed upon them. 

The notation _A_ = _{_ 4 _,_ 7 _,_ 9 _,_ 12 _,_ 0 _}_ defines a set _A_ whose values are listed within the curly braces. 

Given the set _A_ defined previously we can say that 4 is a member of _A_ denoted by 4 _∈ A_ , and that 99 is not a member of _A_ denoted by 99 _∈/ A_ . 

Often defining a set by manually stating its members is tiresome, and more importantly the set may contain a large number of values. A more concise way of defining a set and its members is by providing a series of properties that the values of the set must satisfy. For example, from the definition _A_ = _{x|x >_ 0 _, x_ % 2 = 0 _}_ the set _A_ contains only positive integers that are even. _x_ is an alias to the current value we are inspecting and to the right hand side of _|_ are the properties that _x_ must satisfy to be in the set _A_ . In this example, _x_ must be _>_ 0, and the remainder of the arithmetic expression _x/_ 2 must be 0. You will be able to note from the previous definition of the set _A_ that the set can contain an infinite number of values, and that the values of the set _A_ will be all even integers that are a member of the natural numbers set N, where N = _{_ 1 _,_ 2 _,_ 3 _, ...}_ . Finally in this brief introduction to sets we will cover set intersection and union, both of which are very common operations (amongst many others) performed on sets. The union set can be defined as follows _A ∪ B_ = _{x | x ∈ A or x ∈ B}_ , and intersection _A ∩ B_ = _{x | x ∈ A and x ∈ B}_ . Figure 5.1 demonstrates set intersection and union graphically. 

Given the set definitions _A_ = _{_ 1 _,_ 2 _,_ 3 _}_ , and _B_ = _{_ 6 _,_ 2 _,_ 9 _}_ the union of the two sets is _A ∪ B_ = _{_ 1 _,_ 2 _,_ 3 _,_ 6 _,_ 9 _}_ , and the intersection of the two sets is _A ∩ B_ = _{_ 2 _}_ . 

Both set union and intersection are sometimes provided within the framework associated with mainstream languages. This is the case in .NET 3.5[1] where such algorithms exist as extension methods defined in the type _System.Linq.Enumerable_[2] , as a result DSA does not provide implementations of 

> 1 `http://www.microsoft.com/NET/` 

> 2 `http://msdn.microsoft.com/en-us/library/system.linq.enumerable_members.aspx` 

44 

_CHAPTER 5. SETS_ 

45 

**==> picture [242 x 103] intentionally omitted <==**

Figure 5.1: a) _A ∩ B_ ; b) _A ∪ B_ 

these algorithms. Most of the algorithms defined in _System.Linq.Enumerable_ deal mainly with sequences rather than sets exclusively. 

Set union can be implemented as a simple traversal of both sets adding each item of the two sets to a new union set. 

1) **algorithm** Union( _set_ 1, _set_ 2) 2) **Pre:** _set_ 1, and _set_ 2 _̸_ = _∅_ 3) _union_ is a set 3) **Post:** A union of _set_ 1, and _set_ 2 has been created 4) **foreach** _item_ **in** _set_ 1 5) _union_ .Add( _item_ ) 6) **end foreach** 7) **foreach** _item_ **in** _set_ 2 8) _union_ .Add( _item_ ) 9) **end foreach** 10) **return** _union_ 11) **end** Union 

The run time of our _Union_ algorithm is _O_ ( _m_ + _n_ ) where _m_ is the number of items in the first set and _n_ is the number of items in the second set. This runtime applies only to sets that exhibit _O_ (1) insertions. 

Set intersection is also trivial to implement. The only major thing worth pointing out about our algorithm is that we traverse the set containing the fewest items. We can do this because if we have exhausted all the items in the smaller of the two sets then there are no more items that are members of both sets, thus we have no more items to add to the intersection set. 

_CHAPTER 5. SETS_ 

46 

1) **algorithm** Intersection( _set_ 1, _set_ 2) 2) **Pre:** _set_ 1, and _set_ 2 _̸_ = _∅_ 3) _intersection_ , and _smallerSet_ are sets 3) **Post:** An intersection of _set_ 1, and _set_ 2 has been created 4) **if** _set_ 1.Count _< set_ 2.Count 5) _smallerSet ← set_ 1 6) **else** 7) _smallerSet ← set_ 2 8) **end if** 9) **foreach** _item_ **in** _smallerSet_ 10) **if** _set_ 1.Contains( _item_ ) **and** _set_ 2.Contains( _item_ ) 11) _intersection_ .Add( _item_ ) 12) **end if** 13) **end foreach** 14) **return** _intersection_ 15) **end** Intersection 

The run time of our _Intersection_ algorithm is _O_ ( _n_ ) where _n_ is the number of items in the smaller of the two sets. Just like our _Union_ algorithm a linear runtime can only be attained when operating on a set with _O_ (1) insertion. 

## **5.1 Unordered** 

Sets in the general sense do not enforce the explicit ordering of their members. For example the members of _B_ = _{_ 6 _,_ 2 _,_ 9 _}_ conform to no ordering scheme because it is not required. 

Most libraries provide implementations of unordered sets and so DSA does not; we simply mention it here to disambiguate between an unordered set and ordered set. 

We will only look at insertion for an unordered set and cover briefly why a hash table is an efficient data structure to use for its implementation. 

## **5.1.1 Insertion** 

An unordered set can be efficiently implemented using a hash table as its backing data structure. As mentioned previously we only add an item to a set if that item is not already in the set, so the backing data structure we use must have a quick look up and insertion run time complexity. 

A hash map generally provides the following: 

1. _O_ (1) for insertion 

2. approaching _O_ (1) for look up 

The above depends on how good the hashing algorithm of the hash table is, but most hash tables employ incredibly efficient general purpose hashing algorithms and so the run time complexities for the hash table in your library of choice should be very similar in terms of efficiency. 

_CHAPTER 5. SETS_ 

47 

## **5.2 Ordered** 

An ordered set is similar to an unordered set in the sense that its members are distinct, but an ordered set enforces some predefined comparison on each of its members to produce a set whose members are ordered appropriately. 

In DSA 0.5 and earlier we used a binary search tree (defined in _§_ 3) as the internal backing data structure for our ordered set. From versions 0.6 onwards we replaced the binary search tree with an AVL tree primarily because AVL is balanced. 

The ordered set has its order realised by performing an inorder traversal upon its backing tree data structure which yields the correct ordered sequence of set members. 

Because an ordered set in DSA is simply a wrapper for an AVL tree that additionally ensures that the tree contains unique items you should read _§_ 7 to learn more about the run time complexities associated with its operations. 

## **5.3 Summary** 

Sets provide a way of having a collection of unique objects, either ordered or unordered. 

When implementing a set (either ordered or unordered) it is key to select the correct backing data structure. As we discussed in _§_ 5.1.1 because we check first if the item is already contained within the set before adding it we need this check to be as quick as possible. For unordered sets we can rely on the use of a hash table and use the key of an item to determine whether or not it is already contained within the set. Using a hash table this check results in a near constant run time complexity. Ordered sets cost a little more for this check, however the logarithmic growth that we incur by using a binary search tree as its backing data structure is acceptable. 

Another key property of sets implemented using the approach we describe is that both have favourably fast look-up times. Just like the check before insertion, for a hash table this run time complexity should be near constant. Ordered sets as described in 3 perform a binary chop at each stage when searching for the existence of an item yielding a logarithmic run time. 

We can use sets to facilitate many algorithms that would otherwise be a little less clear in their implementation. For example in _§_ 11.4 we use an unordered set to assist in the construction of an algorithm that determines the number of repeated words within a string. 

## **Chapter 6** 

## **Queues** 

Queues are an essential data structure that are found in vast amounts of software from user mode to kernel mode applications that are core to the system. Fundamentally they honour a first in first out (FIFO) strategy, that is the item first put into the queue will be the first served, the second item added to the queue will be the second to be served and so on. 

A traditional queue only allows you to access the item at the front of the queue; when you add an item to the queue that item is placed at the back of the queue. 

Historically queues always have the following three core methods: 

**Enqueue:** places an item at the back of the queue; 

**Dequeue:** retrieves the item at the front of the queue, and removes it from the queue; 

- **Peek:**[1] retrieves the item at the front of the queue without removing it from the queue 

As an example to demonstrate the behaviour of a queue we will walk through a scenario whereby we invoke each of the previously mentioned methods observing the mutations upon the queue data structure. The following list describes the operations performed upon the queue in Figure 6.1: 

1. Enqueue(10) 

2. Enqueue(12) 

3. Enqueue(9) 

4. Enqueue(8) 

5. Enqueue(3) 

6. Dequeue() 

7. Peek() 

- 1This operation is sometimes referred to as Front 

48 

_CHAPTER 6. QUEUES_ 

49 

8. Enqueue(33) 

9. Peek() 

10. Dequeue() 

## **6.1 A standard queue** 

A queue is implicitly like that described prior to this section. In DSA we don’t provide a standard queue because queues are so popular and such a core data structure that you will find pretty much every mainstream library provides a queue data structure that you can use with your language of choice. In this section we will discuss how you can, if required, implement an efficient queue data structure. 

The main property of a queue is that we have access to the item at the front of the queue. The queue data structure can be efficiently implemented using a singly linked list (defined in _§_ 2.1). A singly linked list provides _O_ (1) insertion and deletion run time complexities. The reason we have an _O_ (1) run time complexity for deletion is because we only ever remove items from the front of queues (with the Dequeue operation). Since we always have a pointer to the item at the head of a singly linked list, removal is simply a case of returning the value of the old head node, and then modifying the head pointer to be the next node of the old head node. The run time complexity for searching a queue remains the same as that of a singly linked list: _O_ ( _n_ ). 

## **6.2 Priority Queue** 

Unlike a standard queue where items are ordered in terms of who arrived first, a priority queue determines the order of its items by using a form of custom comparer to see which item has the highest priority. Other than the items in a priority queue being ordered by priority it remains the same as a normal queue: you can only access the item at the front of the queue. 

A sensible implementation of a priority queue is to use a heap data structure (defined in _§_ 4). Using a heap we can look at the first item in the queue by simply returning the item at index 0 within the heap array. A heap provides us with the ability to construct a priority queue where the items with the highest priority are either those with the smallest value, or those with the largest. 

## **6.3 Double Ended Queue** 

Unlike the queues we have talked about previously in this chapter a double ended queue allows you to access the items at both the front, and back of the queue. A double ended queue is commonly known as a deque which is the name we will here on in refer to it as. 

A deque applies no prioritization strategy to its items like a priority queue does, items are added in order to either the front of back of the deque. The former properties of the deque are denoted by the programmer utilising the data structures exposed interface. 

_CHAPTER 6. QUEUES_ 

50 

**==> picture [172 x 545] intentionally omitted <==**

Figure 6.1: Queue mutations 

_CHAPTER 6. QUEUES_ 

51 

Deque’s provide front and back specific versions of common queue operations, e.g. you may want to enqueue an item to the front of the queue rather than the back in which case you would use a method with a name along the lines of _EnqueueFront_ . The following list identifies operations that are commonly supported by deque’s: 

- EnqueueFront 

- EnqueueBack 

- DequeueFront 

- DequeueBack 

- PeekFront 

- PeekBack 

Figure 6.2 shows a deque after the invocation of the following methods (inorder): 

1. EnqueueBack(12) 

2. EnqueueFront(1) 

3. EnqueueBack(23) 

4. EnqueueFront(908) 

5. DequeueFront() 

6. DequeueBack() 

The operations have a one-to-one translation in terms of behaviour with those of a normal queue, or priority queue. In some cases the set of algorithms that add an item to the back of the deque may be named as they are with normal queues, e.g. _EnqueueBack_ may simply be called _Enqueue_ an so on. Some frameworks also specify explicit behaviour’s that data structures must adhere to. This is certainly the case in .NET where most collections implement an interface which requires the data structure to expose a standard _Add_ method. In such a scenario you can safely assume that the _Add_ method will simply enqueue an item to the back of the deque. 

With respect to algorithmic run time complexities a deque is the same as a normal queue. That is enqueueing an item to the back of a the queue is _O_ (1), additionally enqueuing an item to the front of the queue is also an _O_ (1) operation. 

A deque is a wrapper data structure that uses either an array, or a doubly linked list. Using an array as the backing data structure would require the programmer to be explicit about the size of the array up front, this would provide an obvious advantage if the programmer could deterministically state the maximum number of items the deque would contain at any one time. Unfortunately in most cases this doesn’t hold, as a result the backing array will inherently incur the expense of invoking a resizing algorithm which would most likely be an _O_ ( _n_ ) operation. Such an approach would also leave the library developer 

_CHAPTER 6. QUEUES_ 

52 

**==> picture [138 x 340] intentionally omitted <==**

Figure 6.2: Deque data structure after several mutations 

_CHAPTER 6. QUEUES_ 

53 

to look at array minimization techniques as well, it could be that after several invocations of the resizing algorithm and various mutations on the deque later that we have an array taking up a considerable amount of memory yet we are only using a few small percentage of that memory. An algorithm described would also be _O_ ( _n_ ) yet its invocation would be harder to gauge strategically. 

To bypass all the aforementioned issues a deque typically uses a doubly linked list as its baking data structure. While a node that has two pointers consumes more memory than its array item counterpart it makes redundant the need for expensive resizing algorithms as the data structure increases in size dynamically. With a language that targets a garbage collected virtual machine memory reclamation is an opaque process as the nodes that are no longer referenced become unreachable and are thus marked for collection upon the next invocation of the garbage collection algorithm. With C++ or any other language that uses explicit memory allocation and deallocation it will be up to the programmer to decide when the memory that stores the object can be freed. 

## **6.4 Summary** 

With normal queues we have seen that those who arrive first are dealt with first; that is they are dealt with in a first-in-first-out (FIFO) order. Queues can be ever so useful; for example the Windows CPU scheduler uses a different queue for each priority of process to determine which should be the next process to utilise the CPU for a specified time quantum. Normal queues have constant insertion and deletion run times. Searching a queue is fairly unusual—typically you are only interested in the item at the front of the queue. Despite that, searching is usually exposed on queues and typically the run time is linear. 

In this chapter we have also seen priority queues where those at the front of the queue have the highest priority and those near the back have the lowest. One implementation of a priority queue is to use a heap data structure as its backing store, so the run times for insertion, deletion, and searching are the same as those for a heap (defined in _§_ 4). 

Queues are a very natural data structure, and while they are fairly primitive they can make many problems a lot simpler. For example the breadth first search defined in _§_ 3.7.4 makes extensive use of queues. 

## **Chapter 7** 

## **AVL Tree** 

In the early 60’s G.M. Adelson-Velsky and E.M. Landis invented the first selfbalancing binary search tree data structure, calling it AVL Tree. 

An AVL tree is a binary search tree (BST, defined in _§_ 3) with a self-balancing condition stating that the difference between the height of the left and right subtrees cannot be no more than one, see Figure 7.1. This condition, restored after each tree modification, forces the general shape of an AVL tree. Before continuing, let us focus on why balance is so important. Consider a binary search tree obtained by starting with an empty tree and inserting some values in the following order 1,2,3,4,5. 

The BST in Figure 7.2 represents the worst case scenario in which the running time of all common operations such as search, insertion and deletion are _O_ ( _n_ ). By applying a balance condition we ensure that the worst case running time of each common operation is _O_ ( _log n_ ). The height of an AVL tree with _n_ nodes is _O_ ( _log n_ ) regardless of the order in which values are inserted. 

The AVL balance condition, known also as the node balance factor represents an additional piece of information stored for each node. This is combined with a technique that efficiently restores the balance condition for the tree. In an AVL tree the inventors make use of a well-known technique called tree rotation. 

**==> picture [161 x 66] intentionally omitted <==**

**----- Start of picture text -----**<br>
h<br>h+1<br>**----- End of picture text -----**<br>


Figure 7.1: The left and right subtrees of an AVL tree differ in height by at most 1 

54 

_CHAPTER 7. AVL TREE_ 

55 

**==> picture [160 x 207] intentionally omitted <==**

**----- Start of picture text -----**<br>
1<br>2<br>3<br>4<br>5<br>**----- End of picture text -----**<br>


Figure 7.2: Unbalanced binary search tree 

**==> picture [315 x 154] intentionally omitted <==**

**----- Start of picture text -----**<br>
2 4<br>1 4 2 5<br>3 5 1 3<br>a) b)<br>**----- End of picture text -----**<br>


Figure 7.3: Avl trees, insertion order: -a)1,2,3,4,5 -b)1,5,4,3,2 

_CHAPTER 7. AVL TREE_ 

56 

## **7.1 Tree Rotations** 

A tree rotation is a constant time operation on a binary search tree that changes the shape of a tree while preserving standard BST properties. There are left and right rotations both of them decrease the height of a BST by moving smaller subtrees down and larger subtrees up. 

**==> picture [382 x 117] intentionally omitted <==**

**----- Start of picture text -----**<br>
14 8<br>Right Rotation<br>8 24 2 14<br>Left Rotation<br>2 11 11 24<br>**----- End of picture text -----**<br>


Figure 7.4: Tree left and right rotations 

_CHAPTER 7. AVL TREE_ 

57 

1) **algorithm** LeftRotation( _node_ ) 2) **Pre:** _node_ .Right ! = _∅_ 3) **Post:** _node_ .Right is the new root of the subtree, 4) _node_ has become _node_ .Right’s left child and, 5) BST properties are preserved 6) _RightNode ← node_ .Right 7) _node_ .Right _← RightNode_ .Left 8) _RightNode_ .Left _← node_ 9) **end** LeftRotation 

1) **algorithm** RightRotation( _node_ ) 2) **Pre:** _node_ .Left ! = _∅_ 3) **Post:** _node_ .Left is the new root of the subtree, 4) _node_ has become _node_ .Left’s right child and, 5) BST properties are preserved 6) _LeftNode ← node_ .Left 7) _node_ .Left _← LeftNode_ .Right 8) _LeftNode_ .Right _← node_ 9) **end** RightRotation 

The right and left rotation algorithms are symmetric. Only pointers are changed by a rotation resulting in an _O_ (1) runtime complexity; the other fields present in the nodes are not changed. 

## **7.2 Tree Rebalancing** 

The algorithm that we present in this section verifies that the left and right subtrees differ at most in height by 1. If this property is not present then we perform the correct rotation. 

Notice that we use two new algorithms that represent double rotations. These algorithms are named _LeftAndRightRotation_ , and _RightAndLeftRotation_ . The algorithms are self documenting in their names, e.g. _LeftAndRightRotation_ first performs a left rotation and then subsequently a right rotation. 

_CHAPTER 7. AVL TREE_ 

58 

- 1) **algorithm** CheckBalance( _current_ ) 

- 2) **Pre:** _current_ is the node to start from balancing 

- 3) **Post:** _current_ height has been updated while tree balance is if needed 4) restored through rotations 

- 5) **if** _current_ .Left = _∅_ **and** _current_ .Right = _∅_ 6) _current_ .Height = -1; 7) **else** 8) _current_ .Height = Max( _Height_ ( _current_ .Left), _Height_ ( _current.Right_ )) + 1 9) **end if** 10) **if** _Height_ ( _current_ .Left) - _Height_ ( _current_ .Right) _>_ 1 11) **if** _Height_ ( _current_ .Left.Left) - _Height_ ( _current_ .Left.Right) _>_ 0 12) RightRotation( _current_ ) 13) **else** 14) LeftAndRightRotation( _current_ ) 15) **end if** 16) **else if** _Height_ ( _current_ .Left) - _Height_ ( _current_ .Right) _< −_ 1 17) **if** _Height_ ( _current_ .Right.Left) - _Height_ ( _current_ .Right.Right) _<_ 0 18) LeftRotation( _current_ ) 19) **else** 20) RightAndLeftRotation( _current_ ) 21) **end if** 22) **end if** 23) **end** CheckBalance 

## **7.3 Insertion** 

AVL insertion operates first by inserting the given value the same way as BST insertion and then by applying rebalancing techniques if necessary. The latter is only performed if the AVL property no longer holds, that is the left and right subtrees height differ by more than 1. Each time we insert a node into an AVL tree: 

1. We go down the tree to find the correct point at which to insert the node, in the same manner as for BST insertion; then 

2. we travel up the tree from the inserted node and check that the node balancing property has not been violated; if the property hasn’t been violated then we need not rebalance the tree, the opposite is true if the balancing property has been violated. 

_CHAPTER 7. AVL TREE_ 

59 

1) **algorithm** Insert( _value_ ) 2) **Pre:** _value_ has passed custom type checks for type _T_ 3) **Post:** _value_ has been placed in the correct location in the tree 4) **if** _root_ = _∅_ 5) _root ←_ node( _value_ ) 6) **else** 7) InsertNode( _root_ , _value_ ) 8) **end if** 9) **end** Insert 

1) **algorithm** InsertNode( _current_ , _value_ ) 2) **Pre:** _current_ is the node to start from 3) **Post:** _value_ has been placed in the correct location in the tree while 4) preserving tree balance 5) **if** _value < current_ .Value 6) **if** _current_ .Left = _∅_ 7) _current_ .Left _←_ node( _value_ ) 8) **else** 9) InsertNode( _current_ .Left, _value_ ) 10) **end if** 11) **else** 12) **if** _current_ .Right = _∅_ 13) _current_ .Right _←_ node( _value_ ) 14) **else** 15) InsertNode( _current_ .Right, _value_ ) 16) **end if** 17) **end if** 18) CheckBalance(current) 19) **end** InsertNode 

## **7.4 Deletion** 

Our balancing algorithm is like the one presented for our BST (defined in _§_ 3.3). The major difference is that we have to ensure that the tree still adheres to the AVL balance property after the removal of the node. If the tree doesn’t need to be rebalanced and the value we are removing is contained within the tree then no further step are required. However, when the value is in the tree and its removal upsets the AVL balance property then we must perform the correct rotation(s). 

_CHAPTER 7. AVL TREE_ 

60 

1) **algorithm** Remove( _value_ ) 

- 2) **Pre:** _value_ is the value of the node to remove, _root_ is the root node 3) of the Avl 

- 4) **Post:** node with _value_ is removed and tree rebalanced if found in which 5) case yields true, otherwise false 6) _nodeToRemove ← root_ 7) _parent ←∅_ 8) _Stackpath ←_ root 9) **while** _nodeToRemove ̸_ = _∅_ and _nodeToRemove.V alue_ = _V alue_ 10) _parent_ = _nodeToRemove_ 11) **if** _value < nodeToRemove_ .Value 12) _nodeToRemove ←_ nodeToRemove.Left 13) **else** 14) _nodeToRemove ←_ nodeToRemove.Right 15) **end if** 16) path.Push(nodeToRemove) 17) **end while** 18) **if** _nodeToRemove_ = _∅_ 19) **return false** // value not in Avl 20) **end if** 21) _parent ←_ FindParent( _value_ ) 22) **if** _count_ = 1 // _count_ keeps track of the # of nodes in the Avl 23) _root ←∅_ // we are removing the only node in the Avl 24) **else if** _nodeToRemove_ .Left = _∅_ **and** _nodeToRemove_ .Right = _null_ 25) // case #1 26) **if** _nodeToRemove_ .Value _< parent_ .Value 27) _parent_ .Left _←∅_ 28) **else** 29) _parent_ .Right _←∅_ 30) **end if** 31) **else if** _nodeToRemove_ .Left = _∅_ **and** _nodeToRemove_ .Right = _∅_ 32) // case # 2 

- 33) **if** _nodeToRemove_ .Value _< parent_ .Value 34) _parent_ .Left _← nodeToRemove_ .Right 35) **else** 36) _parent_ .Right _← nodeToRemove_ .Right 37) **end if** 38) **else if** _nodeToRemove_ .Left = _∅_ **and** _nodeToRemove_ .Right = _∅_ 39) // case #3 

- 40) **if** _nodeToRemove_ .Value _< parent_ .Value 41) _parent_ .Left _← nodeToRemove_ .Left 42) **else** 43) _parent_ .Right _← nodeToRemove_ .Left 44) **end if** 45) **else** 

- 46) // case #4 

- 47) _largestV alue ← nodeToRemove_ .Left 48) **while** _largestV alue_ .Right = _∅_ 

- 49) // find the largest value in the left subtree of _nodeToRemove_ 50) _largestV alue ← largestV alue_ .Right 

_CHAPTER 7. AVL TREE_ 

61 

51) **end while** 52) // set the parents’ Right pointer of _largestV alue_ to _∅_ 53) FindParent( _largestV alue_ .Value).Right _←∅_ 54) _nodeToRemove_ .Value _← largestV alue_ .Value 55) **end if** 56) **while** _path.Count >_ 0 57) CheckBalance(path.Pop()) // we trackback to the root node check balance 58) **end while** 59) _count ← count −_ 1 60) **return true** 61) **end** Remove 

## **7.5 Summary** 

The AVL tree is a sophisticated self balancing tree. It can be thought of as the smarter, younger brother of the binary search tree. Unlike its older brother the AVL tree avoids worst case linear complexity runtimes for its operations. The AVL tree guarantees via the enforcement of balancing algorithms that the left and right subtrees differ in height by at most 1 which yields at most a logarithmic runtime complexity. 

## **Part II** 

## **Algorithms** 

62 

## **Chapter 8** 

## **Sorting** 

All the sorting algorithms in this chapter use data structures of a specific type to demonstrate sorting, e.g. a 32 bit integer is often used as its associated operations (e.g. _<_ , _>_ , etc) are clear in their behaviour. 

The algorithms discussed can easily be translated into generic sorting algorithms within your respective language of choice. 

## **8.1 Bubble Sort** 

One of the most simple forms of sorting is that of comparing each item with every other item in some list, however as the description may imply this form of sorting is not particularly effecient _O_ ( _n_[2] ). In it’s most simple form bubble sort can be implemented as two loops. 

- 1) **algorithm** BubbleSort( _list_ ) 

2) **Pre:** _list_ = _∅_ 3) **Post:** _list_ has been sorted into values of ascending order 4) **for** _i ←_ 0 to _list.Count −_ 1 5) **for** _j ←_ 0 to _list.Count −_ 1 6) **if** _list_ [ _i_ ] _< list_ [ _j_ ] 7) _Swap_ ( _list_ [ _i_ ] _, list_ [ _j_ ]) 8) **end if** 9) **end for** 10) **end for** 11) **return** _list_ 12) **end** BubbleSort 

## **8.2 Merge Sort** 

Merge sort is an algorithm that has a fairly efficient space time complexity - _O_ ( _n log n_ ) and is fairly trivial to implement. The algorithm is based on splitting a list, into two similar sized lists ( _left_ , and _right_ ) and sorting each list and then merging the sorted lists back together. 

_Note: the function MergeOrdered simply takes two ordered lists and makes them one._ 

63 

_CHAPTER 8. SORTING_ 

64 

**==> picture [435 x 218] intentionally omitted <==**

**----- Start of picture text -----**<br>
4 75 74 2 54 4 75 74 2 54 4 74 75 2 54 4 74 2 75 54 4 74 2 54 75<br>0 1 2 3 4 0 1 2 3 4 0 1 2 3 4 0 1 2 3 4 0 1 2 3 4<br>4 74 2 54 75 4 74 2 54 75 4 2 74 54 75 4 2 54 74 75<br>0 1 2 3 4 0 1 2 3 4 0 1 2 3 4 0 1 2 3 4<br>4 2 54 74 75 2 4 54 74 75 2 4 54 74 75<br>0 1 2 3 4 0 1 2 3 4 0 1 2 3 4<br>2 4 54 74 75 2 4 54 74 75<br>0 1 2 3 4 0 1 2 3 4<br>2 4 54 74 75<br>0 1 2 3 4<br>**----- End of picture text -----**<br>


Figure 8.1: Bubble Sort Iterations 

1) **algorithm** Mergesort( _list_ ) 2) **Pre:** _list_ = _∅_ 3) **Post:** _list_ has been sorted into values of ascending order 4) **if** _list_ .Count = 1 // already sorted 5) **return** _list_ 6) **end if** 7) _m ← list_ .Count _/_ 2 8) _left ←_ list( _m_ ) 9) _right ←_ list( _list_ .Count _− m_ ) 10) **for** _i ←_ 0 to _left_ .Count _−_ 1 11) _left_ [ _i_ ] _←_ list[ _i_ ] 12) **end for** 13) **for** _i ←_ 0 to _right_ .Count _−_ 1 14) _right_ [ _i_ ] _←_ list[ _i_ ] 15) **end for** 16) _left ←_ Mergesort( _left_ ) 17) _right ←_ Mergesort( _right_ ) 18) **return** MergeOrdered( _left_ , _right_ ) 19) **end** Mergesort 

_CHAPTER 8. SORTING_ 

65 

**==> picture [360 x 221] intentionally omitted <==**

**----- Start of picture text -----**<br>
4<br>4 4<br>2<br>75 75<br>4<br>4<br>75<br>54<br>75<br>74<br>74<br>74 75<br>2<br>2<br>74<br>54<br>54<br>2 2<br>74<br>54 2 2<br>54 54<br>5<br>4<br>Divide Impera (Merge)<br>**----- End of picture text -----**<br>


Figure 8.2: Merge Sort Divide et Impera Approach 

## **8.3 Quick Sort** 

Quick sort is one of the most popular sorting algorithms based on divide et impera strategy, resulting in an _O_ ( _n log n_ ) complexity. The algorithm starts by picking an item, called pivot, and moving all smaller items before it, while all greater elements after it. This is the main quick sort operation, called partition, recursively repeated on lesser and greater sub lists until their size is one or zero - in which case the list is implicitly sorted. 

Choosing an appropriate pivot, as for example the median element is fundamental for avoiding the drastically reduced performance of _O_ ( _n_[2] ). 

_CHAPTER 8. SORTING_ 

66 

**==> picture [198 x 308] intentionally omitted <==**

**----- Start of picture text -----**<br>
4 75 74 2 54<br>Pivot<br>4 75 74 2 54<br>Pivot<br>4 54 74 2 75<br>Pivot<br>4 2 74 54 75<br>Pivot<br>4 2 54 74 75<br>Pivot<br>4 2 74 75<br>Pivot Pivot<br>2 4 74 75<br>Pivot Pivot<br>2 4 54 74 75<br>**----- End of picture text -----**<br>


Figure 8.3: Quick Sort Example (pivot median strategy) 

## 1) **algorithm** QuickSort( _list_ ) 

2) **Pre:** _list_ = _∅_ 3) **Post:** _list_ has been sorted into values of ascending order 4) **if** _list_ .Count = 1 // already sorted 5) **return** _list_ 6) **end if** 7) _pivot ←_ MedianValue( _list_ ) 8) **for** _i ←_ 0 to _list_ .Count _−_ 1 9) **if** _list_ [ _i_ ] = _pivot_ 10) _equal_ .Insert( _list_ [ _i_ ]) 11) **end if** 12) **if** _list_ [ _i_ ] _< pivot_ 13) _less_ .Insert( _list_ [ _i_ ]) 14) **end if** 15) **if** _list_ [ _i_ ] _> pivot_ 16) _greater_ .Insert( _list_ [ _i_ ]) 17) **end if** 18) **end for** 19) **return** Concatenate(QuickSort( _less_ ), _equal_ , QuickSort( _greater_ )) 20) **end** Quicksort 

_CHAPTER 8. SORTING_ 

67 

## **8.4 Insertion Sort** 

Insertion sort is a somewhat interesting algorithm with an expensive runtime of _O_ ( _n_[2] ). It can be best thought of as a sorting scheme similar to that of sorting a hand of playing cards, i.e. you take one card and then look at the rest with the intent of building up an ordered set of cards in your hand. 

**==> picture [342 x 132] intentionally omitted <==**

**----- Start of picture text -----**<br>
4 75 74<br>4 75 74 2 54 4 75 74 2 54 4 75 74 2 54<br>2 54<br>4 74 75 2 54 2 4 74 75 54 2 4 54 74 75<br>**----- End of picture text -----**<br>


Figure 8.4: Insertion Sort Iterations 

1) **algorithm** Insertionsort( _list_ ) 2) **Pre:** _list_ = _∅_ 3) **Post:** _list_ has been sorted into values of ascending order 4) _unsorted ←_ 1 5) **while** _unsorted < list_ .Count 6) _hold ← list_ [ _unsorted_ ] 7) _i ← unsorted −_ 1 8) **while** _i ≥_ 0 **and** _hold < list_ [ _i_ ] 9) _list_ [ _i_ + 1] _← list_ [ _i_ ] 10) _i ← i −_ 1 11) **end while** 12) _list_ [ _i_ + 1] _← hold_ 13) _unsorted ← unsorted_ + 1 14) **end while** 15) **return** _list_ 16) **end** Insertionsort 

_CHAPTER 8. SORTING_ 

68 

## **8.5 Shell Sort** 

Put simply shell sort can be thought of as a more efficient variation of insertion sort as described in _§_ 8.4, it achieves this mainly by comparing items of varying distances apart resulting in a run time complexity of _O_ ( _n log_[2] _n_ ). 

Shell sort is fairly straight forward but may seem somewhat confusing at first as it differs from other sorting algorithms in the way it selects items to compare. Figure 8.5 shows shell sort being ran on an array of integers, the red coloured square is the current value we are holding. 

- 1) **algorithm** ShellSort( _list_ ) 

2) **Pre:** _list_ = _∅_ 

3) **Post:** _list_ has been sorted into values of ascending order 4) _increment ← list_ .Count _/_ 2 5) **while** _increment_ = 0 6) _current ← increment_ 7) **while** _current < list_ .Count 8) _hold ← list_ [ _current_ ] 9) _i ← current − increment_ 10) **while** _i ≥_ 0 **and** _hold < list_ [ _i_ ] 11) _list_ [ _i_ + _increment_ ] _← list_ [ _i_ ] 12) _i−_ = _increment_ 13) **end while** 14) _list_ [ _i_ + _increment_ ] _← hold_ 15) _current ← current_ + 1 16) **end while** 17) _increment /_ = 2 18) **end while** 19) **return** _list_ 20) **end** ShellSort 

## **8.6 Radix Sort** 

Unlike the sorting algorithms described previously radix sort uses buckets to sort items, each bucket holds items with a particular property called a key. Normally a bucket is a queue, each time radix sort is performed these buckets are emptied starting the smallest key bucket to the largest. When looking at items within a list to sort we do so by isolating a specific key, e.g. in the example we are about to show we have a maximum of three keys for all items, that is the highest key we need to look at is hundreds. Because we are dealing with, in this example base 10 numbers we have at any one point 10 possible key values 0 _.._ 9 each of which has their own bucket. Before we show you this first simple version of radix sort let us clarify what we mean by isolating keys. Given the number 102 if we look at the first key, the ones then we can see we have two of them, progressing to the next key - tens we can see that the number has zero of them, finally we can see that the number has a single hundred. The number used as an example has in total three keys: 

_CHAPTER 8. SORTING_ 

69 

Figure 8.5: Shell sort 

_CHAPTER 8. SORTING_ 

70 

1. Ones 

2. Tens 

3. Hundreds 

For further clarification what if we wanted to determine how many thousands the number 102 has? Clearly there are none, but often looking at a number as final like we often do it is not so obvious so when asked the question how many thousands does 102 have you should simply pad the number with a zero in that location, e.g. 0102 here it is more obvious that the key value at the thousands location is zero. 

The last thing to identify before we actually show you a simple implementation of radix sort that works on only positive integers, and requires you to specify the maximum key size in the list is that we need a way to isolate a specific key at any one time. The solution is actually very simple, but its not often you want to isolate a key in a number so we will spell it out clearly here. A key can be accessed from any integer with the following expression: _key ←_ ( _number / keyToAccess_ ) % 10. As a simple example lets say that we want to access the tens key of the number 1290, the tens column is key 10 and so after substitution yields _key ←_ (1290 _/_ 10) % 10 = 9. The next key to look at for a number can be attained by multiplying the last key by ten working left to right in a sequential manner. The value of _key_ is used in the following algorithm to work out the index of an array of queues to enqueue the item into. 

1) **algorithm** Radix( _list_ , _maxKeySize_ ) 2) **Pre:** _list_ = _∅_ 3) _maxKeySize ≥_ 0 and represents the largest key size in the list 4) **Post:** _list_ has been sorted 5) _queues ←_ Queue[10] 6) _indexOfKey ←_ 1 7) **for** _i ←_ 0 **to** _maxKeySize −_ 1 8) **foreach** _item_ **in** _list_ 9) _queues_ [GetQueueIndex( _item_ , _indexOfKey_ )].Enqueue( _item_ ) 10) **end foreach** 11) _list ←_ CollapseQueues( _queues_ ) 12) ClearQueues( _queues_ ) 13) _indexOfKey ← indexOfKey ∗_ 10 14) **end for** 15) **return** _list_ 16) **end** Radix 

Figure 8.6 shows the members of _queues_ from the algorithm described above operating on the list whose members are 90 _,_ 12 _,_ 8 _,_ 791 _,_ 123 _,_ and 61, the key we are interested in for each number is highlighted. Omitted queues in Figure 8.6 mean that they contain no items. 

## **8.7 Summary** 

Throughout this chapter we have seen many different algorithms for sorting lists, some are very efficient (e.g. quick sort defined in _§_ 8.3), some are not (e.g. 

_CHAPTER 8. SORTING_ 

71 

**==> picture [336 x 196] intentionally omitted <==**

Figure 8.6: Radix sort base 10 algorithm 

bubble sort defined in _§_ 8.1). 

Selecting the correct sorting algorithm is usually denoted purely by efficiency, e.g. you would always choose merge sort over shell sort and so on. There are also other factors to look at though and these are based on the actual implementation. Some algorithms are very nicely expressed in a recursive fashion, however these algorithms ought to be pretty efficient, e.g. implementing a linear, quadratic, or slower algorithm using recursion would be a very bad idea. 

If you want to learn more about why you should be very, very careful when implementing recursive algorithms see Appendix C. 

## **Chapter 9** 

## **Numeric** 

Unless stated otherwise the alias _n_ denotes a standard 32 bit integer. 

## **9.1 Primality Test** 

A simple algorithm that determines whether or not a given integer is a prime number, e.g. 2, 5, 7, and 13 are **all** prime numbers, however 6 is not as it can be the result of the product of two numbers that are _<_ 6. 

In an attempt to slow down the inner loop the _[√] n_ is used as the upper bound. 

1) **algorithm** IsPrime( _n_ ) 2) **Post:** _n_ is determined to be a prime or not 3) **for** _i ←_ 2 **to** _n_ **do** 4) **for** _j ←_ 1 **to** _sqrt_ ( _n_ ) **do** 5) **if** _i ∗ j_ = _n_ 6) **return** false 7) **end if** 8) **end for** 9) **end for** 10) **end** IsPrime 

## **9.2 Base conversions** 

DSA contains a number of algorithms that convert a base 10 number to its equivalent binary, octal or hexadecimal form. For example 7810 has a binary representation of 10011102. 

Table 9.1 shows the algorithm trace when the number to convert to binary is 74210. 

72 

_CHAPTER 9. NUMERIC_ 

73 

- 1) **algorithm** ToBinary( _n_ ) 

- 2) **Pre:** _n ≥_ 0 3) **Post:** _n_ has been converted into its base 2 representation 

- 4) **while** _n >_ 0 5) _list.Add_ ( _n_ % 2) 6) _n ← n/_ 2 7) **end while** 

- 8) **return** Reverse( _list_ ) 

9) **end** ToBinary 

|_n_|_list_|
|---|---|
|742|_{_ 0 _}_|
|371|_{_ 0_,_1 _}_|
|185|_{_ 0_,_1_,_1 _}_|
|92|_{_ 0_,_1_,_1_,_0 _}_|
|46|_{_ 0_,_1_,_1_,_0_,_1 _}_|
|23|_{_ 0_,_1_,_1_,_0_,_1_,_1 _}_|
|11|_{_ 0_,_1_,_1_,_0_,_1_,_1_,_1 _}_|
|5|_{_ 0_,_1_,_1_,_0_,_1_,_1_,_1_,_1 _}_|
|2|_{_ 0_,_1_,_1_,_0_,_1_,_1_,_1_,_1_,_0 _}_|
|1|_{_ 0_,_1_,_1_,_0_,_1_,_1_,_1_,_1_,_0_,_1 _}_|



Table 9.1: Algorithm trace of ToBinary 

## **9.3 Attaining the greatest common denominator of two numbers** 

A fairly routine problem in mathematics is that of finding the greatest common denominator of two integers, what we are essentially after is the greatest number which is a multiple of both, e.g. the greatest common denominator of 9, and 15 is 3. One of the most elegant solutions to this problem is based on Euclid’s algorithm that has a run time complexity of _O_ ( _n_[2] ). 

- 1) **algorithm** GreatestCommonDenominator( _m_ , _n_ ) 

- 2) **Pre:** _m_ and _n_ are integers 

- 3) **Post:** the greatest common denominator of the two integers is calculated 4) **if** _n_ = 0 

- 5) **return** _m_ 

- 6) **end if** 

- 7) **return** GreatestCommonDenominator( _n_ , _m_ % _n_ ) 

- 8) **end** GreatestCommonDenominator 

_CHAPTER 9. NUMERIC_ 

74 

## **9.4 Computing the maximum value for a number of a specific base consisting of N digits** 

This algorithm computes the maximum value of a number for a given number of digits, e.g. using the base 10 system the maximum number we can have made up of 4 digits is the number 999910. Similarly the maximum number that consists of 4 digits for a base 2 number is 11112 which is 1510. 

The expression by which we can compute this maximum value for _N_ digits is: _B[N] −_ 1. In the previous expression _B_ is the number base, and _N_ is the number of digits. As an example if we wanted to determine the maximum value for a hexadecimal number (base 16) consisting of 6 digits the expression would be as follows: 16[6] _−_ 1. The maximum value of the previous example would be represented as _FFFFFF_ 16 which yields 1677721510. 

In the following algorithm _numberBase_ should be considered restricted to the values of 2, 8, 9, and 16. For this reason in our actual implementation _numberBase_ has an enumeration type. The _Base_ enumeration type is defined as: 

## _Base_ = _{Binary ←_ 2 _, Octal ←_ 8 _, Decimal ←_ 10 _, Hexadecimal ←_ 16 _}_ 

The reason we provide the definition of _Base_ is to give you an idea how this algorithm can be modelled in a more readable manner rather than using various checks to determine the correct base to use. For our implementation we cast the value of _numberBase_ to an integer, as such we extract the value associated with the relevant option in the _Base_ enumeration. As an example if we were to cast the option _Octal_ to an integer we would get the value 8. In the algorithm listed below the cast is implicit so we just use the actual argument _numberBase_ . 

## 1) **algorithm** MaxValue( _numberBase_ , _n_ ) 

- 2) **Pre:** _numberBase_ is the number system to use, _n_ is the number of digits 

- 3) **Post:** the maximum value for _numberBase_ consisting of _n_ digits is computed 4) **return** Power( _numberBase, n_ ) _−_ 1 

- 5) **end** MaxValue 

## **9.5 Factorial of a number** 

Attaining the factorial of a number is a primitive mathematical operation. Many implementations of the factorial algorithm are recursive as the problem is recursive in nature, however here we present an iterative solution. The iterative solution is presented because it too is trivial to implement and doesn’t suffer from the use of recursion (for more on recursion see _§_ C). 

The factorial of 0 and 1 is 0. The aforementioned acts as a base case that we will build upon. The factorial of 2 is 2 _∗_ the factorial of 1, similarly the factorial of 3 is 3 _∗_ the factorial of 2 and so on. We can indicate that we are after the factorial of a number using the form _N_ ! where _N_ is the number we wish to attain the factorial of. Our algorithm doesn’t use such notation but it is handy to know. 

_CHAPTER 9. NUMERIC_ 

75 

1) **algorithm** Factorial( _n_ ) 

2) **Pre:** _n ≥_ 0, _n_ is the number to compute the factorial of 3) **Post:** the factorial of _n_ is computed 4) **if** _n <_ 2 5) **return** 1 6) **end if** 7) _factorial ←_ 1 8) **for** _i ←_ 2 **to** _n_ 9) _factorial ← factorial ∗ i_ 10) **end for** 11) **return** _factorial_ 12) **end** Factorial 

## **9.6 Summary** 

In this chapter we have presented several numeric algorithms, most of which are simply here because they were fun to design. Perhaps the message that the reader should gain from this chapter is that algorithms can be applied to several domains to make work in that respective domain attainable. Numeric algorithms in particular drive some of the most advanced systems on the planet computing such data as weather forecasts. 

## **Chapter 10** 

## **Searching** 

## **10.1 Sequential Search** 

A simple algorithm that search for a specific item inside a list. It operates looping on each element _O_ ( _n_ ) until a match occurs or the end is reached. 

1) **algorithm** SequentialSearch( _list_ , _item_ ) 2) **Pre:** _list_ = _∅_ 3) **Post:** return _index_ of item if found, otherwise _−_ 1 

- 4) _index ←_ 0 5) **while** _index < list_ .Count **and** _list_ [ _index_ ] = _item_ 6) _index ← index_ + 1 

7) **end while** 8) **if** _index < list_ .Count **and** _list_ [ _index_ ] = _item_ 9) **return** _index_ 10) **end if** 11) **return** _−_ 1 12) **end** SequentialSearch 

## **10.2 Probability Search** 

Probability search is a statistical sequential searching algorithm. In addition to searching for an item, it takes into account its frequency by swapping it with it’s predecessor in the list. The algorithm complexity still remains at _O_ ( _n_ ) but in a non-uniform items search the more frequent items are in the first positions, reducing list scanning time. 

Figure 10.1 shows the resulting state of a list after searching for two items, notice how the searched items have had their search probability increased after each search operation respectively. 

76 

_CHAPTER 10. SEARCHING_ 

77 

**==> picture [172 x 226] intentionally omitted <==**

Figure 10.1: a) Search(12), b) Search(101) 

## 1) **algorithm** ProbabilitySearch( _list_ , _item_ ) 

2) **Pre:** _list_ = _∅_ 3) **Post:** a boolean indicating where the item is found or not; in the former case swap founded item with its predecessor 

4) _index ←_ 0 5) **while** _index < list_ .Count **and** _list_ [ _index_ ] = _item_ 6) _index ← index_ + 1 7) **end while** 8) **if** _index ≥ list_ .Count **or** _list_ [ _index_ ] = _item_ 9) **return** false 10) **end if** 11) **if** _index >_ 0 12) _Swap_ ( _list_ [ _index_ ] _, list_ [ _index −_ 1]) 13) **end if** 14) **return** true 15) **end** ProbabilitySearch 

## **10.3 Summary** 

In this chapter we have presented a few novel searching algorithms. We have presented more efficient searching algorithms earlier on, like for instance the logarithmic searching algorithm that AVL and BST tree’s use (defined in _§_ 3.2). We decided not to cover a searching algorithm known as binary chop (another name for binary search, binary chop usually refers to its array counterpart) as 

_CHAPTER 10. SEARCHING_ 

78 

the reader has already seen such an algorithm in _§_ 3. 

Searching algorithms and their efficiency largely depends on the underlying data structure being used to store the data. For instance it is quicker to determine whether an item is in a hash table than it is an array, similarly it is quicker to search a BST than it is a linked list. If you are going to search for data fairly often then we strongly advise that you sit down and research the data structures available to you. In most cases using a list or any other primarily linear data structure is down to lack of knowledge. Model your data and then research the data structures that best fit your scenario. 

## **Chapter 11** 

## **Strings** 

Strings have their own chapter in this text purely because string operations and transformations are incredibly frequent within programs. The algorithms presented are based on problems the authors have come across previously, or were formulated to satisfy curiosity. 

## **11.1 Reversing the order of words in a sentence** 

Defining algorithms for primitive string operations is simple, e.g. extracting a sub-string of a string, however some algorithms that require more inventiveness can be a little more tricky. 

The algorithm presented here does not simply reverse the characters in a string, rather it reverses the order of words within a string. This algorithm works on the principal that words are all delimited by white space, and using a few markers to define where words start and end we can easily reverse them. 

79 

_CHAPTER 11. STRINGS_ 

80 

1) **algorithm** ReverseWords( _value_ ) 2) **Pre:** _value_ = _∅_ , _sb_ is a string buffer 3) **Post:** the words in _value_ have been reversed 4) _last ← value_ .Length _−_ 1 5) _start ← last_ 6) **while** _last ≥_ 0 7) // skip whitespace 8) **while** _start ≥_ 0 **and** _value_ [ _start_ ] = whitespace 9) _start ← start −_ 1 10) **end while** 11) _last ← start_ 12) // march down to the index before the beginning of the word 13) **while** _start ≥_ 0 **and** _start_ = whitespace 14) _start ← start −_ 1 15) **end while** 16) // append chars from _start_ + 1 to _length_ + 1 to string buffer sb 17) **for** _i ← start_ + 1 **to** _last_ 18) _sb_ .Append( _value_ [ _i_ ]) 19) **end for** 20) // if this isn’t the last word in the string add some whitespace after the word in the buffer 21) **if** _start >_ 0 22) _sb_ .Append(‘ ’) 23) **end if** 24) _last ← start −_ 1 25) _start ← last_ 26) **end while** 27) // check if we have added one too many whitespace to _sb_ 28) **if** _sb_ [ _sb_ .Length _−_ 1] = whitespace 29) // cut the whitespace 30) _sb_ .Length _← sb_ .Length _−_ 1 31) **end if** 32) **return** _sb_ 33) **end** ReverseWords 

## **11.2 Detecting a palindrome** 

Although not a frequent algorithm that will be applied in real-life scenarios detecting a palindrome is a fun, and as it turns out pretty trivial algorithm to design. 

The algorithm that we present has a _O_ ( _n_ ) run time complexity. Our algorithm uses two pointers at opposite ends of string we are checking is a palindrome or not. These pointers march in towards each other always checking that each character they point to is the same with respect to value. Figure 11.1 shows the _IsPalindrome_ algorithm in operation on the string “Was it Eliot’s toilet I saw?” If you remove all punctuation, and white space from the aforementioned string you will find that it is a valid palindrome. 

_CHAPTER 11. STRINGS_ 

81 

Figure 11.1: _left_ and _right_ pointers marching in towards one another 

- 1) **algorithm** IsPalindrome( _value_ ) 

2) **Pre:** _value_ = _∅_ 3) **Post:** _value_ is determined to be a palindrome or not 4) _word ← value_ .Strip().ToUpperCase() 5) _left ←_ 0 6) _right ← word_ .Length _−_ 1 7) **while** _word_ [ _left_ ] = _word_ [ _right_ ] **and** _left < right_ 8) _left ← left_ + 1 9) _right ← right −_ 1 10) **end while** 11) **return** _word_ [ _left_ ] = _word_ [ _right_ ] 12) **end** IsPalindrome 

In the _IsPalindrome_ algorithm we call a method by the name of _Strip_ . This algorithm discards punctuation in the string, including white space. As a result _word_ contains a heavily compacted representation of the original string, each character of which is in its uppercase representation. 

Palindromes discard white space, punctuation, and case making these changes allows us to design a simple algorithm while making our algorithm fairly robust with respect to the palindromes it will detect. 

## **11.3 Counting the number of words in a string** 

Counting the number of words in a string can seem pretty trivial at first, however there are a few cases that we need to be aware of: 

1. tracking when we are in a string 

2. updating the word count at the correct place 

3. skipping white space that delimits the words 

As an example consider the string “Ben ate hay” Clearly this string contains three words, each of which distinguished via white space. All of the previously listed points can be managed by using three variables: 

1. _index_ 

2. _wordCount_ 

3. _inWord_ 

_CHAPTER 11. STRINGS_ 

82 

Figure 11.2: String with three words 

Figure 11.3: String with varying number of white space delimiting the words 

Of the previously listed _index_ keeps track of the current index we are at in the string, _wordCount_ is an integer that keeps track of the number of words we have encountered, and finally _inWord_ is a Boolean flag that denotes whether or not at the present time we are within a word. If we are not currently hitting white space we are in a word, the opposite is true if at the present index we are hitting white space. 

What denotes a word? In our algorithm each word is separated by one or more occurrences of white space. We don’t take into account any particular splitting symbols you may use, e.g. in .NET _String.Split_[1] can take a char (or array of characters) that determines a delimiter to use to split the characters within the string into chunks of strings, resulting in an array of sub-strings. 

In Figure 11.2 we present a string indexed as an array. Typically the pattern is the same for most words, delimited by a single occurrence of white space. Figure 11.3 shows the same string, with the same number of words but with varying white space splitting them. 

> 1http://msdn.microsoft.com/en-us/library/system.string.split.aspx 

_CHAPTER 11. STRINGS_ 

83 

1) **algorithm** WordCount( _value_ ) 2) **Pre:** _value_ = _∅_ 3) **Post:** the number of words contained within _value_ is determined 4) _inWord ← true_ 5) _wordCount ←_ 0 6) _index ←_ 0 7) // skip initial white space 8) **while** _value_ [ _index_ ] = whitespace **and** _index < value_ .Length _−_ 1 9) _index ← index_ + 1 10) **end while** 11) // was the string just whitespace? 12) **if** _index_ = _value_ .Length **and** _value_ [ _index_ ] = whitespace 13) **return** 0 14) **end if** 15) **while** _index < value_ .Length 16) **if** _value_ [ _index_ ] = whitespace 17) // skip all whitespace 18) **while** _value_ [ _index_ ] = whitespace **and** _index < value_ .Length _−_ 1 19) _index ← index_ + 1 20) **end while** 21) _inWord ← false_ 22) _wordCount ← wordCount_ + 1 23) **else** 24) _inWord ← true_ 25) **end if** 26) _index ← index_ + 1 27) **end while** 28) // last word may have not been followed by whitespace 29) **if** _inWord_ 30) _wordCount ← wordCount_ + 1 31) **end if** 32) **return** _wordCount_ 33) **end** WordCount 

## **11.4 Determining the number of repeated words within a string** 

With the help of an unordered set, and an algorithm that can split the words within a string using a specified delimiter this algorithm is straightforward to implement. If we split all the words using a single occurrence of white space as our delimiter we get all the words within the string back as elements of an array. Then if we iterate through these words adding them to a set which contains only unique strings we can attain the number of unique words from the string. All that is left to do is subtract the unique word count from the total number of stings contained in the array returned from the split operation. The split operation that we refer to is the same as that mentioned in _§_ 11.3. 

_CHAPTER 11. STRINGS_ 

84 

**==> picture [370 x 152] intentionally omitted <==**

Figure 11.4: a) Undesired _uniques_ set; b) desired _uniques_ set 

- 1) **algorithm** RepeatedWordCount( _value_ ) 

2) **Pre:** _value_ = _∅_ 3) **Post:** the number of repeated words in _value_ is returned 4) _words ← value_ .Split(’ ’) 5) _uniques ←_ Set 6) **foreach** _word_ **in** _words_ 7) _uniques_ .Add( _word_ .Strip()) 8) **end foreach** 9) **return** _words_ .Length _−uniques_ .Count 10) **end** RepeatedWordCount 

You will notice in the _RepeatedWordCount_ algorithm that we use the _Strip_ method we referred to earlier in _§_ 11.1. This simply removes any punctuation from a _word_ . The reason we perform this operation on each _word_ is so that we can build a more accurate unique string collection, e.g. “test”, and “test!” are the same word minus the punctuation. Figure 11.4 shows the undesired and desired sets for the _unique_ set respectively. 

## **11.5 Determining the first matching character between two strings** 

The algorithm to determine whether any character of a string matches any of the characters in another string is pretty trivial. Put simply, we can parse the strings considered using a double loop and check, discarding punctuation, the equality between any characters thus returning a non-negative index that represents the location of the first character in the match (Figure 11.5); otherwise we return -1 if no match occurs. This approach exhibit a run time complexity of _O_ ( _n_[2] ). 

_CHAPTER 11. STRINGS_ 

85 

**==> picture [413 x 108] intentionally omitted <==**

**----- Start of picture text -----**<br>
i i i<br>Word t e s t t e s t t e s t<br>0 1 2 3 4 0 1 2 3 4 0 1 2 3 4<br>index index index<br>Match p t e r s p t e r s p t e r s<br>0 1 2 3 4 5 6 0 1 2 3 4 5 6 0 1 2 3 4 5 6<br>a) b) c)<br>**----- End of picture text -----**<br>


Figure 11.5: a) First Step; b) Second Step c) Match Occurred 

1) **algorithm** Any( _word_ , _match_ ) 2) **Pre:** _word, match_ = _∅_ 3) **Post:** _index_ representing match location if occured, _−_ 1 otherwise 4) **for** _i ←_ 0 to _word.Length −_ 1 5) **while** _word_ [ _i_ ] = whitespace 6) _i ← i_ + 1 7) **end while** 8) **for** _index ←_ 0 to _match.Length −_ 1 9) **while** _match_ [ _index_ ] = whitespace 10) _index ← index_ + 1 11) **end while** 12) **if** _match_ [ _index_ ] = _word_ [ _i_ ] 13) **return** _index_ 14) **end if** 15) **end for** 16) **end for** 17) **return** _−_ 1 18) **end** Any 

## **11.6 Summary** 

We hope that the reader has seen how fun algorithms on string data types are. Strings are probably the most common data type (and data structure - remember we are dealing with an array) that you will work with so its important that you learn to be creative with them. We for one find strings fascinating. A simple Google search on string nuances between languages and encodings will provide you with a great number of problems. Now that we have spurred you along a little with our introductory algorithms you can devise some of your own. 

## **Appendix A** 

## **Algorithm Walkthrough** 

Learning how to design good algorithms can be assisted greatly by using a structured approach to tracing its behaviour. In most cases tracing an algorithm only requires a single table. In most cases tracing is not enough, you will also want to use a diagram of the data structure your algorithm operates on. This diagram will be used to visualise the problem more effectively. Seeing things visually can help you understand the problem quicker, and better. 

The trace table will store information about the variables used in your algorithm. The values within this table are constantly updated when the algorithm mutates them. Such an approach allows you to attain a history of the various values each variable has held. You may also be able to infer patterns from the values each variable has contained so that you can make your algorithm more efficient. 

We have found this approach both simple, and powerful. By combining a visual representation of the problem as well as having a history of past values generated by the algorithm it can make understanding, and solving problems much easier. 

In this chapter we will show you how to work through both iterative, and recursive algorithms using the technique outlined. 

## **A.1 Iterative algorithms** 

We will trace the _IsPalindrome_ algorithm (defined in _§_ 11.2) as our example iterative walkthrough. Before we even look at the variables the algorithm uses, first we will look at the actual data structure the algorithm operates on. It should be pretty obvious that we are operating on a string, but how is this represented? A string is essentially a block of contiguous memory that consists of some char data types, one after the other. Each character in the string can be accessed via an index much like you would do when accessing items within an array. The picture should be presenting itself - a string can be thought of as an array of characters. 

For our example we will use _IsPalindrome_ to operate on the string “Never odd or even” Now we know how the string data structure is represented, and the value of the string we will operate on let’s go ahead and draw it as shown in Figure A.1. 

86 

_APPENDIX A. ALGORITHM WALKTHROUGH_ 

87 

Figure A.1: Visualising the data structure we are operating on 

_value word lef t right_ 

Table A.1: A column for each variable we wish to track 

The _IsPalindrome_ algorithm uses the following list of variables in some form throughout its execution: 

1. _value_ 

2. _word_ 

3. _left_ 

4. _right_ 

Having identified the values of the variables we need to keep track of we simply create a column for each in a table as shown in Table A.1. 

Now, using the _IsPalindrome_ algorithm execute each statement updating the variable values in the table appropriately. Table A.2 shows the final table values for each variable used in _IsPalindrome_ respectively. 

While this approach may look a little bloated in print, on paper it is much more compact. Where we have the strings in the table you should annotate these strings with array indexes to aid the algorithm walkthrough. 

There is one other point that we should clarify at this time - whether to include variables that change only a few times, or not at all in the trace table. In Table A.2 we have included both the _value_ , and _word_ variables because it was convenient to do so. You may find that you want to promote these values to a larger diagram (like that in Figure A.1) and only use the trace table for variables whose values change during the algorithm. We recommend that you promote the core data structure being operated on to a larger diagram outside of the table so that you can interrogate it more easily. 

|_value_|_word_|_left_|_right_|
|---|---|---|---|
|“Never odd or even”|“NEVERODDOREVEN”|0|13|
|||1|12|
|||2|11|
|||3|10|
|||4|9|
|||5|8|
|||6|7|
|||7|6|



Table A.2: Algorithm trace for _IsPalindrome_ 

_APPENDIX A. ALGORITHM WALKTHROUGH_ 

88 

We cannot stress enough how important such traces are when designing your algorithm. You can use these trace tables to verify algorithm correctness. At the cost of a simple table, and quick sketch of the data structure you are operating on you can devise correct algorithms quicker. Visualising the problem domain and keeping track of changing data makes problems a lot easier to solve. Moreover you always have a point of reference which you can look back on. 

## **A.2 Recursive Algorithms** 

For the most part working through recursive algorithms is as simple as walking through an iterative algorithm. One of the things that we need to keep track of though is which method call returns to who. Most recursive algorithms are much simple to follow when you draw out the recursive calls rather than using a table based approach. In this section we will use a recursive implementation of an algorithm that computes a number from the Fiboncacci sequence. 

- 1) **algorithm** Fibonacci( _n_ ) 

- 2) **Pre:** _n_ is the number in the fibonacci sequence to compute 

- 3) **Post:** the fibonacci sequence number _n_ has been computed 4) **if** _n <_ 1 

5) **return** 0 

6) **else if** _n <_ 2 7) **return** 1 

- 8) **end if** 

9) **return** Fibonacci( _n −_ 1) + Fibonacci( _n −_ 2) 10) **end** Fibonacci 

Before we jump into showing you a diagrammtic representation of the algorithm calls for the _Fibonacci_ algorithm we will briefly talk about the cases of the algorithm. The algorithm has three cases in total: 

1. _n <_ 1 

2. _n <_ 2 

3. _n ≥_ 2 

The first two items in the preceeding list are the base cases of the algorithm. Until we hit one of our base cases in our recursive method call tree we won’t return anything. The third item from the list is our recursive case. 

With each call to the recursive case we etch ever closer to one of our base cases. Figure A.2 shows a diagrammtic representation of the recursive call chain. In Figure A.2 the order in which the methods are called are labelled. Figure A.3 shows the call chain annotated with the return values of each method call as well as the order in which methods return to their callers. In Figure A.3 the return values are represented as annotations to the red arrows. 

It is important to note that each recursive call only ever returns to its caller upon hitting one of the two base cases. When you do eventually hit a base case that branch of recursive calls ceases. Upon hitting a base case you go back to 

_APPENDIX A. ALGORITHM WALKTHROUGH_ 

89 

**==> picture [334 x 116] intentionally omitted <==**

Figure A.2: Call chain for _Fibonacci_ algorithm 

**==> picture [333 x 130] intentionally omitted <==**

Figure A.3: Return chain for _Fibonacci_ algorithm 

_APPENDIX A. ALGORITHM WALKTHROUGH_ 

90 

the caller and continue execution of that method. Execution in the caller is contiued at the next statement, or expression after the recursive call was made. 

In the _Fibonacci_ algorithms’ recursive case we make two recursive calls. When the first recursive call (Fibonacci( _n −_ 1)) returns to the caller we then execute the the second recursive call (Fibonacci( _n −_ 2)). After both recursive calls have returned to their caller, the caller can then subesequently return to its caller and so on. 

Recursive algorithms are much easier to demonstrate diagrammatically as Figure A.2 demonstrates. When you come across a recursive algorithm draw method call diagrams to understand how the algorithm works at a high level. 

## **A.3 Summary** 

Understanding algorithms can be hard at times, particularly from an implementation perspective. In order to understand an algorithm try and work through it using trace tables. In cases where the algorithm is also recursive sketch the recursive calls out so you can visualise the call/return chain. 

In the vast majority of cases implementing an algorithm is simple provided that you know how the algorithm works. Mastering how an algorithm works from a high level is key for devising a well designed solution to the problem in hand. 

## **Appendix B** 

## **Translation Walkthrough** 

The conversion from pseudo to an actual imperative language is usually very straight forward, to clarify an example is provided. In this example we will convert the algorithm in _§_ 9.1 to the C# language. 

1) public static bool IsPrime(int number) 

2) _{_ 3) if (number _<_ 2) 4) _{_ 5) return false; 6) _}_ 7) int innerLoopBound = (int)Math.Floor(Math.Sqrt(number)); 8) for (int i = 1; i _<_ number; i++) 9) _{_ 10) for(int j = 1; j _<_ = innerLoopBound; j++) 11) _{_ 12) if (i _∗_ j == number) 13) _{_ 14) return false; 15) _}_ 16) _}_ 17) _}_ 18) return true; 19) _}_ 

For the most part the conversion is a straight forward process, however you may have to inject various calls to other utility algorithms to ascertain the correct result. 

A consideration to take note of is that many algorithms have fairly strict preconditions, of which there may be several - in these scenarios you will need to inject the correct code to handle such situations to preserve the correctness of the algorithm. Most of the preconditions can be suitably handled by throwing the correct exception. 

91 

_APPENDIX B. TRANSLATION WALKTHROUGH_ 

92 

## **B.1 Summary** 

As you can see from the example used in this chapter we have tried to make the translation of our pseudo code algorithms to mainstream imperative languages as simple as possible. 

Whenever you encounter a keyword within our pseudo code examples that you are unfamiliar with just browse to Appendix E which descirbes each keyword. 

## **Appendix C Recursive Vs. Iterative Solutions** 

One of the most succinct properties of modern programming languages like C++, C#, and Java (as well as many others) is that these languages allow you to define methods that reference themselves, such methods are said to be recursive. One of the biggest advantages recursive methods bring to the table is that they usually result in more readable, and compact solutions to problems. 

A recursive method then is one that is defined in terms of itself. Generally a recursive algorithms has two main properties: 

1. One or more base cases; and 

2. A recursive case 

For now we will briefly cover these two aspects of recursive algorithms. With each recursive call we should be making progress to our base case otherwise we are going to run into trouble. The trouble we speak of manifests itself typically as a stack overflow, we will describe why later. 

Now that we have briefly described what a recursive algorithm is and why you might want to use such an approach for your algorithms we will now talk about iterative solutions. An iterative solution uses no recursion whatsoever. An iterative solution relies only on the use of loops (e.g. for, while, do-while, etc). The down side to iterative algorithms is that they tend not to be as clear as to their recursive counterparts with respect to their operation. The major advantage of iterative solutions is speed. Most production software you will find uses little or no recursive algorithms whatsoever. The latter property can sometimes be a companies prerequisite to checking in code, e.g. upon checking in a static analysis tool may verify that the code the developer is checking in contains no recursive algorithms. Normally it is systems level code that has this zero tolerance policy for recursive algorithms. 

Using recursion should always be reserved for fast algorithms, you should avoid it for the following algorithm run time deficiencies: 

1. _O_ ( _n_[2] ) 

2. _O_ ( _n_[3] ) 

93 

_APPENDIX C. RECURSIVE VS. ITERATIVE SOLUTIONS_ 

94 

## 3. _O_ (2 _[n]_ ) 

If you use recursion for algorithms with any of the above run time efficiency’s you are inviting trouble. The growth rate of these algorithms is high and in most cases such algorithms will lean very heavily on techniques like divide and conquer. While constantly splitting problems into smaller problems is good practice, in these cases you are going to be spawning a lot of method calls. All this overhead (method calls don’t come _that_ cheap) will soon pile up and either cause your algorithm to run a lot slower than expected, or worse, you will run out of stack space. When you exceed the allotted stack space for a thread the process will be shutdown by the operating system. This is the case irrespective of the platform you use, e.g. .NET, or native C++ etc. You can ask for a bigger stack size, but you typically only want to do this if you have a very good reason to do so. 

## **C.1 Activation Records** 

An activation record is created every time you invoke a method. Put simply an activation record is something that is put on the stack to support method invocation. Activation records take a small amount of time to create, and are pretty lightweight. 

Normally an activation record for a method call is as follows (this is very general): 

- The actual parameters of the method are pushed onto the stack 

- The return address is pushed onto the stack 

- The top-of-stack index is incremented by the total amount of memory required by the local variables within the method 

- A jump is made to the method 

In many recursive algorithms operating on large data structures, or algorithms that are inefficient you will run out of stack space quickly. Consider an algorithm that when invoked given a specific value it creates many recursive calls. In such a case a big chunk of the stack will be consumed. We will have to wait until the activation records start to be unwound after the nested methods in the call chain exit and return to their respective caller. When a method exits it’s activation record is unwound. Unwinding an activation record results in several steps: 

1. The top-of-stack index is decremented by the total amount of memory consumed by the method 

2. The return address is popped off the stack 

3. The top-of-stack index is decremented by the total amount of memory consumed by the actual parameters 

_APPENDIX C. RECURSIVE VS. ITERATIVE SOLUTIONS_ 

95 

While activation records are an efficient way to support method calls they can build up very quickly. Recursive algorithms can exhaust the stack size allocated to the thread fairly fast given the chance. 

Just about now we should be dusting the cobwebs off the age old example of an iterative vs. recursive solution in the form of the Fibonacci algorithm. This is a famous example as it highlights both the beauty and pitfalls of a recursive algorithm. The iterative solution is not as pretty, nor self documenting but it does the job a lot quicker. If we were to give the Fibonacci algorithm an input of say 60 then we would have to wait a while to get the value back because it has an _O_ ( _g[n]_ ) run time. The iterative version on the other hand has a _O_ ( _n_ ) run time. Don’t let this put you off recursion. This example is mainly used to shock programmers into thinking about the ramifications of recursion rather than warning them off. 

## **C.2 Some problems are recursive in nature** 

Something that you may come across is that some data structures and algorithms are actually recursive in nature. A perfect example of this is a tree data structure. A common tree node usually contains a value, along with two pointers to two other nodes of the same node type. As you can see tree is recursive in its makeup wit each node possibly pointing to two other nodes. 

When using recursive algorithms on tree’s it makes sense as you are simply adhering to the inherent design of the data structure you are operating on. Of course it is not all good news, after all we are still bound by the limitations we have mentioned previously in this chapter. 

We can also look at sorting algorithms like merge sort, and quick sort. Both of these algorithms are recursive in their design and so it makes sense to model them recursively. 

## **C.3 Summary** 

Recursion is a powerful tool, and one that all programmers should know of. Often software projects will take a trade between readability, and efficiency in which case recursion is great provided you don’t go and use it to implement an algorithm with a quadratic run time or higher. Of course this is not a rule of thumb, this is just us throwing caution to the wind. Defensive coding will always prevail. 

Many times recursion has a natural home in recursive data structures and algorithms which are recursive in nature. Using recursion in such scenarios is perfectly acceptable. Using recursion for something like linked list traversal is a little overkill. Its iterative counterpart is probably less lines of code than its recursive counterpart. 

Because we can only talk about the implications of using recursion from an abstract point of view you should consult your compiler and run time environment for more details. It may be the case that your compiler recognises things like tail recursion and can optimise them. This isn’t unheard of, in fact most commercial compilers will do this. The amount of optimisation compilers can 

_APPENDIX C. RECURSIVE VS. ITERATIVE SOLUTIONS_ 

96 

do though is somewhat limited by the fact that you are still using recursion. You, as the developer have to accept certain accountability’s for performance. 

## **Appendix D** 

## **Testing** 

Testing is an essential part of software development. Testing has often been discarded by many developers in the belief that the burden of proof of their software is on those within the company who hold test centric roles. This couldn’t be further from the truth. As a developer you should at least provide a suite of unit tests that verify certain boundary conditions of your software. 

A great thing about testing is that you build up progressively a safety net. If you add or tweak algorithms and then run your suite of tests you will be quickly alerted to any cases that you have broken with your recent changes. Such a suite of tests in any sizeable project is absolutely essential to maintaining a fairly high bar when it comes to quality. Of course in order to attain such a standard you need to think carefully about the tests that you construct. 

Unit testing which will be the subject of the vast majority of this chapter are widely available on most platforms. Most modern languages like C++, C#, and Java offer an impressive catalogue of testing frameworks that you can use for unit testing. 

The following list identifies testing frameworks which are popular: 

JUnit: Targeted at Jav., `http://www.junit.org/` 

NUnit: Can be used with languages that target Microsoft’s Common Language Runtime. `http://www.nunit.org/index.php` 

Boost Test Library: Targeted at C++. The test library that ships with the incredibly popular Boost libraries. `http://www.boost.org` . A direct link to the libraries documentation `http://www.boost.org/doc/libs/1_36_0/libs/test/doc/ html/index.html` 

CppUnit: Targeted at C++. `http://cppunit.sourceforge.net/` 

Don’t worry if you think that the list is very sparse, there are far more on offer than those that we have listed. The ones listed are the testing frameworks that we believe are the most popular for C++, C#, and Java. 

## **D.1 What constitutes a unit test?** 

A unit test should focus on a single atomic property of the subject being tested. Do not try and test many things at once, this will result in a suite of somewhat 

97 

_APPENDIX D. TESTING_ 

98 

unstructured tests. As an example if you were wanting to write a test that verified that a particular value _V_ is returned from a specific input _I_ then your test should do the smallest amount of work possible to verify that _V_ is correct given _I_ . A unit test should be simple and self describing. 

As well as a unit test being relatively atomic you should also make sure that your unit tests execute quickly. If you can imagine in the future when you may have a test suite consisting of thousands of tests you want those tests to execute as quickly as possible. Failure to attain such a goal will most likely result in the suite of tests not being ran that often by the developers on your team. This can occur for a number of reasons but the main one would be that it becomes incredibly tedious waiting several minutes to run tests on a developers local machine. 

Building up a test suite can help greatly in a team scenario, particularly when using a continuous build server. In such a scenario you can have the suite of tests devised by the developers and testers ran as part of the build process. 

Employing such strategies can help you catch niggling little error cases early rather than via your customer base. There is nothing more embarrassing for a developer than to have a very trivial bug in their code reported to them from a customer. 

## **D.2 When should I write my tests?** 

A source of great debate would be an understatement to personify such a question as this. In recent years a test driven approach to development has become very popular. Such an approach is known as test driven development, or more commonly the acronym TDD. 

One of the founding principles of TDD is to write the unit test first, watch it fail and then make it pass. The premise being that you only ever write enough code at any one time to satisfy the state based assertions made in a unit test. We have found this approach to provide a more structured intent to the implementation of algorithms. At any one stage you only have a single goal, to make the failing test pass. Because TDD makes you write the tests up front you never find yourself in a situation where you forget, or can’t be bothered to write tests for your code. This is often the case when you write your tests after you have coded up your implementation. We, as the authors of this book ourselves use TDD as our preferred method. 

As we have already mentioned that TDD is our favoured approach to testing it would be somewhat of an injustice to not list, and describe the mantra that is often associate with it: 

Red: Signifies that the test has failed. 

Green: The failing test now passes. 

Refactor: Can we restructure our program so it makes more sense, and easier to maintain? 

The first point of the above list always occurs at least once (more if you count the build error) in TDD initially. Your task at this stage is solely to make the test pass, that is to make the respective test green. The last item is based around 

_APPENDIX D. TESTING_ 

99 

the restructuring of your program to make it as readable and maintainable as possible. The last point is very important as TDD is a progressive methodology to building a solution. If you adhere to progressive revisions of your algorithm restructuring when appropriate you will find that using TDD you can implement very cleanly structured types and so on. 

## **D.3 How seriously should I view my test suite?** 

Your tests are a major part of your project ecosystem and so they should be treated with the same amount of respect as your production code. This ranges from correct, and clean code formatting, to the testing code being stored within a source control repository. 

Employing a methodology like TDD, or testing after implementing you will find that you spend a great amount of time writing tests and thus they should be treated no differently to your production code. All tests should be clearly named, and fully documented as to their intent. 

## **D.4 The three A’s** 

Now that you have a sense of the importance of your test suite you will inevitably want to know how to actually structure each block of imperatives within a single unit test. A popular approach - the three A’s is described in the following list: 

Assemble: Create the objects you require in order to perform the state based assertions. 

Act: Invoke the respective operations on the objects you have assembled to mutate the state to that desired for your assertions. 

Assert: Specify what you expect to hold after the previous two steps. 

The following example shows a simple test method that employs the three A’s: 

public void MyTest() _{_ 

// assemble Type t = new Type(); // act t.MethodA(); // assert Assert.IsTrue(t.BoolExpr) 

_}_ 

## **D.5 The structuring of tests** 

Structuring tests can be viewed upon as being the same as structuring production code, e.g. all unit tests for a _Person_ type may be contained within 

_APPENDIX D. TESTING_ 

100 

a _PersonTest_ type. Typically all tests are abstracted from production code. That is that the tests are disjoint from the production code, you may have two dynamic link libraries (dll); the first containing the production code, the second containing your test code. 

We can also use things like inheritance etc when defining classes of tests. The point being that the test code is very much like your production code and you should apply the same amount of thought to its structure as you would do the production code. 

## **D.6 Code Coverage** 

Something that you can get as a product of unit testing are code coverage statistics. Code coverage is merely an indicator as to the portions of production code that your units tests cover. Using TDD it is likely that your code coverage will be very high, although it will vary depending on how easy it is to use TDD within your project. 

## **D.7 Summary** 

Testing is key to the creation of a moderately stable product. Moreover unit testing can be used to create a safety blanket when adding and removing features providing an early warning for breaking changes within your production code. 

## **Appendix E** 

## **Symbol Definitions** 

Throughout the pseudocode listings you will find several symbols used, describes the meaning of each of those symbols. 

|**Symbol**|**Description**|
|---|---|
|_←_|Assignment.|
|=|Equality.|
|_≤_|Less than or equal to.|
|_<_|Less than.*|
|_≥_|Greater than or equal to.|
|_>_|Greater than.*|
|=|Inequality.|
|_∅_|Null.|
|**and**|Logical and.|
|**or**|Logical or.|
|whitespace|Single occurrence of whitespace.|
|**yield**|Like **return** but builds a sequence.|



Table E.1: Pseudo symbol definitions 

* This symbol has a direct translation with the vast majority of imperative counterparts. 

101 

