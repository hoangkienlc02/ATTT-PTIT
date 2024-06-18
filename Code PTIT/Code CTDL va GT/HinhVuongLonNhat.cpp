#include<bits/stdc++.h>
using namespace std;
int n,m,res,a[505][505], dp[505][505];
void HinhVuongLonNhat(){
   memset(a,0,sizeof(a));
   memset(dp,0,sizeof(dp));
   cin>>n>>m;res=1;
   for(int i=0;i<n;i++)
       for(int j=0;j<m;j++)
          cin>>a[i][j];
   for(int i=0;i<n;i++) dp[i][0]=a[i][0];
   for(int i=0;i<m;i++) dp[0][i]=a[0][i];
for(int i=1;i<n;i++)
      for(int j=1;j<m;j++)
          if(a[i][j]==1)//3
          dp[i][j]=min(dp[i-1][j],min(dp[i][j-1],dp[i-1][j-1] ))+1;
	for(int i=0;i<n;i++)
	  for(int j=1;j<m;j++)
	    res=max(res,dp[i][j]);
	cout<<res<<endl;
}
int main(){
	int t;cin>>t;
	while (t--) HinhVuongLonNhat();
	return 0;	
}

