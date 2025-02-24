#include <iostream>

//--------------------------------------------
// BTS and functions
//--------------------------------------------

// Binary search node defition
template <typename T>
class BTSNode
{
public:
    T value;
    BTSNode* parent;
    BTSNode* leftNode;
    BTSNode* rightNode;

    BTSNode(T value, BTSNode* parent = nullptr)
    {
        this->value = value;
        this->parent = parent;
    }
};

// Search for value in tree
template <typename T>
BTSNode<T>* find(BTSNode<T>* node, T value)
{
    // Fail to find
    if (node == nullptr)
        return nullptr;

    // Find
    if (value == node->value)
        return node;

    // Left
    if (value < node->value)
        return find(node->leftNode, value);

    // Right
    return find(node->rightNode, value);
}

// Insert value to tree
template <typename T>
void add(BTSNode<T>* node, T value)
{
    // Fail
    if (node == nullptr)
        return;

    // Left
    if (value < node->value)
    {
        if (node->leftNode == nullptr)
            node->leftNode = new BTSNode<T>(value, node); // Add
        else
            add(node->leftNode, value); // Iterate to left

        return;
    }

    // Right
    if (value > node->value)
    {
        if (node->rightNode == nullptr)
            node->rightNode = new BTSNode<T>(value, node); // Add
        else
            add(node->rightNode, value); // Iterate to left
    }
}

//--------------------------------------------
// Debug
//--------------------------------------------

template <typename T>
void printNode(BTSNode<T>* node, int isRight = -1)
{
    // Iterate
    if (node->leftNode != nullptr)
        printNode(node->leftNode, 0);
    else
        printNode(node->rightNode, 1);

    // Print
    switch (isRight)
    {
    case 0:
        std::cout << "l: " << node->value;
        break;
    case 1:
        std::cout << "r: " << node->value;
        break;
    default:
        std::cout << node->value;
        break;
    }
}

template <typename T>
void printTree(BTSNode<T>* root)
{
    std::cout << "Print tree ---------------- \n";
    printNode(root);
    std::cout << "--------------------------- \n";
}

//--------------------------------------------
// Program run
//--------------------------------------------

int main() {
    BTSNode<int>* root = new BTSNode<int>(5);
    add<int>(root, 1);
    add<int>(root, 10);
    printTree<int>(root);
    return 0;
}