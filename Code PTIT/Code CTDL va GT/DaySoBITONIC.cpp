#include <bits/stdc++.h>
using namespace std;
int n,a[102],dpl[102],dpr[102];
string x,y,z;
void DaySoBITONIC(){
   cin>>n;
   for(int i=1;i<=n;i++) cin>>a[i];
   memset(dpl,0,sizeof(dpl));
   memset(dpr,0,sizeof(dpr));
   for(int i=1;i<=n;i++){
       for(int j=0;j<i;j++){
          if(a[j]<a[i])dpl[i]=max(dpl[i],dpl[j]+a[i]);
       }
	}
	for(int i=n+1;i>=1;i--){
	    for(int j=n+1;j>i;j--){
	        if(a[j]<a[i])dpr[i]=max(dpr[i],dpr[j]+a[i]);

		}
	}
	int res=0;
	for(int i=1;i<=n;i++){
	    res=max(res,dpl[i]+dpr[i]-a[i]);
	}cout<<res<<endl;
}
int main(){
	int t;cin>>t;
	while(t--) DaySoBITONIC();
	return 0;
}
