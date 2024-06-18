#include <bits/stdc++.h>
using namespace std;
void initwsolve(){
     int n;cin>>n;
   int a[n];
   for(int i=0;i<n;i++)cin>>a[i];
   int res=1e9+7;
   for(int i=0;i<n-1;i++){
      for(int j=i+1;j<n;j++){
          if(abs(a[j]+a[i])<abs(res))res=a[j]+a[i];
    	}
	}
   cout<<res<<endl;
}
int main() {
     int t;cin>>t;
     while(t--) initwsolve();
     return 0;
}
