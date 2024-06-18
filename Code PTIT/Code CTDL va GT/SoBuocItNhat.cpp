#include <bits/stdc++.h>
using namespace std ;

void SoBuocItNhat(){
     int n;cin>>n;
     int a[n+1],dp[n+1];
     for(int i=0;i<n;i++) cin>>a[i];
     memset(dp,0,sizeof(dp));
     dp[0]=1;//1
     for(int i=1;i<n;i++){//2
          dp[i]=1;
          for(int j=0;j<i;j++){
                if(a[j]<=a[i] )dp[i]=max(dp[i] ,dp[j]+1);
           }
     }
     int res=*max_element(dp,dp+n);
     cout<<n-res<<endl;
}
int main(){
     int t; cin>>t;
     while(t--) SoBuocItNhat();
     return 0;
}
