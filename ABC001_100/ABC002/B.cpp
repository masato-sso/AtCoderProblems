#include<iostream>
#include<string>
#include<stdio.h>

using namespace std;
typedef long long ll;

int main(){
    string W;
    cin>>W;
    string res="";
    for(int i=0;i<(int)W.size();i++){
        if(W[i]=='a' || W[i]=='i' || W[i]=='u' || W[i]=='e' || W[i]=='o'){
            continue;
        }
        res+=W[i];
    }
    cout<<res<<endl;
}