#include<iostream>
#include<string>
#include<stdio.h>
#include<bits/stdc++.h>
#include<vector>

using namespace std;

int main(){
    int N;
    cin>>N;
    vector<int> T(N,0);
    for(int i=0;i<N;i++){
        cin>>T[i];
    }

    int ans=10000;
    for(int i=0;i<N;i++){
        if(T[i]<ans){
            ans=T[i];
        }
    }
    cout<<ans<<endl;
}