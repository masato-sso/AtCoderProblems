#include<iostream>
#include<string>
#include<stdio.h>
#include<bits/stdc++.h>
#include<vector>

using namespace std;

vector<long long int>memo;

long long int f(long long int n){
    if(memo[n]==-1){ 
        if(n==1) return memo[1]=0;
        if(n==2) return memo[2]=0;
        if(n==3) return memo[3]=1;
        else return memo[n]=(f(n-1)+f(n-2)+f(n-3))%10007;
    }else{
        return memo[n];
    }
}

int main(){
    long long int n;
    cin>>n;
    memo.assign(n+1,-1);
    cout<<f(n)<<endl;
}