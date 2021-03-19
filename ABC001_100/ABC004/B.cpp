#include<iostream>
#include<string>
#include<stdio.h>
#include<bits/stdc++.h>
#include<vector>

using namespace std;

int main(){
    vector<vector<string>>c;
    vector<string> v(4,"");
    for(int i=0;i<4;i++){
        for(int j=0;j<4;j++){
            cin>>v[j];
        }
        c.push_back(v);
    }

    vector<vector<string>>out;

    for(int i=3;i>-1;i--){
        for(int j=3;j>-1;j--){
            cout<<c[i][j];
            cout<<" ";
        }
        cout<<endl;
    }

}