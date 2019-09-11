#include "bits/stdc++.h"

using namespace std;

int main(){
  cin.tie(0);
  ios::sync_with_stdio(false);

  long long N;

  cin>>N;

  long long L[N+1];
  L[0]=2;
  L[1]=1;

  for(int i=2;i<=N;i++){
      L[i]=L[i-1]+L[i-2];
  }

  cout<<L[N]<<endl;

  return 0;
}