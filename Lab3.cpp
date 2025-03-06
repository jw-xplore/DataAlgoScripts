#include <iostream>
#include <chrono>
#include <thread>

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
template <typename T> void printTree(BTSNode<T>* root);

// Search for value in tree
template <typename T>
BTSNode<T>* find(BTSNode<T>* node, T value)
{
    // Fail to find
    if (node == nullptr)
        return nullptr;
      
    std::this_thread::sleep_for(std::chrono::milliseconds(1));
    //std::cout << "searching " << value << "\n";
    //std::cout<<"\b "; 

    // Find
    if (value == node->value)
    {
        std::cout << "found " << value << "\n";
        return node;
    }

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
        }
        else
            node->leftNode = add<T>(node->leftNode, value); // Iterate to left
    }

    // Right
    if (value > node->value)
    {
        if (node->rightNode == nullptr)
        {
            // Add
            node->rightNode = new BTSNode<T>(value, node);
        }
        else
            node->rightNode = add<T>(node->rightNode, value); // Iterate to left
    }

    return node;
}

// Insert value to tree and rebalance tree afterwards
template <typename T>
BTSNode<T>* addAndBalance(BTSNode<T>* node, T value)
{
    // Fail
    if (node == nullptr)
        return node;

    // Add
    node = add<T>(node, value);

    // Balance
    if (node->parent == nullptr)
    {
        node = balance<T>(node);
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

template <typename T>
int size(BTSNode<T>* node)
{
    if (node == nullptr)
        return 0;
    
    int leftS = size(node->leftNode);
    int rightS = size(node->rightNode);
    
    return 1 + leftS + rightS;
}

// Return difference between height of left and right subtrees from seleted root node
// Positive = left heavy
// Negative = right heavy
// 0 = balanced
template <typename T>
int weight(BTSNode<T>* node)
{
    int leftH = size(node->leftNode);
    int rightH = size(node->rightNode);

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
        node->leftNode = balance(node->leftNode);

    if (node->rightNode != nullptr)
        node->rightNode = balance(node->rightNode);

    // Check balance and children balance
    int w = weight(node);

    // No need to rebalance
    if (abs(w) <= 1)
        return node;

    // Rotation values
    BTSNode<T>* newRoot = nullptr;
    BTSNode<T>* smallest = nullptr; // left
    BTSNode<T>* largest = nullptr; // rigth

    BTSNode<T>* prevLeft = nullptr;
    BTSNode<T>* prevRight = nullptr;

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

            if (node->leftNode != nullptr)
                prevLeft = node->leftNode->rightNode;

            largest->leftNode = nullptr;
        }

        // Left-right rotation
        if (lw <= 0)
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

            if (node->rightNode != nullptr)
                prevRight = node->rightNode->leftNode;

            smallest->rightNode = nullptr;
        }

        // Right-left rotation
        if (rw >= 0)
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

    if (prevLeft != nullptr)
    {
        prevLeft->parent = largest;
        largest->leftNode = prevLeft;
    }

    if (prevRight != nullptr)
    {
        prevRight->parent = smallest;
        smallest->rightNode = prevRight;
    }

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

template <typename T>
BTSNode<int>* treeTest(T data[], int dataSize, const char* name, bool balanced = false)
{
    std::cout << "Run test: " << name << " ------------------------------------ \n";

    int largestVal = data[0];

    BTSNode<int>* root = new BTSNode<int>(data[0]);
    std::chrono::steady_clock::time_point begin = std::chrono::steady_clock::now();

    for (int i = 1; i < dataSize; i++)
    {
        if (balanced)
            root = addAndBalance<T>(root, data[i]);
        else
            root = add<T>(root, data[i]);
            
        if (largestVal < data[i])
            largestVal = data[i];
    }

    std::cout << name << " add time: " << std::chrono::duration_cast<std::chrono::microseconds>((std::chrono::steady_clock::now() - begin)).count() << " ms \n";

    /*
    begin = std::chrono::steady_clock::now();
    printTree(root);
    std::cout << name << " print time: " << std::chrono::duration_cast<std::chrono::microseconds>((std::chrono::steady_clock::now() - begin)).count() << "ms \n";
    */
    std::chrono::steady_clock::time_point begin2 = std::chrono::steady_clock::now();
    find<T>(root, largestVal);
    std::cout << name << " find time: " << std::chrono::duration_cast<std::chrono::microseconds>((std::chrono::steady_clock::now() - begin2)).count() << " ms \n";

    std::cout << "Finished test: " << name << " ------------------------------------ \n\n";

    return root;
}

int* randomDataSet(int size, int min, int max)
{
    srand(time(0));
    int* data = new int[size];

    for (int i = 1; i < size; i++)
    {
        data[i] = rand() % max - min;
    }

    return data;
}

int* linearDataSet(int size)
{
    int* data = new int[size];

    for (int i = 1; i < size; i++)
    {
        data[i] = i;
    }

    return data;
}

int main() {

    // Data
    int dataL = 2000;
    int* data = randomDataSet(dataL, 1, 1000000);

    int worstDataL = 2000;
    int* worstData = linearDataSet(worstDataL);

    // Regular BST
    BTSNode<int>* root = treeTest<int>(data, dataL, "Regular");
    BTSNode<int>* worstTree = treeTest<int>(worstData, worstDataL, "Worst");

    // Balanced BST - AVL style
    BTSNode<int>* balanced = treeTest<int>(data, dataL, "Balanced", true);
    BTSNode<int>* worstBalanced = treeTest<int>(worstData, worstDataL, "Balanced worst", true);
    
    // Balance representation
    std::cout << "--------------------- \n";
    std::cout << "--------------------- \n";
    std::cout << "Show balanced tree: \n";
    int* shortData = randomDataSet(10, -50, 50);
    BTSNode<int>* balanceShow = treeTest<int>(shortData, 10, "Balanced for show", true);
    printTree(balanceShow);
    
    
    /*
    printTree(balanced);
    std::cout << "rand w: " << weight(balanced) << "\n";
    printTree(worstBalanced);
    std::cout << "worst w: " << weight(worstBalanced) << "\n";
    */
}