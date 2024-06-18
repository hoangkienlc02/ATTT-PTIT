#include<bits/stdc++.h>
using namespace std;
void out(int *a,int n){
   for(int i=0;i<n;i++) cout<<a[i]<<' ';
   cout<<endl;
}
int main(){
    int n;cin>>n;
    int a[n+1];
    for(int i=0;i<n;i++) cin>>a[i];
    for(int i=0;i<n-1;i++) {
       int ok=0;
      	for(int j=1;j<n;j++){
          	if(a[j]<a[j-1]){
              	ok=1;swap(a[j],a[j-1]);
        	}
    	}
       	if(ok==1) cout<<"Buoc "<<i+1<<": ",out(a,n);

       else break;
     }
     return 0;
}
