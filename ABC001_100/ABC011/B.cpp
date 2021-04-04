#include<iostream>
#include<string>
#include<stdio.h>
#include<bits/stdc++.h>
#include<map>
#include<vector>

using namespace std;


int main(){
    string S;
    string ans="";
    cin>>S;
    if(!isupper(S[0])){
        ans+=toupper(S[0]);
    }else{
        ans+=S[0];
    }
    for(int i=1;i<S.size();i++){
        if(isupper(S[i])){
            ans+=tolower(S[i]);
        }else{
            ans=ans+S[i];
        }
    }
    cout<<ans<<endl;
}