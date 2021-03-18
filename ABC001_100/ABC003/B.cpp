#include<iostream>
#include<string>
#include<stdio.h>
#include<bits/stdc++.h>

using namespace std;

int main(){
    string S,N;
    cin>>S>>N;
    bool flag=true;

    for(int i=0;i<S.size();i++){
        if(S[i]==N[i]){
            continue;
        }else{
            if(S[i]=='@' || N[i]=='@'){
                if(S[i]=='@'){
                    if(N[i]=='a' || N[i]=='t' || N[i]=='c' || N[i]=='o' || N[i]=='d' || N[i]=='e' || N[i]=='r'){
                        continue;
                    }else{
                        flag=false;
                    }
                }else{
                    if(S[i]=='a' || S[i]=='t' || S[i]=='c' || S[i]=='o' || S[i]=='d' || S[i]=='e' || S[i]=='r'){
                        continue;
                    }else{
                        flag=false;
                    }
                }
            }
            flag=false;
        }
    }

    if(flag){
        cout<<"You can win"<<endl;
    }else{
        cout<<"You will lose"<<endl;
    }
}