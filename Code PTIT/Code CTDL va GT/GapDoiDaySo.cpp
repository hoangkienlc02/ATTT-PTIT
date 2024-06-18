#include<bits/stdc++.h>
const int mod=1e9+7;
using namespace std;
long long n,k;
long long gapdoi(long long n,long long k){
    //if(k==1) return 1 ;
    if(k==pow(2,n)) return n+1 ;
	if(k<=pow(2,n))return gapdoi(n-1,k);
    return gapdoi(n-1,k-pow(2,n));
}
void solve(){
   cin>>n>>k;
   cout<<gapdoi(n-1,k)<<endl;
}
int main(){
   int t;cin>>t;
   while(t--)solve();
   return 0;
}
