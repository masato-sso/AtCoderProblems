#include<iostream>
#include<string>
#include<stdio.h>
#include<bits/stdc++.h>

using namespace std;

int main(){
    int N;
    cin>>N;

    long long ex=0;

    for(int i=1;i<N+1;i++){
        ex+=i*10000;
    }

    cout<<ex/N<<endl;
}