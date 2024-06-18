#include <bits/stdc++.h>
using namespace std;
int n;
bool a[11][11],ok;
string s;
void Try(int x,int y){
	if(x==n&&y==n){
    	cout<<s<<' '; ok=1;return;
	}
	if(a[x+1][y]==1){
    	s+='D';
    	Try(x+1,y);
    	s.erase(s.length()-1);
	}
	if(a[x][y+1]==1){
     	s+='R';
    	Try(x,y+1);
     	s.erase(s.length()-1);
  	}
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
}
