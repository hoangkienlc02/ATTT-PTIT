#include<bits/stdc++.h>
using namespace std;
void DoiChoCacChuSo(){
   int k;cin>>k;
   string s;cin>>s;
   for(int i=0;i<k&&i<s.length();i++){
       int max=i,j=s.length();
       while (j-->i) {if (s[j]>s[max]) max=j;}
  		if(max!=i) swap(s[i],s[max]);
       else k++;
   }
   cout<<s<<endl;
}
int main(){
	int t;cin>>t;
	while(t--) DoiChoCacChuSo();
	return 0;
}
