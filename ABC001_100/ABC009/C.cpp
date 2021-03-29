#include<iostream>
#include<string>
#include<stdio.h>
#include<bits/stdc++.h>
#include<map>
#include<vector>

using namespace std;


int main(){
    int N,K;
    cin>>N>>K;
    string S,ans;
    ans="";
    cin>>S;

    int count_s[26]={0};
    int count_t[26]={0};
    for(int i=0;i<N;i++){
        ++count_s[S[i]-'a'];
        ++count_t[S[i]-'a'];
    }
    for(int i=0;i<N;i++){
        for(int idx=0;idx<26;idx++){
            if(!count_t[idx]) continue;
            char c='a'+idx;
            int diff=0;
            for(int j=0;j<i;j++){
                if(S[j]!=ans[j]) diff++;
            }
            if(c!=S[i]) diff++;
            --count_s[S[i]-'a'];
            --count_t[idx];
            int num=(N-1)-i;
            for(int j=0;j<26;j++){
                num-=min(count_s[j],count_t[j]);
            }
            diff+=num;
            if(diff<=K){
                ans+=('a'+idx);
                break;
            }
            ++count_s[S[i]-'a'];
            ++count_t[idx];
        }
    }
    cout<<ans<<endl;
}