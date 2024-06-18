#include<bits/stdc++.h>
#include<stdlib.h>
#include<iostream>
#include<string>
using namespace std ;
int convert(string s){
	int res=0 ;
	for(int i=0 ; i<s.length() ; i++){
		res=10*res+s[i]-48 ;
	}
	return res ;
}
int main(){
    string a,b;
    cin>>a>>b;
  	int min=0,max=0;
   	for(int i=0;i<a.length();i++){
        if(a[i]=='6') a[i]='5';
	}
    for(int i=0;i<b.length();i++){
        if(b[i]=='6') b[i]='5';
	}
  	cout<<convert(a)+convert(b) <<" " ;
   	for(int i=0;i<a.length();i++){
        if(a[i]=='5') a[i]='6';
	}
    for(int i=0;i<b.length();i++){
        if(b[i]=='5') b[i]='6';
	}
  	cout<<convert(a)+convert(b)<<endl;
}
