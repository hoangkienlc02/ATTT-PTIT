#include <bits/stdc++.h>
using namespace std;
void tapConKeTiep(){ //duyet nguoc tim phan tu dau tien khac (n-k+i) , neu i=0 --> in to hop dau tien
    int n,k; cin>>n>>k;
    int a[k+1],i=k;
    for(int i=1;i<=k;i++) cin>>a[i];
	while(a[i]==n-k+i&&i>0) i--; 
	if(i==0) {
		for(int i=1;i<=k;i++){
			a[i]=i;
		} 
	}
    else {
		a[i]++;
        for(int j=i+1;j<=k;j++) {
        	a[j]=a[j-1]+1;
		}
    }
    for(int i=1;i<=k;i++) {
		cout<<a[i]<<' ';
	}
    cout<<endl;
}
int main() {
    int t;cin>>t;
    while(t--) tapConKeTiep();
	return 0;
}
