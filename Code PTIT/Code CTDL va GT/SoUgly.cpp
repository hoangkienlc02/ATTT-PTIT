#include<bits/stdc++.h>
using namespace std;
int n;
long long dp[1001];
void SoUgly(){
     dp[0]=1;
     int x=2,y=3,z=5,i2=0,i3=0,i5=0;
     for(int i=1;i<1001;i++){
          dp[i]=min(x,min(y,z));
          if(dp[i]==x) i2++,x=dp[i2]*2;
          if(dp[i]==y) i3++,y=dp[i3]*3;
         if(dp[i]==z) i5++,z=dp[i5]*5;
     }
}
int main(){
     int t; cin>>t;
     SoUgly();
     while(t--) {
          cin>>n;
          cout<<dp[n-1]<<endl;
    }
}
