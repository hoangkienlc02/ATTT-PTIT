#include<bits/stdc++.h>
using namespace std ;
int n ;

vector <int> a(11);
vector <vector <int> > res;
void DaySo2(){
    cin>>n; a.resize(n);res.clear() ;
    for(int i=0;i<a.size();i++) cin>>a[i]; res.push_back(a);
	while(a.size()>1){
        for(int i=0;i<a.size()-1;i++) a[i]=a[i]+a[i+1];
        a.pop_back();
        res.push_back(a);
	}
	for(int i=res.size()-1;i>=0;i--){
        cout<<'[';
        for(int j=0;j<res[i].size()-1;j++) cout<<res[i][j]<<' ';
        cout<<res[i].back()<<']'<<' ';
    }
    cout<<endl;
}
int main(){
    int t;cin>>t;
    while(t--) DaySo2();
    return 0;
}
