class Record {
 
  private int shares;
  private int pricePerShare;
 
  //constructor
  Record(int sharesNewValue, int pricePerShareNewValue) {
    shares = sharesNewValue;
    pricePerShare = pricePerShareNewValue;
  }
 
  //inspectors
  public int getShares() {
    return shares;
  }
 
  public int getPricePerShare() {
    return pricePerShare;
  }
  
  //modifiers
  public void setShares(int sharesNewValue) {
    shares = sharesNewValue;
  }
 
  public void setPricePerShare(int pricePerShareNewValue) {
    pricePerShare = pricePerShareNewValue;
  }
 
}