#include<iostream>
#include<string>
#include<stdio.h>
#include<bits/stdc++.h>
#include<vector>

using namespace std;

typedef long long int ln;

int main(){
    ln N,M,a,b,c;
    a=-1;
    b=-1;
    c=-1;
    cin>>N>>M;

    for(int i=0;i<N+1;i++){
        b=4*N-2*i-M;
        if(b>=0){
            a=i;
            c=N-a-b;
            if(a>=0 && c>=0){
                break;
            }else{
                a=-1;
                b=-1;
                c=-1;
            }
        }else{
            a=-1;
            b=-1;
            c=-1;
        }
    }
    cout<<a<<" "<<b<<" "<<c<<endl;
}