class Queue {
 
  private int count; //number of elements in the queue
  private int head;  //index of head element, -1 if queue is empty
  private int tail;  //index of tail element, -1 if queue is empty
  private int MAXSIZE = 10;  //Physical size of the queue. DO NOT CHANGE!
  private Record [ ] space; //circular array to store the elements of the queue
 
  //constructor
  Queue() {
	  tail = head = -1;
	  count = 0;
	  space = new Record[MAXSIZE];
 
  }
 
  //inspectors
  public boolean queueEmpty() {
		if (count == 0) {
			return true;
		}
		return false;
 
  }
 
  public int queueCount() {
		return count;
  }
 
  public Record queueFront() {
		if (head != -1) {
			return space[head];
		}
		return null;
 
  }
 
  public Record queueRear() {
		if (tail != -1) {
			return space[tail];
		}
		return null;
 
  }
 
  public String toString() {
	  String out = "< ";
	  int top = head;
	  for (int i = 0; i < count; i++) {
		  out = out + "("+ space[top].getShares() + "," + space[top].getPricePerShare()+")";
		  top = (top + 1) % MAXSIZE;
	  }
	  return out + " >";
  }
 
  //modifiers
  public boolean queueDequeue( ) {
	if (queueEmpty()) {
		return false;
	}
	else if (count == 1) {
		head=tail= -1;
		count = 0;
		return true;
	}
	head = (head+1)%MAXSIZE;
	count--;
	return true;
 
  }
 
  public void queueEnqueue(Record element) {

	if (count == MAXSIZE) {
		Record[] space2 = new Record[MAXSIZE*2];
		int next = head;
		for(int i = 0; i < MAXSIZE; i++)
		{
			space2[i] = space[next];
			next = (next+1)%MAXSIZE;
		}
		space = space2;
		tail = MAXSIZE-1;
		MAXSIZE=MAXSIZE*2;
		space[tail+1] = element;
		count++;
		tail++;
	}
	else {
		space[(tail+1)%MAXSIZE] = element;
		count++;
		tail = (tail+1) % MAXSIZE;
		if (count == 1) {
			head = tail;
		}
	}

  }

  public Queue queueCopy() {
		Queue temp = new Queue();
		int next = head;
		for (int i = 0; i < count; i++) {
			temp.queueEnqueue(space[next]);
			next = (next + 1)%MAXSIZE;
		}
		return temp;
  }
}
