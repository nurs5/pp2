#include <iostream>
#include <string>
using namespace std;
string a(string s1,string s2)
{   int i=0;
 if (s1.length()>s2.length())
     return s1;
 if (s2.length()>s1.length())
     return s2; 
 while(true)
 {
     if(s1[i]>s2[i])
     {
         return s1;
     return 0;
     }
     if(s1[i]<s2[i])
     {
         return s2;
     return 0;
     }
     i++;
     
     }
     return s1;
   
}
int main()
{
    string s1,s2,s3;
    cin>>s1>>s2>>s3;
    cout<<a(s1,a(s2,s3));
    
}