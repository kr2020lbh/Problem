import java.util.Scanner;
public class 시험성적_9498 {

	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		int N = scanner.nextInt();
		
		if (N>=90) {
			System.out.println("A");
		}
		else if(N>=80) {
			System.out.println("B");
		}
		else if(N>=70) {
			System.out.println("C");
		}
		else if(N>=60) {
			System.out.println("D");
		}
		else {
			System.out.println("F");
		}
	}	
}
