#include<iostream>
#include<string>
#include<stdio.h>
#include<bits/stdc++.h>
#include<vector>

using namespace std;


int main(){
    int T,N,M;
    cin>>T>>N;
    vector<int>A(N,0);
    for(int i=0;i<N;i++){
        cin>>A[i];
    }
    cin>>M;
    vector<int>B(M,0);
    for(int i=0;i<M;i++){
        cin>>B[i];
    }

    sort(A.begin(),A.end());
    sort(B.begin(),B.end());
    
    int start=0;
    bool p=true;
    for(int i=0;i<M;i++){
        bool flag=false;
        for(int j=start;j<N;j++){
            if(B[i]-T<=A[j] && A[j]<=B[i]){
                start=j+1;
                flag=true;
                break;
            }
        }
        if(flag){
            continue;
        }else{
            p=false;
            break;
        }
    }

    if(p){
        cout<<"yes"<<endl;
    }else{
        cout<<"no"<<endl;
    }

}