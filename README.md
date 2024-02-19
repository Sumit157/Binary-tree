# Binary Search Tree (BST) Creation and Operations

## Overview

This C program implements a Binary Search Tree (BST) and provides functionality for creating, searching, and traversing the tree using various methods. A binary search tree is a hierarchical data structure where each node has at most two children, and the left child contains values less than the node, while the right child contains values greater than the node.

## Features

1. **Create BST (`create_bst`):**
   - Accepts user input to determine the number of nodes to create.
   - Dynamically allocates memory for each node and builds the binary search tree.

2. **Tree Traversal:**
   - **In-order (`inorder`):** Displays the values in ascending order.
   - **Pre-order (`preorder`):** Displays the root node first, followed by the left and right subtrees.
   - **Post-order (`postorder`):** Displays the left and right subtrees first, followed by the root node.

3. **Search (`search`):**
   - Allows the user to input a value to search within the BST.
   - Returns whether the value is found or not.

4. **Menu-Driven Interface (`main`):**
   - Provides a simple interactive menu for the user with options to create, search, and traverse the BST.
   - Allows the user to exit the program.

## Usage

1. **Creating a BST:**
   - Choose option 1 to create a BST.
   - Enter the number of nodes to create and input the data for each node.

2. **Searching in BST:**
   - Choose option 2 to search for a specific node in the BST.
   - Enter the value to be searched, and the program will indicate whether it's found or not.

3. **Traversing BST:**
   - Choose options 3, 4, or 5 to display the BST in in-order, pre-order, or post-order, respectively.

4. **Exiting the Program:**
   - Choose option 6 to exit the program.

## Instructions

1. Compile the program using a C compiler (e.g., GCC).
2. Run the executable and follow the on-screen menu.

## Note

- Ensure correct input values to avoid unexpected behavior.

Feel free to explore, modify, and enhance the code for educational purposes or specific use cases.
