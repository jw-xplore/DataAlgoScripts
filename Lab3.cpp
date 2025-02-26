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

// Return highest level node value
template <typename T>
int height(BTSNode<T>* node)
{
    // No node
    if (node == nullptr)
        return 0;

    // Calculate height
    int leftH = height(node->leftNode);
    int rightH = height(node->rightNode);

    int val = leftH;
    if (val < rightH)
        val = rightH;

    val += 1;

    return val;
}

// Return difference between height of left and right subtrees from seleted root node
// Positive = left heavy
// Negative = right heavy
// 0 = balanced
template <typename T>
int weight(BTSNode<T>* node)
{
    int leftH = height(node->leftNode);
    int rightH = height(node->rightNode);

    return leftH - rightH;
}

template <typename T> int sgn(T val)
{
    return (T(0) < val) - (val < T(0));
}

template <typename T>
void balance(BTSNode<T>* node, int parentWeight = 0)
{
    // No child
    if (node->leftNode == nullptr && node->rightNode == nullptr)
        return;

    // Check balance and children balance
    int w = weight(node);

    if (node->leftNode != nullptr)
        balance(node->leftNode, w);

    if (node->rightNode != nullptr)
        balance(node->rightNode, w);

    // No need to rebalance
    if (sgn(w) == sgn(parentWeight) && abs(w) <= 1)
        return;

    // Right rotation
    if (w > 0)
    {

    }

    // Left rotation
    if (w < 0)
    {

    }
}

//--------------------------------------------
// Debug
//--------------------------------------------

template <typename T>
void printNode(BTSNode<T>* node, int isRight = -1)
{
    if (node == nullptr)
        return;

    // Iterate
    if (node->leftNode != nullptr)
        printNode(node->leftNode, 0);
    if (node->rightNode != nullptr)
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
        std::cout << "root: " << node->value;
        break;
    }

    std::cout << "\n";
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
    add<int>(root, 2);
    //add<int>(root, 3);
    add<int>(root, 10);
    printTree<int>(root);
    std::cout << "h: " << height<int>(root) << "\n";
    std::cout << "we: " << weight<int>(root) << "\n";
    return 0;
}