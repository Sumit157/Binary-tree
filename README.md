# 1st Program:- Binary Search Tree (BST) Creation and Operations

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


# 2nd Program:- Binary Search Tree (BST) Node Counting(Countnode.c) Program.

## Overview

This C program implements a binary search tree (BST) and provides functionality for creating the tree, counting the total number of nodes, and counting the total number of leaf nodes. A binary search tree is a hierarchical data structure where each node has at most two children, and the left child contains values less than the node, while the right child contains values greater than the node.

## Features

1. **Create BST (`create_bst`):**
   - Accepts user input to determine the number of nodes to create.
   - Dynamically allocates memory for each node and builds the binary search tree.
   - Inserts each new node into the appropriate position based on its data value.

2. **Count Total Nodes (`count`):**
   - Counts the total number of nodes in the binary search tree using a recursive approach.
   - Returns the total count.

3. **Count Leaf Nodes (`countLeaf`):**
   - Counts the total number of leaf nodes (nodes with no children) in the binary search tree using a recursive approach.
   - Returns the count of leaf nodes.

4. **Menu-Driven Interface (`main`):**
   - Provides a simple interactive menu for the user with options to create the BST, count total nodes, count leaf nodes, and exit the program.

5. **Instructions:**
   - Choose option 1 to create a BST.
   - Choose option 2 to count and display the total number of nodes in the BST.
   - Choose option 3 to count and display the total number of leaf nodes in the BST.
   - Choose option 4 to exit the program.

6. **Note:**
   - The program utilizes static variables to maintain counts across recursive calls.

## Usage

1. Compile the program using a C compiler (e.g., GCC).
2. Run the executable and follow the on-screen menu.

Feel free to explore, modify, and enhance the code for educational purposes or specific use cases.

---

# 3rd Program:- Election Guide Assistant (`election_assistant.py`)

## Overview

This Python assistant provides an interactive, easy-to-follow guide to the election process, including:

- A simple voting timeline.
- Step-by-step election participation guidance.
- A personalized quick voting plan.
- Answers to common election questions.

## Run

```bash
python3 election_assistant.py
```

## Note

This tool provides general U.S.-focused guidance. Election rules vary by state and county, so always verify official details with your local election office.

---

# 4th Program:- India Election Guide Web App (`index.html`)

## Overview

A beautiful, interactive web app tailored for Indian election awareness. It helps users:

- Understand election timelines.
- Follow step-by-step voting guidance.
- Generate a personalized voting checklist.
- Browse/search common election FAQs.

## Run Locally

Open `index.html` in a browser directly, or serve the folder:

```bash
python3 -m http.server 8000
```

Then visit `http://localhost:8000`.

## Important Note

The app provides general guidance for Indian elections. Always verify exact and current rules with official Election Commission/state election resources.
