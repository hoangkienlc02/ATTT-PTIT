#include <bits/stdc++.h>
using namespace std;
void boSungPhanTu(){
     int n;cin>>n;
     int a[n],count=1;
     for(int i=0;i<n;i++)cin>>a[i];
     sort(a,a+n);
     for(int i=1;i<n;i++)
       if(a[i]!=a[i-1])count++;
   cout<<a[n-1]-a[0]-count+1 <<endl;
}
int main() {
     int t;cin>>t;
     while(t--) boSungPhanTu();
return 0;
}
