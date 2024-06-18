#include<bits/stdc++.h>
using namespace std;
void initwsolve(){
   int n; cin>>n;
   int a[n],check[n];
   memset(check,0,sizeof(check));
   for(int i=0;i<n;i++) cin>>a[i];
   sort(a,a+n);
   int res=n,mid=n/2;
   for(int i=0;i<n/2&&mid<n;i++){
       while(mid<n){
          if(a[i]*2<=a[mid]){
         res-- ; mid++;
		  break;
		}else mid++;
	 }
	}
	cout<<res<<endl;
}
int main(){
	int t;cin>>t;
	while(t--)initwsolve();
	return 0;
}
