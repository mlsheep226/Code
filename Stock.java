import java.util.Scanner;
 
class Stock {
 
  	public static void main(String args[]) {
	Queue one = new Queue();
    	Scanner scan = new Scanner(System.in);
 
    	//read the option
	int choice = 0;

 
	int totalShares, totalValue;
	int shares, price;//save the shares and price each time
	totalShares = 0;//save the total shares
	totalValue = 0;//save the total shares value
 
	//process the option
	while(choice != 3)
	{
		System.out.print("Enter option (1:buy, 2:sell, 3:quit): ");
		choice = scan.nextInt();
		//buy
		if(choice == 1)
		{
			System.out.print("Enter shares to buy and price per shares: ");
			shares = scan.nextInt();
			price = scan.nextInt();

			totalShares += shares;
			totalValue += (shares * price);
			Record buy = new Record(shares, price);
			one.queueEnqueue(buy);
			System.out.println("Queue: " + one.toString());
			System.out.printf("Total Shares: %d\n", totalShares);
			System.out.printf("Total Shares Value: $%d\n", totalValue);
		        System.out.println();	
 
		}
		else if(choice == 2)
		{
			System.out.print("Enter shares to sell and selling price per share: ");
			shares = scan.nextInt();
			price = scan.nextInt();
			int totalSell = price * shares;
			int value = 0;
			Record t;
			int shares2 = 0;
			int price2 = 0;
			int loss;
			boolean k = false;
			if (shares <= totalShares) {
				totalShares -= shares;
				while (shares > 0) {
						t = one.queueFront();	
						price2 = t.getPricePerShare();
						shares2 = t.getShares();
						if (shares2 < shares) {
							k = one.queueDequeue();
							if (k == true) {
								value += shares2 * price2;
								loss = shares2 * price2;
								shares -= shares2;
								totalValue -= loss;
							}
						}
						else if (shares2 == shares){
							k = one.queueDequeue();
							if (k == true) {
								loss = shares * price2;
								value += shares * price2;
								totalValue -= loss;
								shares -= shares2;
							}		
						}	
						else if (shares2 > shares) {
							loss = price2 * shares;
							value += price2 * shares;
							totalValue -= loss;
							t.setShares(shares2 - shares);
							shares = 0;
						}
				}
				if (one.queueEmpty()) {
					totalShares = 0;
					totalValue = 0;
				}
				System.out.printf("Profit made: $%d\n", totalSell - value);
				System.out.println("Queue: " + one.toString());
				System.out.printf("Total Shares: %d\n", totalShares);
				System.out.printf("Total Shares Value: $%d\n", totalValue);		
				System.out.println();
			}
			else {
				System.out.println("Not enough shares to sell, please buy more or sell less.");
			}
		}
 
		//quit
		else if(choice == 3)
		{
			System.out.println("Selling Done, Goodbye.");
			System.exit(0);
		}
	}
    }
}

