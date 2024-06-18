#include <bits/stdc++.h>
using namespace std;
void TongCacXauCon(){
   string s;cin>>s;
   long long n=s.length();
   long long dp[n+1];
   dp[0]=s[0]-'0';//1
   long long res=dp[0];
   for(int i=1;i<n;i++){
       dp[i]=10*dp[i-1]+(s[i]-'0')*(i+1);
       res+=dp[i];
    }cout<<res<<endl;
}
int main(){
  int t;cin>>t;
  while(t--) TongCacXauCon();
  return 0;
}
