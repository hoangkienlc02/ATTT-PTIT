#include<bits/stdc++.h>
using namespace std;
int n,a[10000];
void sapXepXemKe(){
   cin>>n;
   for(int i=0;i<n;i++)cin>>a[i];
   sort(a,a+n,greater<int>());
   int l=0,r=n-1;
   while(l<r){
       cout<<a[l]<<' '<<a[r]<<' ';
       l++;r--;
   }
   if(l==r) cout<<a[l];
   cout<<endl;

}
int main(){
   int t;cin>>t;
   while(t--) sapXepXemKe();
}
