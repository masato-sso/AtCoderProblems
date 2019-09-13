#include "bits/stdc++.h"

using namespace std;

int main(){
  cin.tie(0);
  ios::sync_with_stdio(false);

  string S;
  int count;
  bool flag=true;


  cin>>S;
  
  if(S[0]=='A'){
      for(int i=2;i<S.size()-1;i++){
          if(S[i]=='C'){
              count++;
          }else if(S[i]>='A' && S[i]<='Z'){
              flag=false;
              break;
          }
      }
      if(S[1]>='A' && S[1]<='Z'){
          flag=false;
      }
      if(S[S.size()-1]>='A' && S[S.size()-1]<='Z'){
          flag=false;
      }
      if(count==1 && flag){
          cout<<"AC"<<endl;
      }else{
          cout<<"WA"<<endl;
      }
  }else{
      cout<<"WA"<<endl;
  }
  
  return 0;
}