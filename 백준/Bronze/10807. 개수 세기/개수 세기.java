

import java.util.*;
import java.lang.*;
import java.io.*;

public class Main
{
	public static void main (String[] args) throws java.lang.Exception
	{
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int cnt =0;
		int a[] = new int[n];
		for(int i=0;i<n;i++){
			a[i] = sc.nextInt();
		}
		int answer = sc.nextInt();
		for(int i=0;i<n;i++){
			if(a[i] == answer) cnt++;
		}
		System.out.println(cnt);
	}
	
}