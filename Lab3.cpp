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

template <typename T> BTSNode<T>* balance(BTSNode<T>* node);

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
BTSNode<T>* add(BTSNode<T>* node, T value)
{
    // Fail
    if (node == nullptr)
        return node;

    // Left
    if (value < node->value)
    {
        if (node->leftNode == nullptr)
        {
            // Add
            node->leftNode = new BTSNode<T>(value, node);

            /*
            if (node->parent != nullptr)
                node->parent = balance<T>(node->parent);
            */
        }
        else
            node = add<T>(node->leftNode, value); // Iterate to left
    }

    // Right
    if (value > node->value)
    {
        if (node->rightNode == nullptr)
        {
            // Add
            node->rightNode = new BTSNode<T>(value, node);

            /*
            if (node->parent != nullptr)
                node->parent = balance<T>(node->parent);
            */
        }
        else
            node = add<T>(node->rightNode, value); // Iterate to left
    }

    return node;
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
BTSNode<T>* balance(BTSNode<T>* node)
{
    // No child
    if (node->leftNode == nullptr && node->rightNode == nullptr)
        return node;

    // Rebalance children
    if (node->leftNode != nullptr)
        balance(node->leftNode);

    if (node->rightNode != nullptr)
        balance(node->rightNode);

    // Check balance and children balance
    int w = weight(node);

    // No need to rebalance
    if (abs(w) <= 1)
        return node;

    // Rotation values
    BTSNode<T>* newRoot = nullptr;
    BTSNode<T>* smallest = nullptr; // left
    BTSNode<T>* largest = nullptr; // rigth

    // Left heavy
    if (w > 0)
    {
        int lw = weight(node->leftNode);

        // Right rotation (child is also left heavy)
        if (lw > 0)
        {
            newRoot = node->leftNode;
            smallest = node->leftNode->leftNode;
            largest = node;

            largest->leftNode = nullptr;
        }

        // Left-right rotation
        if (lw < 0)
        {
            newRoot = node->leftNode->rightNode;
            smallest = node->leftNode;
            largest = node;

            smallest->rightNode = nullptr;
            largest->leftNode = nullptr;
        }
    }

    // Right heavy
    if (w < 0)
    {
        int rw = weight(node->rightNode);

        // Left rotation (child is also right heavy)
        if (rw < 0)
        {
            newRoot = node->rightNode;
            smallest = node;
            largest = node->rightNode->rightNode;

            smallest->rightNode = nullptr;
        }

        // Right-left rotation
        if (rw > 0)
        {
            newRoot = node->rightNode->leftNode;
            smallest = node;
            largest = node->rightNode;

            smallest->rightNode = nullptr;
            largest->leftNode = nullptr;
        }
    }

    // Apply rotation
    newRoot->parent = node->parent;
    largest->parent = newRoot;
    smallest->parent = newRoot;

    node = newRoot;
    node->leftNode = smallest;
    node->rightNode = largest;
    return node;
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
        std::cout << "l(" << node->parent->value << "): " << node->value;
        break;
    case 1:
        std::cout << "r(" << node->parent->value << "): " << node->value;
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
    add<int>(root, 8);
    //d<int>(root, 6);
    add<int>(root, 2);
    add<int>(root, 10);
    //add<int>(root, 50);
    //add<int>(root, 60);
    //add<int>(root, 32);
    //add<int>(root, 9);
    //add<int>(root, -1);
    //add<int>(root, 10);
    printTree<int>(root);
    std::cout << "h: " << height<int>(root) << "\n";
    std::cout << "we: " << weight<int>(root) << "\n";

    // Rebalance
    std::cout << "------------------ Rebalance \n";
    root = balance<int>(root);
    printTree<int>(root);
    std::cout << "Rebalanced h: " << height<int>(root) << "\n";
    std::cout << "Rebalanced we: " << weight<int>(root) << "\n";

    return 0;
}