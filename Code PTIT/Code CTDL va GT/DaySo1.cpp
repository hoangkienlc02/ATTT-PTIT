#include<bits/stdc++.h>
using namespace std;
int n;
vector <int> a(11);
void out(){
    cout<<'[';
    for(int i=0;i<a.size()-1;i++) cout<<a[i]<<' ';
    cout<<a[a.size()-1]<<']'<<endl;
}
void DaySo1(){
    cin>>n; a.resize(n) ;
    for(int i=0;i<a.size();i++) cin>>a[i]; out();
	while(a.size()>1){
        for(int i=0;i<a.size()-1;i++) a[i]=a[i]+a[i+1];
        a.pop_back();
        out();
	}
}
int main(){
    int t;cin>>t;
    while(t--) DaySo1();
    return 0;
}
