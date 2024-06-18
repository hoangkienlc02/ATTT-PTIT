#include<bits/stdc++.h>
using namespace std;
string s;
bool dp[1005][1005];
void XauConDoiXungDaiNhat(){
     memset(dp,0,sizeof(dp));
     cin>>s;
     s=' '+s;
     int n=s.length(),res=1;
     for(int i=1;i<=n;i++)
          for(int j=1;j<=i;j++)
                dp[i][j]=1;//1
     for(int k=1;k<=n-1;k++){
          for(int i=1;i<=n-k;i++){
                int j=k+i;
                if(s[i]==s[j]) dp[i][j]=dp[i+1][j-1];//2
                if(dp[i][j]!=0) res=max(j-i+1,res);
        }
     }
     cout<<res<<endl;
}
int main(){
       int t;cin>>t;
       while(t--) XauConDoiXungDaiNhat();
      return 0;
}
