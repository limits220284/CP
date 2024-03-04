struct AVLTreeNode 
{
    int data, height;
    AVLTreeNode* left, * right;
    AVLTreeNode(int val) :data(val), left(NULL), right(NULL), height(0) {}
};
int getheight(AVLTreeNode* r) 
{
    return r == NULL ? 0 : r->height;
}
AVLTreeNode* leftLeftRotation(AVLTreeNode* k2)
{
    AVLTreeNode* k1 = k2->left;
    k2->left = k1->right;
    k1->right = k2;
    k2->height = max(getheight(k2->left), getheight(k2->right)) + 1;
    k1->height = max(getheight(k1->left), k2->height) + 1;
    return k1;
}
AVLTreeNode* rightRightRotation(AVLTreeNode* k1)
{
    AVLTreeNode* k2 = k1->right;
    k1->right = k2->left;
    k2->left = k1;
    k1->height = max(getheight(k1->left), getheight(k1->right)) + 1;
    k2->height = max(getheight(k2->right), k1->height) + 1;
    return k2;
}
AVLTreeNode* leftRightRatation(AVLTreeNode* k3)
{
    k3->left = rightRightRotation(k3->left);
    return leftLeftRotation(k3);
}
AVLTreeNode* rightLeftRotation(AVLTreeNode* k4)
{
    k4->right = leftLeftRotation(k4->right);
    return rightRightRotation(k4);
}
AVLTreeNode* insertNode(AVLTreeNode* root, int data)
{
    if (!root)
        root = new AVLTreeNode(data);
    else if (data < root->data)
    {
        root->left = insertNode(root->left, data);
        if (getheight(root->left) - getheight(root->right) == 2)
            if (data < root->left->data)
                root = leftLeftRotation(root);
            else
                root = leftRightRatation(root);
    }
    else if (data > root->data)
    {
        root->right = insertNode(root->right, data);
        if (getheight(root->right) - getheight(root->left) == 2)
            if (data > root->right->data)
                root = rightRightRotation(root);
            else
                root = rightLeftRotation(root);
    }
    else
        cout << "fail" << endl;
    root->height = max(getheight(root->left), getheight(root->right)) + 1;
    return root;
}
AVLTreeNode* Root=nullptr;
void dfs(TreeNode* root)
{
    if(!root) return ;
    Root=insertNode(Root,root->val);
    dfs(root->left);
    dfs(root->right);
}
void build(AVLTreeNode* Troot,TreeNode*& root)
{
    if(!Troot) return ;
    root=new TreeNode(Troot->data);
    build(Troot->left,root->left);
    build(Troot->right,root->right);
}
class Solution {
public:
    TreeNode* balanceBST(TreeNode* root) {
        Root=nullptr;
        dfs(root);
        TreeNode* ret=nullptr;
        build(Root,ret);
        return ret;
    }
};