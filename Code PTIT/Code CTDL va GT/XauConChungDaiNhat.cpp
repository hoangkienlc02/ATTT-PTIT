#include<iostream> 
#include<algorithm> 
using namespace std; 
int longestCommonSubset(string m, string n) { 
	int mLength = m.size(); 
	int nLength = n.size(); 
	int arr[mLength + 1][nLength + 1]; 
	for(int i = 0; i <= mLength; i++) { 
		for(int j = 0; j <= nLength; j++) { 
			if(i == 0 || j == 0) { 
				arr[i][j] = 0; 
			} 
			else if(m[i - 1] == n[j - 1]) { 
				arr[i][j] = 1 + arr[i - 1][j - 1]; 
			} 
			else if(m[i - 1] != n[j - 1]) { 
				arr[i][j] = max(arr[i - 1][j], arr[i][j - 1]); 
			} 
		}	 
	} 
	return arr[mLength][nLength]; 
} 
int main() { 
	int t; 
	cin >> t; 
	while(t--) { 
		string m, n; 
		cin >> m >> n; 
		cout << longestCommonSubset(m, n) << endl; 
	} 
}

