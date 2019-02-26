import de.bezier.data.sql.*;
PImage mapImage;
SQLite db;
Prefecture [] prefs = new Prefecture [47];
PImage fine;
PImage cloudy;
PImage rain;
PImage snow;
int change_month = 0;
int change_day = 0;

void setup() {
  db = new SQLite( this, "weather.db" ); // open DB file 
  size(700, 755);
  //天気のアイコンを読み込む
  mapImage = loadImage("japan_map.gif");
  fine = loadImage("fine.png");
  cloudy = loadImage("cloudy.png");
  rain = loadImage("rain.png");
  snow = loadImage("snow.png");
  for (int i=0; i<47; i++) {
    prefs[i] = new Prefecture();
  }
//都道府県データを配列に格納
  if ( db.connect() ) {
    String sql = "select x, y, name from prefecture_table";
    db.query(sql);
    int j=0;
    while (db.next()) {
      prefs[j].setinfo(db.getInt("x"), db.getInt("y"), db.getString("name"));
      j++;
      if (j==47) break;
    }

//天気情報を配列に格納
    int i=0;
    int day=0;
    int month=0;
    sql = "select name, weather, year, month, day "+
      "from weather_table, prefecture_table "+
      "where weather_table.prefecture_id = prefecture_table.id and year=2009";
    db.query(sql);
    while (db.next()) {
      month = db.getInt("month");
      day = db.getInt("day");
      if (db.getString("name").equals(prefs[i].name) == false) {
        i++;
      }
          prefs[i].weather[month-1][day-1] = db.getString("weather");
    }
  }
}

void draw() {
  image(mapImage, 0, 0);
  put_image();
}

//アイコンの表示を行う関数
void put_image() {
  for (int i=0; i<47; i++) {
    if (prefs[i].weather[change_month][change_day] == null) {
      fill(0);
      text("no data", prefs[i].x, prefs[i].y);
    } else if (prefs[i].weather[change_month][change_day].equals("Fine") == true) {
      fine.resize(0, 20);
      image(fine, prefs[i].x-10, prefs[i].y-10);
    } else if (prefs[i].weather[change_month][change_day].equals("Cloudy") == true) {
      cloudy.resize(0, 20);
      image(cloudy, prefs[i].x-10, prefs[i].y-10);
    } else if (prefs[i].weather[change_month][change_day].equals("Rain") == true) {
      rain.resize(0, 20);
      image(rain, prefs[i].x-10, prefs[i].y-10);
    } else {
      snow.resize(0, 20);
      image(snow, prefs[i].x, prefs[i].y);
    }
  }
  fill(0);
  text(change_month+1+"月"+(1+change_day)+"日", 50, 50);
}

//日付変更の処理
void keyPressed() {  
  if (keyCode == LEFT) {
    change_month--;
    if (change_day>29 && (change_month==3|change_month==5 |change_month==8 |change_month==10)) {
      change_day = 0;
    } else if (change_day>27 && change_month==1) {
      change_day=0;
    }
    if (change_month<0) change_month=11;
  } else if (keyCode == RIGHT) {
    change_month++;
    if (change_day>29 && (change_month==3|change_month==5 |change_month==8 |change_month==10)) {
      change_day = 0;
    } else if (change_day>27 && change_month==1) {
      change_day=0;
    }
    if (change_day>29 && (change_month==3|change_month==5 |change_month==8 |change_month==10)) {
      change_day = 0;
    } else if (change_day>27 && change_month==1) {
      change_day=0;
    }
    if (change_month > 11) change_month=0;
  } else if (keyCode == UP) {
    change_day++;
    if (change_day>30 && (change_month==0|change_month==2 |change_month==4 |change_month==6|change_month==7|change_month==9|change_month==11)) {
      change_day = 0;
    } else if (change_day>29 && (change_month==3|change_month==5 |change_month==8 |change_month==10)) {
      change_day = 0;
    } else if (change_day>27 && change_month==1) {
      change_day=0;
    }
  } else if (keyCode == DOWN) {
    change_day--;
    if (change_day<0 && (change_month==0|change_month==2 |change_month==4 |change_month==6|change_month==7|change_month==9|change_month==11)) {
      change_day = 30;
    } else if (change_day<0 && (change_month==3|change_month==5 |change_month==8 |change_month==10)) {
      change_day = 29;
    } else if (change_day<0 && change_month==1) {
      change_day=27;
    }
  }
  
}
