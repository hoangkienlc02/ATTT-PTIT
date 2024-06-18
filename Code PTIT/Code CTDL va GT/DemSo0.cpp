#include<bits/stdc++.h>
using namespace std;
void DemSo0(){
   int n;
   cin>>n;
   int a[n];
   int res=0;
   for(int i=0;i<n;i++) {
       cin>>a[i];
       if(a[i]==0) res++;
   }
   cout<<res<<endl;
}
int main(){
   int t;cin>>t;
   while(t--)DemSo0();
   return 0;
}

