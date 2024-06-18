#include <bits/stdc++.h>
using namespace std;
int n,a[11];
void out(){
  	for(int i=1;i<=n;i++) {
  		cout<<a[i];
	}
	cout<<' ';
}
void SinhHoanVi(){
  	cin>>n;
  	for(int i=1;i<=n;i++) {
  		a[i]=i; 
	}
	out() ;
  	while(1){
    	int i=n ,j=n;
    	while(a[i]<a[i-1]&&i>0) {
    		i--;
		} 
		i--;
    	if(i==0) break;
		else {
       		while(a[j]<a[i]) j--;
       		swap(a[i],a[j]);
       		sort(a+i+1,a+n+1);
       		out();
    		
		}
	
	}
	cout<<endl ;
}
int main() {
    int t;cin>>t;
    while(t--){
    	SinhHoanVi();
	}
	return 0;
}

