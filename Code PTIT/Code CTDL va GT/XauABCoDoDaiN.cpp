#include <bits/stdc++.h>
using namespace std;
void xauAbCoDoDaiN(){
    int n; cin>>n;
    string s;
    for(int i=0;i<n;i++) s[i]='A';
    for(int i=0;i<n;i++) {
    	cout<<s[i];
	}
	cout<<' ';
	for(int i=0;i<pow(2,n)-1;i++){
        int j=n;
        while(j--&&s[j]=='B') s[j]='A';
    	if(j>=0) s[j]='B';
      	for(int i=0;i<n;i++) {
		  cout<<s[i];
		}
		cout<<' ';
	}
		cout<<endl;
}
int main() {
       int t;cin>>t;
       while(t--) xauAbCoDoDaiN();
return 0;
}
