#include<bits/stdc++.h>
using namespace std;
int V,E,u,check[1005];
vector <int> a[1005];
void dfs(int u){
   cout<<u<<' ';
   check[u]=1;
	for(int i=0;i<a[u].size();i++){
       int v=a[u][i];
       if(check[v]==0) dfs(v);
	}
}
void DFSTrenDoThiVoHuong(){
   cin>>V>>E>>u;
   memset(a,0,sizeof(a));
   memset(check,0,sizeof(check));
	for(int i=1;i<=E;i++){
       int x,y;cin>>x>>y;
       a[x].push_back(y);
       a[y].push_back(x);
	}
   dfs(u);
   cout<<endl;
}
int main(){
   int t;cin>>t;
   while(t--) DFSTrenDoThiVoHuong();
}

