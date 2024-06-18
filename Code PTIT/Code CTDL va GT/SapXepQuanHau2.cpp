#include <bits/stdc++.h>
using namespace std;
int n,res,sum,a[ 10][10],hang[21],cot[21],xuoi[21],nguoc[21];
void Try (int i,int sum){//1
for(int j=1;j<=8;j++){
/*2*/ if(!hang[j]&&!cot[j]&&!xuoi[i-j+8]&&!nguoc[i+j-1]){
        sum+=a[i][j];
        hang[j]=cot[j]=xuoi[i-j+8]=nguoc[i+j-1]=1;
        if(i==8) res=max(res,sum);//3
        else Try(i+1,sum);
        sum-=a[i][j];
        hang[j]=cot[j]=xuoi[i-j+8]=nguoc[i+j-1]=0;
		}
	}
}
int main() {
int t;cin>>t;
while(t--){
    res=0;
	for(int i=1;i<=8;i++)
        for(int j=1;j<=8;j++)
            cin>>a[i][j];
    Try(1,0);//1
    cout<<res<<endl;
}
return 0;
}

