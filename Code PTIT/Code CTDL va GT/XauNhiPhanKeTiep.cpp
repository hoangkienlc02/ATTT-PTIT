#include <bits/stdc++.h>
using namespace std;
void sinh(){
    string s;cin>>s;
    int n=s.length() - 1;
	for(int a=n ; a>=0 ; a--){
		if(s[a]  == '0'){
			s[a] = '1' ;
			break ;
		}else{
			s[a] ='0' ;
		}
	}

    cout<<s<<endl;
}
int main() {
    int t;cin>>t;
    while(t--) {
    	sinh();
	}
	return 0;
}
