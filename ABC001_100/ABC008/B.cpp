#include<iostream>
#include<string>
#include<stdio.h>
#include<bits/stdc++.h>
#include<vector>
#include<map>

using namespace std;


int main(){
    int N;
    cin>>N;
    map<string,int> dict;
    for(string x;N--;dict[x]++){
        cin>>x;
    }
    vector<string>keys;
    for(auto iter=dict.begin();iter!=dict.end();iter++){
        keys.push_back(iter->first);
    }
    int ans_cnt=-1;
    string ans;
    for(int i=0;i<keys.size();i++){
        if(ans_cnt<dict[keys[i]]){
            ans_cnt=dict[keys[i]];
            ans=keys[i];
        }
    }
    cout<<ans<<endl;
}