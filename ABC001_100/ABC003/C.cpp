#include<iostream>
#include<string>
#include<stdio.h>
#include<bits/stdc++.h>
#include<vector>

using namespace std;

int main(){
    int N,K;
    cin>>N>>K;
    vector<int> R(N,0);
    for(int i=0;i<N;i++){
        cin>>R[i];
    }
    sort(R.begin(),R.end());

    double C=0;
    for(int i=N-K;i<N;i++){
        C=(C+R[i])/2.0;
    }

    cout<<setprecision(10)<<C<<endl;
}