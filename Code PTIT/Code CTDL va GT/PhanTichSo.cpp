#include<bits/stdc++.h>
using namespace std;
int n,a[11];
void out(int n){
  cout<<"(";
  for(int i=1;i<n;i++) cout<<a[i]<<' ';
  cout<<a[n]<<") ";
}
void PhanTichSo(int i,int sumcur,int k){
  for(int j=k;j>=1;j--){
    if(sumcur+j<=n){
       a[i]=j;
       sumcur+=j;
       if(sumcur==n) out(i);
       else PhanTichSo(i+1,sumcur,j);
       sumcur-=j;
    }
   }
}
int main(){
     int t;cin>>t;
     while(t--){
    cin>>n;
    PhanTichSo(1,0,n);
    cout<<endl;
	}
     return 0;
}
