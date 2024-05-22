/* package whatever; // don't place package name! */

import java.util.*;
import java.lang.*;
import java.io.*;

/* Name of the class has to be "Main" only if the class is public. */
public class Main
{
	public static void main (String[] args) throws java.lang.Exception
	{
		Scanner sc = new Scanner(System.in);
		String s = sc.next();
		int n = sc.nextInt();
		int tmp = 1;
		int sum =0;
		int length = s.length();
		for(int i=length;i>0;i--){
			char a = s.charAt(i-1);
			if(a >= 'A' && a <= 'Z'){
				sum += (a-'A'+10)*tmp;
			}else{
				sum += (a-'0')*tmp;
			}
			tmp *= n;
		}
		System.out.println(sum);
	}
}