import java.util.*;
import java.util.Scanner;

 
public class Postfix{
	public static void main(String[] args){
		String str; //postfix expression to be read
		Stack<Integer> S = new Stack<Integer>(); //stack for evaluating the postfix expression
		System.out.print("Enter a postfix expression: ");
		Scanner scan = new Scanner(System.in);
		int answer = 0;
 
		//read in the string
		str = scan.next();
		System.out.println();
 
		//calculate the postfix expression
		for(int i = 0; i .0< str.length(); i++)
		{
			//seperate the string to operators and operands
			char a = str.charAt(i);
			String s = Character.toString(a);
			int one = 0;
			int two = 0;
			//if the char is operand, push into the stack
			if(Character.isDigit(a))
			{
				int p = Character.getNumericValue(a);;
				S.push(p);
				System.out.println(a + ":<" + S +">");
			}
			//if the char is operator, pop two operands and do the calculation
			else
			{
				one = S.pop();
				two = S.pop();
				if (a == '+') {
					int add = one + two;
					S.push(add);
					System.out.println(a + ":<" + S +">");
				}
				else if (a == '-') {
					int sub = one - two;
					S.push(sub);
					System.out.println(a + ":<" + S +">");
				}
				else if (a == '*') {
					int mul = one * two;
					S.push(mul);
					System.out.println(a + ":<" + S +">");
				}
				else if (a == '/') {
					double div = two / one;
					S.push((int) div);
					System.out.println(a + ":<" + S +">");
				}
			}
		}
 
		//print the result
		answer = S.pop();
		System.out.println();
		System.out.println("The value of the expression is: " + answer);
		//print out the result of the input expression
	}
}
 
