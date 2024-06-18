#include<bits/stdc++.h>
using namespace std;
int n,s;
int a[202],dp[40005];
void DayConCoTongBangS(){
   memset(dp,0,sizeof(dp));
   cin>>n>>s;
   for(int i=0;i<n;i++) cin>>a[i];
   dp[0]=1;
   for(int i=0;i<n;i++){
       for(int j=s;j>=a[i];j--){
          if(dp[j-a[i]]==1) dp[j]=1;
		}
	}
   cout<<(dp[s]==1?"YES":"NO")<<endl;
}
int main (){
   int t;cin>>t;
   while(t--) DayConCoTongBangS();
   return 0;
}

