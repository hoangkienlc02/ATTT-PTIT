#include <bits/stdc++.h>

using namespace std;
void GiaiMa(){
   string s;cin>>s;
   int dp[45],n=s.length();
   if(s[0]=='0'){cout<<0<<endl;return;}
   s=' '+s;
   memset(dp,0,sizeof(dp));
   dp[0]=1;dp[1]=1;
   for(int i=2;i<=n;i++){
       if(s[i]>'0')dp[i]=dp[i-1] ;
       if(s[i-1]=='1'||(s[i-1]=='2'&&s[i]<'7'))dp[i]+=dp[i-2];
   }
   cout<<dp[n]<<endl;
}
int main(){
    int t;cin>>t;
    while(t--) GiaiMa();
    return 0;
}
