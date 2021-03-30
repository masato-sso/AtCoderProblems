#include<iostream>
#include<string>
#include<stdio.h>
#include<bits/stdc++.h>
#include<map>
#include<vector>

using namespace std;


int main(){
    int n;
    cin>>n;
    vector<int>a(n,0);
    for(int i=0;i<n;i++){
        cin>>a[i];
    }
    int ans=0;
    for(int i=0;i<n;i++){
        while(a[i]%2==0 || a[i]%3-2==0){
            a[i]--;
            ans++;
        }
    }
    cout<<ans<<endl;
}