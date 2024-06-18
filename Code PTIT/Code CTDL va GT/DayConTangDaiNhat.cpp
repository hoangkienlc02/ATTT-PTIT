#include<bits/stdc++.h>
using namespace std;
int n;
int a[1005],dp[1005];
int main (){
    cin>>n;
    for(int i=1;i<=n;i++) cin>>a[i];
    dp[0]=1;dp[1]=1;
	for(int i=1;i<=n;i++){
        for(int j=1;j<i ;j++){
            if(a[j]<a[i]) dp[i]=max(dp[i] , dp[j]+1);
  		}
  	}
    sort(dp,dp+n+1,greater<int>());
    cout<<dp[0];	
}
