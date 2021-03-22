#include<iostream>
#include<string>
#include<stdio.h>
#include<bits/stdc++.h>
#include<vector>

using namespace std;
using P=pair<int,int>;

const int dx[4]={1,0,-1,0};
const int dy[4]={0,1,0,-1};

int main(){
    int R,C,sy,sx,gy,gx;
    cin>>R>>C>>sy>>sx>>gy>>gx;
    sy--;
    sx--;
    gy--;
    gx--;

    string stage[R];
    for(int i=0;i<R;i++){
        cin>>stage[i];
    }

    vector<vector<int>> dist(R,vector<int>(C,-1));
    queue<P> que;
    dist[sy][sx]=0;
    que.push(make_pair(sy,sx));
    while(!que.empty()){
        auto v=que.front();
        que.pop();
        for(int dir=0;dir<4;dir++){
            int ny=v.first+dy[dir];
            int nx=v.second+dx[dir];
            if(stage[ny][nx]=='#'){
                continue;
            }else if(ny<=0 || ny>=R-1 || nx<=0 || nx>=C-1){
                continue;
            }else if(dist[ny][nx]==-1){
                dist[ny][nx]=dist[v.first][v.second]+1;
                que.push(make_pair(ny,nx));
            }
        }
    }
    cout<<dist[gy][gx]<<endl;
}