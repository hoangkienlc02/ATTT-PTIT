#include<bits/stdc++.h>
using namespace std;
vector<string> res;
main(){
     int n;cin>>n;
     for(int i=1;i<=n;i++){
          string s;cin>>s;
          res.push_back(s);
     }
     string k;cin>>k;
     for(int i=0;i<res.size();i++)
          if(res[i]!=k) cout<<res[i]<<" ";
}
