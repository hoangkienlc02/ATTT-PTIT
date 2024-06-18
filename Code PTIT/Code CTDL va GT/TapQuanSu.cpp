#include <bits/stdc++.h>
using namespace std;
void TapQuanSu(){
     int n,k; cin>>n>>k;
     int a[k+1],b[k+1],i=k;
     for(int i=1;i<=k;i++) cin>>a[i],b[i]=a[i];
     while(a[i]==n-k+i&&i>0) i--;
	if(i==0) cout<<k<<endl;
     else {
        a[i]++;
        for(int j=i+1;j<=k;j++) a[j]=a[j-1]+1;
        int count=0;
        for(int i=1;i<=k;i++){
       		for(int j=1;j<=k;j++){
         		if(a[i]==b[j]) {count++;break;}
         	}
     	}
            cout<<k-count<<endl;
	}
}
int main() {
     int t;/**/cin>>t;
     while(t--) TapQuanSu();
return 0;
}
