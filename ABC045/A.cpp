#include "bits/stdc++.h"
using namespace std;

int daikei(int a,int b,int h){
    return (a+b)*h/2;
}

int main(){
  int a,b,h;

  cin>>a;
  cin>>b;
  cin>>h;

  cout<<daikei(a,b,h)<<endl;

  return 0;
}