#include<bits/stdc++.h>
using namespace std;
void initwsolve(){
    int n,s,m;
    cin>>n>>s>>m;
    int res=0,need=s*m;
    for(int i=1;i<=s;i++){
        if(i%7==0)continue;
        else {
            res++;
            if(res*n>=need){
                cout<<res<<endl;return;
        	}
    	}
	}
    cout<<-1<<endl;
}
int main(){
   int t;cin>>t;
   while(t--)initwsolve();
}
