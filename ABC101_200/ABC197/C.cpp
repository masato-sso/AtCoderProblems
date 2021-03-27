#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;

int main(){
    long long N;
    cin>>N;
    vector<long long>a(N,0);
    for(int i=0;i<N;i++){
        cin>>a[i];
    }
    vector<long long> res ;
    for (int bit = 0; bit < (1<<(N-1)); ++bit) {
        long long tmp = 0;
        long long xors = 0;
        for (int i = 0; i < N-1; ++i) {
            tmp|=a[i];
            if (bit & (1<<i)) {
                xors ^= tmp;
                tmp = 0;
            }
        }
        tmp |=a[N-1];
        xors ^= tmp;
        res.push_back(xors);
    }
    cout<<*min_element(res.begin(),res.end())<<endl;
}