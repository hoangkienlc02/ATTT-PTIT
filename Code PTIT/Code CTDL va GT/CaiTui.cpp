#include<bits/stdc++.h>
int n,v;
int a[ 1005],c[1005],dp[1005][1005];
using namespace std;
void caiTui(){
    cin>>n>>v;
   for(int i=1;i<=n;i++) cin>>a[i];
   for(int i=1;i<=n;i++) cin>>c[i];
   for(int i=0;i<=v;i++) dp[0][i]=0;
   for(int i=1;i<=n;i++){
      for(int j=1;j<=v;j++){
          if(a[i]<=j) dp[i][j]=max(dp[i-1][j], dp[i-1][j-a[i]]+c[i]);
          else dp[i][j]=dp[i-1][j];
    	}
	}
   cout<<dp[n][v]<<endl;
}
int main(){
   int t;cin>>t;
   while(t--) caiTui();
   return 0;
}
