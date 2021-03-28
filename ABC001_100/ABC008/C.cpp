#include<iostream>
#include<string>
#include<stdio.h>
#include<bits/stdc++.h>
#include<map>
#include<vector>

using namespace std;


int main(){
    long long N;
    cin>>N;
    vector<long long>C(N,0);
    for(int i=0;i<N;i++){
        cin>>C[i];
    }
    double ans=0;
    for(int i=0;i<N;i++){
        int cnt=0;
        for(int j=0;j<N;j++){
            if(i==j) continue;
            if(C[i]%C[j]==0) cnt++;
        }
        if(cnt%2==0){
            ans+=(cnt+2.0)/(2.0*cnt+2.0);
        }else{
            ans+=1/2.0;
        }
    }
    cout<<fixed<<setprecision(12)<<ans<<endl;
}