<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=no">
<title>Free Fire - Pro Shooter</title>
<style>
*{margin:0;padding:0;box-sizing:border-box}
body{background:#111;height:100vh;display:flex;justify-content:center;align-items:center;overflow:hidden;font-family:Arial;color:white}
#box{position:relative;width:700px;height:700px;max-width:98vw;max-height:98vh;border:3px solid #ffcc00;border-radius:15px;overflow:hidden;background:#1a2a1a;box-shadow:0 0 50px #ffcc00}
canvas{display:block}
#hud{position:absolute;top:0;left:0;width:100%;padding:10px;display:flex;justify-content:space-between;z-index:10;pointer-events:none;font-weight:900}
.hud-item{background:rgba(0,0,0,0.7);padding:6px 12px;border-radius:15px;border:1px solid #ffcc00;font-size:13px}
#menu{position:absolute;inset:0;background:linear-gradient(180deg, rgba(0,0,0,0.9), #1a1a00);display:flex;flex-direction:column;justify-content:center;align-items:center;z-index:20;text-align:center}
h1{font-size:45px;color:#ffcc00;text-shadow:0 0 20px #ffcc00}
.btn{margin-top:20px;padding:14px 45px;background:#ffcc00;color:#000;border:none;border-radius:30px;font-weight:900;font-size:18px;cursor:pointer;box-shadow:0 0 20px #ffcc00}
#joystick{position:absolute;bottom:20px;left:20px;width:100px;height:100px;background:rgba(255,255,255,0.1);border-radius:50%;border:2px solid rgba(255,255,255,0.3);z-index:15;display:none}
#stick{position:absolute;width:40px;height:40px;background:#ffcc00;border-radius:50%;left:30px;top:30px}
@media(max-width:700px){#joystick{display:block}}
</style>
</head>
<body>
<div id="box">
<div id="hud">
<div class="hud-item">🔫 AMMO: <span id="ammo">30</span></div>
<div class="hud-item">⭐ KILLS: <span id="score">0</span></div>
<div class="hud-item">❤️ HP: <span id="hp">100</span></div>
</div>
<canvas id="game" width="700" height="700"></canvas>
<div id="joystick"><div id="stick"></div></div>
<div id="menu">
<h1>FREE FIRE</h1>
<h2 style="color:#fff;margin:10px">MINI PRO</h2>
<p style="color:#ccc;font-size:13px;margin:10px">WASD = Run | Mouse = Aim<br>Left Click = Shoot | R = Reload</p>
<p style="color:#ffcc00;margin-top:10px">👨‍✈️ Person shooting with gun!</p>
<button class="btn" onclick="start()">▶️ PLAY NOW</button>
<p style="font-size:10px;color:#666;margin-top:15px">Pro Edition by Miss Tooba</p>
</div>
</div>

<script>
const canvas=document.getElementById('game'),ctx=canvas.getContext('2d');
let running=false,score=0,hp=100,ammo=30,level=1;
let player={x:350,y:350,w:22,h:22,angle:0,speed:4};
let bullets=[],enemies=[],drops=[];
let keys={},mouse={x:350,y:100};
let audioCtx;

function start(){
score=0;hp=100;ammo=30;level=1;bullets=[];enemies=[];drops=[];
document.getElementById('menu').style.display='none';
running=true;
loop(); spawnLoop();
}
function spawnLoop(){
if(!running) return;
let angle=Math.random()*Math.PI*2;
let dist=400;
enemies.push({x:350+Math.cos(angle)*dist,y:350+Math.sin(angle)*dist,hp:2+Math.floor(level/2),speed:1+level*0.2});
setTimeout(spawnLoop, 1200 - level*80);
}

canvas.addEventListener('mousemove',e=>{
let r=canvas.getBoundingClientRect();
mouse.x=(e.clientX-r.left)*(700/r.width);
mouse.y=(e.clientY-r.top)*(700/r.height);
player.angle=Math.atan2(mouse.y-player.y, mouse.x-player.x);
});
canvas.addEventListener('click',()=>{ if(running) shoot(); });
window.addEventListener('keydown',e=>{
keys[e.key.toLowerCase()]=true;
if(e.key.toLowerCase()=='r') reload();
});
window.addEventListener('keyup',e=>keys[e.key.toLowerCase()]=false);

function shoot(){
if(ammo<=0){playSound(100,0.3); return;}
ammo--;bullets.push({x:player.x,y:player.y,dx:Math.cos(player.angle)*12,dy:Math.sin(player.angle)*12,life:40});
playSound(900,0.07); createFlash();
document.getElementById('ammo').innerText=ammo;
}
function reload(){if(ammo<30){ammo=30;document.getElementById('ammo').innerText=ammo;playSound(300,0.4);}}
function createFlash(){drops.push({x:player.x+Math.cos(player.angle)*20,y:player.y+Math.sin(player.angle)*20,type:'flash',life:4});}

function playSound(f,d){
try{
if(!audioCtx) audioCtx=new (window.AudioContext||window.webkitAudioContext)();
let o=audioCtx.createOscillator(),g=audioCtx.createGain();
o.frequency.value=f;o.type='square';o.connect(g);g.connect(audioCtx.destination);
g.gain.setValueAtTime(0.2,audioCtx.currentTime);g.gain.exponentialRampToValueAtTime(0.01,audioCtx.currentTime+d);
o.start();o.stop(audioCtx.currentTime+d);
}catch(e){}
}

function loop(){
if(!running) return;
ctx.fillStyle='#2a3a2a';ctx.fillRect(0,0,700,700);
// Grass texture
ctx.fillStyle='rgba(0,0,0,0.1)';
for(let i=0;i<50;i++){ctx.fillRect(Math.random()*700,Math.random()*700,2,2);}

// Player move
if(keys['w']||keys['arrowup']) player.y-=player.speed;
if(keys['s']||keys['arrowdown']) player.y+=player.speed;
if(keys['a']||keys['arrowleft']) player.x-=player.speed;
if(keys['d']||keys['arrowright']) player.x+=player.speed;
player.x=Math.max(30,Math.min(670,player.x));
player.y=Math.max(30,Math.min(670,player.y));

// Draw Player - FREE FIRE PERSON
ctx.save();ctx.translate(player.x,player.y);ctx.rotate(player.angle);
// Body
ctx.fillStyle='#ffcc00';ctx.fillRect(-6,-10,12,20);
// Head
ctx.fillStyle='#ffdbac';ctx.beginPath();ctx.arc(0,-14,9,0,Math.PI*2);ctx.fill();
// Gun
ctx.fillStyle='#333';ctx.fillRect(8,-3,22,5);
ctx.fillStyle='#666';ctx.fillRect(28,-2,8,3);
ctx.restore();

// Bullets
for(let i=bullets.length-1;i>=0;i--){
let b=bullets[i];b.x+=b.dx;b.y+=b.dy;b.life--;
ctx.fillStyle='#ffff00';ctx.shadowColor='#ffcc00';ctx.shadowBlur=10;
ctx.beginPath();ctx.arc(b.x,b.y,4,0,Math.PI*2);ctx.fill();ctx.shadowBlur=0;
if(b.life<=0) bullets.splice(i,1);
}

// Enemies - like enemy players
for(let i=enemies.length-1;i>=0;i--){
let e=enemies[i];
let ang=Math.atan2(player.y-e.y, player.x-e.x);
e.x+=Math.cos(ang)*e.speed; e.y+=Math.sin(ang)*e.speed;

// Enemy person
ctx.save();ctx.translate(e.x,e.y);ctx.rotate(ang);
ctx.fillStyle='#ff0040';ctx.fillRect(-6,-10,12,20);
ctx.fillStyle='#fff';ctx.beginPath();ctx.arc(0,-14,8,0,Math.PI*2);ctx.fill();
ctx.fillStyle='#000';ctx.fillRect(5,-2,12,4);
ctx.restore();

// Hit by bullet
for(let j=bullets.length-1;j>=0;j--){
let b=bullets[j];
if(Math.hypot(b.x-e.x,b.y-e.y)<20){
e.hp--;bullets.splice(j,1);playSound(400,0.08);
if(e.hp<=0){enemies.splice(i,1);score++;drops.push({x:e.x,y:e.y,type:'blood',life:20});playSound(150,0.3);break;}
}
}
// Touch player
if(Math.hypot(player.x-e.x,player.y-e.y)<30){
hp-=0.6;enemies.splice(i,1);
if(hp<=0){gameOver();}
}
}

for(let i=drops.length-1;i>=0;i--){
let d=drops[i];d.life--;
if(d.type=='flash'){ctx.fillStyle=`rgba(255,255,0,${d.life/4})`;ctx.beginPath();ctx.arc(d.x,d.y,10,0,Math.PI*2);ctx.fill();}
if(d.type=='blood'){ctx.fillStyle=`rgba(255,0,0,${d.life/20})`;ctx.beginPath();ctx.arc(d.x,d.y,12,0,Math.PI*2);ctx.fill();}
if(d.life<=0) drops.splice(i,1);
}

document.getElementById('score').innerText=score;
document.getElementById('hp').innerText=Math.floor(hp);
level=Math.floor(score/5)+1;

requestAnimationFrame(loop);
}

function gameOver(){
running=false;
document.getElementById('menu').style.display='flex';
document.getElementById('menu').innerHTML=`<h1>GAME OVER</h1><h2 style="color:white;margin:10px">Kills: ${score}</h2><p>Level ${level} - You are Free Fire PRO! 🔥</p><button class="btn" onclick="start()">🔁 PLAY AGAIN</button>`;
}
</script>
</body>
</html>