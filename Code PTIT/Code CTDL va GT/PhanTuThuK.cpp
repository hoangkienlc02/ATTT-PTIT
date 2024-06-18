#include<bits/stdc++.h>
using namespace std;
void PhanTuThuK(){
   int n,m,k;
   cin>>n>>m>>k;
   int a[m+n];
   for(int i=0;i<n+m;i++) cin>>a[i];
   sort(a,a+m+n);
   cout<<a[k-1]<<endl;
}
int main(){
   int t;cin>>t;
   while(t--)PhanTuThuK();
   return 0;
}
