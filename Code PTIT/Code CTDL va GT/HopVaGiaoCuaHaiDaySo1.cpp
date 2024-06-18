#include <bits/stdc++.h>
using namespace std;
void hopVaGiaoCuaHaiDaySo1(){
	int n,m;
     cin>>n>>m;
     int a[100005],b[100005],dp1[100005],dp2[100005];
     for(int i=0;i<=100000;i++) {dp1[i]= 0;dp2[i]=0; }
     for(int i=0;i<n;i++){
          cin>>a[i]; dp1[a[i]]=1;
     }
     for(int i=0;i<m;i++){
          cin>>b[i]; dp2[b[i]]=1;
	}
     for(int i=0;i<=100000;i++)
          if(dp1[i]==1||dp2[i]==1) cout<<i<<' ';
     cout<<endl;
     for(int i=0;i<=100000;i++)
          if(dp1[i]==1&dp2[i]==1) cout<<i<<' ';
     cout<<endl;

}

int main(){
     int t;
     cin>>t;
     while(t--) hopVaGiaoCuaHaiDaySo1();
}
