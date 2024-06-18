#include <bits/stdc++.h>
using namespace std;
int n,k,a[15];
void sinhToHop(){
    cin>>n>>k;
    for(int i=1;i<=k;i++) {
    	a[i]=i;
	}
    for(int i=1;i<=k;i++) {
    	cout<<a[i]; cout<<' ';
	}
	while(1){
    	int i=k;
    	while(a[i]==n-k+i&&i>0) i--;
    	if(i==0) {
    		break;
		}
    	else{
       		a[i]++;
       		for(int j=i+1;j<=k;j++) a[j]=a[j-1]+1;
       		for(int i=1;i<=k;i++) cout<<a[i]; cout<<' ';
    	}
	}
    cout<<endl;
}
int main() {
    int t;cin>>t;
    while(t--)sinhToHop();
	return 0;
}
