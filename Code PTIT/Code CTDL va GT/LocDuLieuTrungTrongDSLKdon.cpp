#include<bits/stdc++.h>
using namespace std;
vector<int> res;
main(){
    int n;cin>>n;
    int f[100005];
    memset(f,0,sizeof(f));
    for(int i=1;i<=n;i++){
        int n;cin>>n;
        res.push_back(n);
        f[n]++;
    }
    for(int i=0;i<res.size();i++){
        if(f[res[i]]>0) {
        	cout<<res[i]<<" ";
        	f[res[i]]=0;
        }
	}
}

