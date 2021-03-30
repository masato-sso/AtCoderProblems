#include<iostream>
#include<string>
#include<stdio.h>
#include<bits/stdc++.h>
#include<map>
#include<vector>

using namespace std;


int main(){
    int txa,tya,txb,tyb,T,V;
    cin>>txa>>tya>>txb>>tyb>>T>>V;
    int n;
    cin>>n;
    int x,y;
    bool flag=false;
    for(int i=0;i<n;i++){
        cin>>x>>y;
        if(flag) continue;
        double first=sqrt((x-txa)*(x-txa)+(y-tya)*(y-tya));
        double second=sqrt((x-txb)*(x-txb)+(y-tyb)*(y-tyb));
        double move=T*V;
        if((first+second)<=move){
            flag=true;
        }
    }
    if(flag){
        cout<<"YES"<<endl;
    }else{
        cout<<"NO"<<endl;
    }


}