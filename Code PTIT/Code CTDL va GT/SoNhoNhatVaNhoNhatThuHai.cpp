#include <bits/stdc++.h>
using namespace std;
void TimKiemTrongDaySapXepVong(){
     int n;cin>>n;
     int a[n],res=-1;
     for(int i=0;i<n;i++)cin>>a[i];
     sort(a,a+n);
     for(int i=1;i<n;i++)
       if(a[i]!=a[i-1]){res=a[i];break;}
     if(res==-1)cout<<-1<<endl;
     else cout<<a[0]<<' '<<res<<endl;
}
int main() {
     int t;cin>>t;
     while(t--) TimKiemTrongDaySapXepVong();
	return 0;
}
