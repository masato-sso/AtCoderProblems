#include<iostream>
#include<string>
#include<stdio.h>
#include<bits/stdc++.h>
#include<vector>

using namespace std;

typedef long long ll;

void swap(ll &a,ll &b){
    ll tmp;
    tmp=a;
    a=b;
    b=tmp;
}

int main(){
    ll N;
    cin>>N;
    ll first,second,mod;
    vector<ll> a={1,2,3,4,5,6};
    for(int i=0;i<N;i++){
        mod=i%5;
        first=mod+1;
        second=mod+2;
        swap(a[first-1],a[second-1]);
    }
    for(int i=0;i<6;i++){
        cout<<a[i];
    }
    cout<<endl;
}