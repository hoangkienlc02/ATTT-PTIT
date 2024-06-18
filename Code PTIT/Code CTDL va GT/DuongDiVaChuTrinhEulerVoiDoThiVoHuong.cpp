#include<bits/stdc++.h>
using namespace std;
vector< vector<int> > a;
int V,E,x,y;
void DuongDiVaChuTrinhEulerVoiDoThiVoHuong(){
     a.clear();
     cin>>V>>E;
     a.resize(1005);
     for(int i=1;i<=E;i++){
          cin>>x>>y;
          a[x].push_back(y);
          a[y].push_back(x);
     }
     int odd=0 ;
     for(int i=1;i<=V;i++)
          if(a[i].size()%2!=0) odd++;
     if(odd==0) cout<<"2\n";
     else if(odd==2) cout<<"1\n";
     else cout<<"0\n";
}
int main(){
     int t; cin>>t;
     while(t--)DuongDiVaChuTrinhEulerVoiDoThiVoHuong();
     return 0;
}
