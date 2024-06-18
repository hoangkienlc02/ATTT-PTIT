#include<bits/stdc++.h>
using namespace std;
int n,k;
void ChiaMangThanhHaiMangConCoTongLonNhat(){
   cin>>n>>k;
   long long a[n];
   for(int i=0;i<n;i++)cin>>a[i];
   sort(a,a+n);
   int mark=min(k,n-k);
   for(int i=1;i<n;i++) a[i]+=a[i-1];
   cout<<a[n-1]-2*a[mark-1]<<endl;
}
int main(){
    int t;cin>>t;
    while(t--) ChiaMangThanhHaiMangConCoTongLonNhat();
    return 0;
}
