class Solution {
    struct trie {
        array<std::unique_ptr<trie>, 26> arr;
        int cnt = 0;
        void build(std::string::iterator begin, std::string::iterator end) {
            if (begin == end) {
                ++cnt;
                return;
            }
            int x = *begin - 'a';
            if (!arr[x]) {
                arr[x] = std::make_unique<trie>();
            }
            arr[x]->build(++begin, end);
        }

        void merge(std::unique_ptr<trie> node) {
            if (node == nullptr) {
                return;
            }
            cnt += node->cnt;
            for (int i = 0; i < 26; ++i) {
                if (node->arr[i]) {
                    if (!arr[i]) {
                        arr[i] = std::move(node->arr[i]);
                    } else {
                        arr[i] -> merge(std::move(node->arr[i]));
                    }
                }
            }
        }
    };
public:
    int numMatchingSubseq(string s, vector<string>& words) {
        trie root;
        for (auto& word : words) {
            root.build(word.begin(), word.end());
        }
        for (char c: s) {
            root.merge(std::move(root.arr[c-'a']));
        }
        return root.cnt;
    }
};