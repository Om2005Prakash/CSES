#include <vector>
#include <set>
#include <unordered_map>
#include <deque>
#include <algorithm>
using namespace std;

vector<int> v = {1, 2, 3, 4, 5};
set<int> s;
unordered_map<int, int> umap;
deque<int> dq;

int main(){
    sort(v.begin(), v.end());
    sort(v.rbegin(), v.rend());
    int key = 3;
    if (binary_search(v.begin(), v.end(), key)) {}
    do{

    }while (next_permutation(v.begin(), v.end()));
    int minval = *min_element(v.begin(), v.end());
    int maxval = *max_element(v.begin(), v.end());
    vector<int> u;
    for(int i = 0; i < 10; i++) if (i%2 == 0) v.
    
}