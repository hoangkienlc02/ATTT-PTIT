#include <bits/stdc++.h>
using namespace std;
void capSoTongBangK(){
     int n,k;
	 cin>>n>>k;
     int a[n];
     int count=0;
     for(int i=0;i<n;i++) cin>>a[i];
     for(int i=0;i<n-1;i++)
          for(int j=i+1;j<n;j++)
                if (a[j]==k-a[i]) count++;
     cout<<count<<endl;
}
int main() {
     int t;cin>>t;
     while(t--) capSoTongBangK();
return 0;
}
