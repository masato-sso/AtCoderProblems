#include "bits/stdc++.h"
using namespace std;


int main(){
  string a,b,c;

  cin>>a;
  cin>>b;
  cin>>c;

  char turn='a';
  int a_idx=0;
  int b_idx=0;
  int c_idx=0;

  int a_length=a.length();
  int b_length=b.length();
  int c_length=c.length();

  string winner;

  while(true){
      if(turn=='a'){
          if(a[a_idx]=='a'){
              turn='a';
          }else if(a[a_idx]=='b'){
              turn='b';
          }else if(a[a_idx]=='c'){
              turn='c';
          }
          if(a_idx>=a_length){
                winner='A';
                break;
            }
          a_idx++;
      }else if(turn=='b'){
          if(b[b_idx]=='a'){
              turn='a';
          }else if(b[b_idx]=='b'){
              turn='b';
          }else if(b[b_idx]=='c'){
              turn='c';
          }
          if(b_idx>=b_length){
                winner="B";
                break;
            }
          b_idx++;
      }else if(turn=='c'){
          if(c[c_idx]=='a'){
              turn='a';
          }else if(c[c_idx]=='b'){
              turn='b';
          }else if(c[c_idx]=='c'){
              turn='c';
          }
          if(c_idx>=c_length){
                winner='C';
                break;
            }
          c_idx++;
      }
  }
  cout<<winner<<endl;

  return 0;
}