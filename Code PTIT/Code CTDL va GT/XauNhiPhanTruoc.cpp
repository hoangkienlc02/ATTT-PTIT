#include<bits/stdc++.h>
using namespace std;
void XauNhiPhanTruoc(){
    string s;
    cin>>s;
    int n=s.length();
    while(n--){
        if(s[n]=='1'){
            s[n]='0';
        	break;
    	}
        else s[n]='1';
    }
    cout<<s<<endl;
}
int main(){
	int n ;
	cin>>n ;
	while(n--) XauNhiPhanTruoc() ;
	return 0;
}
