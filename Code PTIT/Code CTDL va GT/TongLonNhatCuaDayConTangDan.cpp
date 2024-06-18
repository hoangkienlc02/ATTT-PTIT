#include<bits/stdc++.h>
using namespace std;
void TongLonNhatCuaDayConTangDan(){
   int n;cin>>n;
   int a[n+1],dp[n+1];
   for(int i=0;i<n;i++)cin>>a[i];
   dp[0]= a[0];//1
   for(int i=1;i<n;i++){//2
       int summax=0;
       for(int j=0;j<i;j++)
          if(a[j]<a[i])summax=max(summax,dp[j]);
       dp[i]=a[i]+summax;
   }
   sort(dp,dp+n);
   cout<<dp[n-1]<<endl;
}
int main(){
   int t;cin>>t;
   while (t--)TongLonNhatCuaDayConTangDan();
   return 0;
}
