#include<bits/stdc++.h>
using namespace std;
int v,e,u,U,check[1005];
vector <int> a[1005];
void dfs(int u){
   check[u]=1;
   for(int i=0;i<a[u].size();i++){
       int U=a[u][i];
       if(check[U]==0) {
          dfs(U);
    	}
	}
}
void KiemTraDuongDi(){
   cin>>v>>e;
   memset(a,0,sizeof(a));
 for(int i=1;i<=e;i++){
       int u,v;cin>>u>>v;
		a[u].push_back(v);
		a[v].push_back(u);
	}
	int q;cin>>q;
	for(int i=1;i<=q;i++){
		int u,v;cin>>u>>v;
		memset(check,0,sizeof(check));
		dfs(u); 
		if(check[v]==0) cout<<"NO"<<endl;
		else cout<<"YES"<<endl;
	}
}
int main(){
	int t;cin>>t;
	while(t--) KiemTraDuongDi();
}
