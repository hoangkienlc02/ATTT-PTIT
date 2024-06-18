#include<bits/stdc++.h>
const int mod=1e9+7;
using namespace std;
int n,k;
void TinhPNK(){
     cin>>n>>k;
     long long res=1;
     if(k>n){cout<<0<<endl; return;}
     for(int i=n;i>=n-k+1;i--){
          res= (res%mod*i%mod)%mod;
	}
     cout<<res<<endl;
}
int main(){
     int t; cin>>t;
     while(t--) TinhPNK();
}
