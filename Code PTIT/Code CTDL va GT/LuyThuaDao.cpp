#include<bits/stdc++.h>
const int mod=1e9+7;
using namespace std;
long long n;
long long luythua(long long n,long long k){
   if(k==0) return 1;
   if(k==1) return n%mod;
   long long temp=luythua(n,k/2);
   if(k%2==0) return temp*temp%mod;
   else return temp*temp%mod*n%mod;
}
void solve(){
    cin>>n;
    long long m=n,r=0;
    while(m){
        r=r*10+m%10;
        m/=10;
	}
    cout<<luythua(n,r)<<endl;
}
int main(){
   int t;cin>>t;
   while(t--)solve();
   return 0;
}
