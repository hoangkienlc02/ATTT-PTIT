#include<bits/stdc++.h>
using namespace std;
int main(){
     int n;cin>>n;
     int a[n+1];
     vector <int> res;
     for(int i=0;i<n;i++) cin>>a[i];
     for(int i=0;i<n;i++) {
       cout<<"Buoc "<<i<<": ";
       res.push_back(a[i]);
       sort(res.begin(),res.end());

       for(int i=0;i<res.size();i++) cout<<res[i]<<' ';
       cout<<endl;
	}
     return 0;
}
