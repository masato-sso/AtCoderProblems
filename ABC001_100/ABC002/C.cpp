#include<iostream>
#include<string>
#include<stdio.h>
#include<bits/stdc++.h>

using namespace std;

struct Point
{
    double x,y;
};

int main(){
    Point a,b,c;
    cin>>a.x>>a.y>>b.x>>b.y>>c.x>>c.y;
    //平行移動
    b.x-=a.x;
    c.x-=a.x;
    b.y-=a.y;
    c.y-=a.y;
    a.x=0;
    a.y=0;

    double ans;
    double tmp=b.x*c.y-b.y*c.x;
    if(tmp<0){
        tmp=tmp*(-1.0);
    }
    ans=tmp/2.0;
    cout<<fixed<<setprecision(2)<<ans<<endl;
}