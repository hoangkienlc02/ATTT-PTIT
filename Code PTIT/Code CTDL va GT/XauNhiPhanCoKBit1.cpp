#include<bits/stdc++.h>
int n,k,a[17];
using namespace std;
void check(){
    int count=0;
    for(int i=1;i<=n;i++) if(a[i]==1) count++;
    if(count==k){
     	for(int i=1;i<=n;i++) cout<<a[i];cout<<endl;
	}
}
void Try(int i){
 	for(int j=0;j<=1;j++){
    	a[i]=j;
    	if(i==n) check();
    	else Try(i+1);
	}
}
int main(){
    int t;cin>>t;
    while(t--){
    	cin>>n>>k;
    	Try(1);
	}
    return 0;

}

