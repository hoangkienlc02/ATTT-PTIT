#include<bits/stdc++.h>
using namespace std;

int n;
void SapXepThamLam(){
   cin>>n;
   int a[n],b[n];
   for(int i=0;i<n;i++){cin>>a[i]; b[i]=a[i];}
   sort(b,b+n);
   for(int i=0;i<n;i++){
        if((a[i]!=b[i]&&a[n-i-1]!=b[i])){
          	cout<<"No"<<endl;
          	return;
    	}
    }
    cout<<"Yes"<<endl;
}
int main(){
    int t;cin>>t;
    while(t--) SapXepThamLam();
    return 0;
}
 
