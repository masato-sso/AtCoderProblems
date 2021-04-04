#include<iostream>
#include<string>
#include<stdio.h>
#include<bits/stdc++.h>
#include<map>
#include<vector>

using namespace std;


int main(){
    int N,NG[3];
    cin>>N;
    cin>>NG[0];
    cin>>NG[1];
    cin>>NG[2];

    vector<vector<bool>> dp(305,vector<bool>(105,false));

    dp[N][0]=true;
    if(N!=NG[0] && N!=NG[1] && N!=NG[2]){
        for(int n=0;n<=100;n++){
            for(int i=N;i>=0;i--){
                if(i==NG[0] || i==NG[1] || i==NG[2]) continue;
                for(int j=1;j<=3;j++){
                    if(i-j>=0 && i-j!=NG[0] && i-j!=NG[1] && i-j!=NG[2]){
                        if(!dp[i-j][n+1] && dp[i][n]) dp[i-j][n+1]=true;
                    }
                }
            }
        }
    }
    for(int i=0;i<=100;i++){
        if(dp[0][i]){
            cout<<"YES"<<endl;
            return 0;
        }
    }
    cout<<"NO"<<endl;
}