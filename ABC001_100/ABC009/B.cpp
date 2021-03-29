#include<iostream>
#include<string>
#include<stdio.h>
#include<bits/stdc++.h>
#include<map>
#include<vector>

using namespace std;


int main(){
    int N;
    cin>>N;
    vector<int>A(N,0);
    for(int i=0;i<N;i++){
        cin>>A[i];
    }
    int first_max=-1;
    int second_max=-1;

    for(int i=0;i<N;i++){
        if(A[i]>first_max){
            second_max=first_max;
            first_max=A[i];

        }
        else{
            if(A[i]==first_max){
                continue;
            }
            if(A[i]>second_max){
                second_max=A[i];
            }
        }
    }

    cout<<second_max<<endl;
}