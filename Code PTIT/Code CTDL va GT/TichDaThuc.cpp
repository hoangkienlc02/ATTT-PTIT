#include<bits/stdc++.h>
using namespace std;
void TichDaThuc(){
   int m,n; cin>>m>>n;
   int p[m],q[n],r[m+n];//1
   memset(r,0,sizeof(r));
   for(int i=0;i<m;i++) cin>>p[i];
   for(int i=0;i<n;i++) cin>>q[i];
   for(int i=0;i<m;i++){//2
       for(int j=0;j<n;j++){
          r[i+j]+=p[i]*q[j];//3
 	  }
 	}
   for(int i=0;i<m+n-1;i++)cout<<r[i]<<' ';//1
   cout<<endl;
}
int main(){
   int t;cin>>t;
   while(t--)TichDaThuc();
   return 0;
}
