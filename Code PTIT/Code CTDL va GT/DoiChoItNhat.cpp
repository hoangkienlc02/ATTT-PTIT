#include<bits/stdc++.h>
#define MAX 10005
using namespace std;
int n;
int a[MAX],b[MAX],check[MAX];
void xuli(){
   cin>>n;
   for(int i=0;i<n;i++){
       cin>>a[i]; b[i]=a[i];
   }
   sort(b,b+n);
   int res=0;
   for(int i=0;i<n;i++)
       if(a[i]!=b[i])
          for(int j=i+1;j<n;j++)
              if(a[j]==b[i]){
                 res++;
                 swap(a[i],a[j]);
                 break;
              }
   cout<<res<<endl;;
}
int main(){
   int t;cin>>t;
   while(t--) xuli();
}
