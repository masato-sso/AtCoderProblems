#include "bits/stdc++.h"

using namespace std;

int main(){
  cin.tie(0);
  ios::sync_with_stdio(false);

  int R;

  cin>>R;

  if(R<1200){
    cout<<"ABC"<<endl;
  }else if(R<2800){
    cout<<"ARC"<<endl;
  }else{
    cout<<"AGC"<<endl;
  }

  
  return 0;
}