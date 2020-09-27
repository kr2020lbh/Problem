import java.util.Scanner;
import java.io.FileInputStream;

public class 지그재그숫자_1986 
{

	public static void main(String[] args) 
	{
		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt();
		for (int t=1;t<=T;t++) 
		{
			int num = sc.nextInt();
			int sum = 0;
			for (int i=1;i<=num;i++) 
			{
				if (i%2==1) {sum+=i;}
				else {sum+=-i;}
			}
			System.out.println("#"+t+" "+sum);
		}	
	}
}
