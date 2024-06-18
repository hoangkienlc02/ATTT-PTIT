#include<bits/stdc++.h>
using namespace std;
int n;
bool a[11][11],check[11][11],ok;
string s;
void Try(int x,int y){
	if(x==n&&y==n){
    	cout<<s<<' '; ok=1;return;
	}
    check[x][y]=1;
    if(x<n&&a[x+1][y]==1&&check[x+1][y]==0){
	    s+='D';
	    Try(x+1,y);
	    s.erase(s.length()-1);
	}
	if(y>=1&&a[x][y-1]==1&&check[x][y-1]==0){
	    s+='L';
	    Try(x,y-1);
	    s.erase(s.length()-1);
	}
	if(y<n&&a[x][y+1]==1&&check[x][y+1]==0){
	    s+='R';
	    Try(x, y+1);
	    s.erase(s.length()-1);
	}
	if(x>=1&&a[x-1][y]==1&&check[x-1][y]==.0){
	    s+='U';
	    Try(x-1,y);
	    s.erase(s.length()-1);
	}
	check[x][y]=0;
}
int main(){
   int t;cin>>t;
   while(t--){
      cin>>n;ok=0;
      for(int i=1;i<=n;i++)
        for(int j=1;j<=n;j++)
            cin>>a[i][j];
      if(a[1][1]==0){cout<<-1<<endl;continue;}
      Try(1,1);
      if(ok==0) cout<<-1;
      cout<<endl;
	}
   return 0;
}
