#include<bits/stdc++.h>
const int mod=1e9+7;
using namespace std;
int a[ 1005],n,k,dp[1005][1005];
void tinh(){//1
   for(int i=0;i<1005;i++){
      for(int j=0;j<=i;j++){
          if(j==0||j==i)dp[i][j]=1;
          else dp[i][j]= (dp[i-1][j-1]+dp[i-1][j])%mod;
       }
	}
}
int main(){
     int t;cin>>t;
     tinh();
     while(t--) {
       cin>>n>>k;
       cout<<dp[n][k]<<endl;
	}
}
