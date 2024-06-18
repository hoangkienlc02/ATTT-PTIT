#include<bits/stdc++.h>
using namespace std;
int n,k,a[11][11],check[11];
vector <int> b(11);
vector <vector<int> > v;
void checksum(){
  int sum=0;
  for(int i=1;i<=n;i++) sum+=a[i][b[i]];
  if(sum==k) v.push_back(b);
}
                            
void Try(int i){
     for(int j=1;j<=n;j++){
          if(check[j]==0){
                check[j]=1;
                b[i]=j;
                if(i==n) checksum();
                else Try(i+1);
                check[j]=0;
        }
	}
}
int main(){
    cin>>n>>k;
    for(int i=1;i<=n;i++)
        for(int j=1;j<=n;j++)
            cin>>a[i][j];
             Try(1);
cout<<v.size()<<endl;
      for(int i=0;i<v.size();i++){
         for(int j=1;j<=n;j++){
             cout<<v[i][j]<<' ';
        }cout<<endl;
	}
	return 0;
}

