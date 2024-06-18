#include<bits/stdc++.h>
using namespace std;

void TimKiemNhiPhan(){
    int n,k;
    cin>>n>>k;
    int a[n+1];
    for(int i=1;i<=n;i++) cin>>a[i];
    int l=1,r=n,ok=0;
    while(l<=r){
        if(k==a[l]|| k==a[r]){
            if(k==a[l])cout<<l<<endl;
            if(k==a[r])cout<<r<<endl;
            ok=l; break;
        } 
		l++;r--;
	}
   if(ok==0)cout<<"NO"<<endl;
}
int main(){
   int t;cin>>t;
   while(t--)TimKiemNhiPhan();
   return 0;
}

