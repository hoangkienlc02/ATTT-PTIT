#include<bits/stdc++.h>
using namespace std;
void initwsolve(){
   int n,k; cin>>n>>k;
   int res=0,a[n];
   for(int i=0;i<n;i++)cin>>a[i];
   for(int i=0;i<n;i++){
       if(a[i]==k)res++;
	}
   if(res>0)cout<<res<<endl;
   else cout<<-1<<endl;
}
int main(){
   int t; cin>>t;
   while(t--)initwsolve();
   return 0;
}
