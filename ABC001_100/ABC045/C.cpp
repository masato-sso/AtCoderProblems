#include "bits/stdc++.h"
#include <cstdlib>
using namespace std;

long result=0;

void dfs(string s,int pos,long sum){
  int length=s.size();
  long num;
  string tmp;
  for(int i=pos+1;i<=length;i++){
    tmp=s.substr(pos,i-pos);
    num=strtol(tmp.c_str(),0,10);
    dfs(s,i,sum+num);
  }
  if(pos==length){
    result+=sum;
  }
}

int main(){
  cin.tie(0);
  ios::sync_with_stdio(false);
  string s;

  cin>>s;
  
  dfs(s,0,0);

  cout<<result<<endl;

  return 0;
}