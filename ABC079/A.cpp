#include "bits/stdc++.h"

using namespace std;

int main(){
  cin.tie(0);
  ios::sync_with_stdio(false);

  string N;

  cin>>N;
  
  char tmp=N[0];
  int count=0;
  int count_max=0;
  
  for(int i=0;i<N.size();i++){
    if(tmp==N[i]){
      count++;
    }else{
      tmp=N[i];
      count=1;
    }
    if(count_max<count){
      count_max=count;
    }
  }
  
  if(count_max>=3){
    cout<<"Yes"<<endl;
  }else{
    cout<<"No"<<endl;
  }
  
  return 0;
}