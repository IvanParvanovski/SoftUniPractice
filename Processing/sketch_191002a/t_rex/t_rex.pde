    dino d = new dino();
    pillar[] p = new pillar[3];
    boolean end=false;
    boolean intro=true;
    int score=0;
    
    void setup(){
    size(500,500);
    }
    
       void draw(){
      background(0);
      if(end){
      d.move();
      }
      d.drawDino();
      if(end){
      d.drag();
      }
       
      fill(0);
      stroke(255);
      textSize(32);
      if(end){
      rect(20,20,100,50);
      fill(255);
      text(score,30,58);
      }else{
      rect(150,100,200,50);
      rect(150,200,200,50);
      fill(255);
      if(intro){
        text("Dino Code",155,140);
        text("Click to Play",155,240);
      }else{
      text("game over",170,140);
      text("score",180,240);
      text(score,280,240);
      }
      }
    }
    
    class dino{
     float yDino = 225;
     float xDino = 100;
     float ySpeed = 0;
     
     void checkCollisions(){
     if(yDino>500){
      end=false;
     }
    }
    
     void jump(){
       ySpeed += 10;
    }
    
    void drag(){ 
     ySpeed += 0.4;
    }
    
    void move(){
     yDino+=ySpeed; 
     for(int i = 0;i<3;i++){
      p[i].xDino-=3;
     }

    }
     
     void drawDino(){
     ellipse(xDino,yDino,10,10);
     }
    }
    
    
    class pillar{
      boolean crashed = false;
      float xDino;
      
    float pilX1 = random(50);
    float pilY1 = 50;
    float pilY2 = 50;
    
    void drawPillar(){
    line(pilX1,pilY1,pilX1,pilY2);
    
    if (xDino > pilX1 && crashed == false){
    crashed = true;
    score++;
    }
     }
    }
    
    void reset(){
     end=true;
     score=0;
     d.yDino=400;
    
    }

    
    void mousePressed(){
     d.jump();
     intro=false;
     if(end==false){
       reset();
     }
    }
    void keyPressed(){
     d.jump(); 
     intro=false;
     if(end==false){
       reset();
     }
    }
    

     
