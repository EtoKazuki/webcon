class Prefecture {
  int x;
  int y;
  String name;
  String [][] weather = new String [12][31];
  float [] air_pressure = new float [365];
  int [] year = new int [7];
  int [] month = new int [12];
  int [] day = new int [365];
   
  Prefecture() {
  }
 
  void setinfo(int _x, int _y, String _name) {
    x = _x;
    y = _y;
    name = _name;
  } 
}
