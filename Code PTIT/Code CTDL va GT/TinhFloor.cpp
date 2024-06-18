#include<bits/stdc++.h>
using namespace std;
void solve(){
   int n,x;
   cin>>n>>x;
   int a[n+1];
   int res=-1;
   for(int i=1;i<=n;i++) {
        cin>>a[i];
        if(a[i]<=x)res=i;
   	} 
	if(res==-1)cout<<"-1"<<endl;
   	else cout<<res<<endl;
}
int main(){
    int t;cin>>t;
    while(t--)solve();
    return 0;
}
