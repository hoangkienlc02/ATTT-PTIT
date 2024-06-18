#include<bits/stdc++.h>
const int mod=123456789;
using namespace std;
long long n,k;
long long luythua(long long n,long long k){
   if(k==0) return 1;
   if(k==1) return n%mod;
   long long temp=luythua(n,k/2);
   if(k%2==0) return temp*temp %mod;
   else return temp*temp%mod*n%mod;
}
void solve(){
    cin>>n;
	if(n==1) cout<<1<<endl;
    else cout<<luythua(2,n-1)<<endl;
}
int main(){
    int t;cin>>t;
    while(t--)solve();
    return 0;
}
