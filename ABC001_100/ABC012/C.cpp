#include<iostream>
#include<string>
#include<stdio.h>
#include<bits/stdc++.h>
#include<map>
#include<vector>

using namespace std;


int main(){
    const int correct_sum=2025;
    int N;
    cin>>N;
    int diff=correct_sum-N;
    for(int i=1;i<10;i++){
        if(diff%i==0){
            int div=(int)diff/i;
            if(0<div && div<10) cout<<i<<" x "<<div<<endl;
        }
    }
}