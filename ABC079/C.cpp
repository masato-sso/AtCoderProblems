#include "bits/stdc++.h"

using namespace std;

int ctoi(const char c){
  switch(c){
    case '0': return 0;
    case '1': return 1;
    case '2': return 2;
    case '3': return 3;
    case '4': return 4;
    case '5': return 5;
    case '6': return 6;
    case '7': return 7;
    case '8': return 8;
    case '9': return 9;
    default : return -1;
  }
}

string check(int a,int b,int c,int d){
    if(a+b+c+d==7){
        return to_string(a)+"+"+to_string(b)+"+"+to_string(c)+"+"+to_string(d)+"=7";
    }else if(a+b+c-d==7){
        return to_string(a)+"+"+to_string(b)+"+"+to_string(c)+"-"+to_string(d)+"=7";
    }else if(a+b-c+d==7){
        return to_string(a)+"+"+to_string(b)+"-"+to_string(c)+"+"+to_string(d)+"=7";
    }else if(a-b+c+d==7){
        return to_string(a)+"-"+to_string(b)+"+"+to_string(c)+"+"+to_string(d)+"=7";
    }else if(a-b-c+d==7){
        return to_string(a)+"-"+to_string(b)+"-"+to_string(c)+"+"+to_string(d)+"=7";
    }else if(a-b+c-d==7){
        return to_string(a)+"-"+to_string(b)+"+"+to_string(c)+"-"+to_string(d)+"=7";
    }else if(a+b-c-d==7){
        return to_string(a)+"+"+to_string(b)+"-"+to_string(c)+"-"+to_string(d)+"=7";
    }else if(a-b-c-d==7){
        return to_string(a)+"-"+to_string(b)+"-"+to_string(c)+"-"+to_string(d)+"=7";
    }else{
        return "None";
    }
}

int main(){
  cin.tie(0);
  ios::sync_with_stdio(false);

  string ABCD;
  cin>>ABCD;

  char A=ABCD[0];
  char B=ABCD[1];
  char C=ABCD[2];
  char D=ABCD[3];

  cout<<check(ctoi(A),ctoi(B),ctoi(C),ctoi(D))<<endl;

  return 0;
}