#include<iostream>
#include<string>
#include<stdio.h>
#include<bits/stdc++.h>
#include<map>
#include<vector>

using namespace std;


int main(){
    long long N,time;
    cin>>N;
    long long hour,min,sec;
    hour=(long long)N/3600;
    time=N%3600;
    min=(long long)time/60;
    sec=time%60;
    cout<<setfill('0')<<right<<setw(2)<<hour<<":"<<setw(2)<<min<<":"<<setw(2)<<sec<<endl;
}