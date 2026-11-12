html_code = """<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>For Sahar - Special Surprise</title>
<style>
body { margin:0; height:100vh; background: radial-gradient(circle at top, #ff9a9e, #fecfef, #667eea); overflow:hidden; display:flex; justify-content:center; align-items:center; font-family:Arial; }
.container { text-align:center; z-index:10; }
h1 { font-size:45px; color:white; text-shadow: 0 0 20px #ff4d6d; animation: glow 2s infinite alternate; margin:0; }
@keyframes glow { from { transform:scale(1); } to { transform:scale(1.05); } }
.name { font-size:60px; font-weight:bold; color:white; animation: bounce 1.5s infinite; margin:10px 0; }
@keyframes bounce { 0%,100%{transform:translateY(0)} 50%{transform:translateY(-15px)} }
.msg { color:white; font-size:20px; margin-top:15px; background: rgba(255,255,255,0.25); padding:15px 25px; border-radius:30px; backdrop-filter:blur(10px); }
.hearts { position:absolute; width:100%; height:100%; top:0; left:0; pointer-events:none; }
.heart { position:absolute; color:#ff4d6d; font-size:20px; animation: fall linear infinite; }
@keyframes fall { 0%{ transform:translateY(-10vh); opacity:1} 100%{ transform:translateY(110vh); opacity:0} }
.btn { margin-top:20px; padding:12px 30px; border:none; border-radius:25px; background:white; color:#ff4d6d; font-size:18px; font-weight:bold; cursor:pointer; }
.btn:hover { transform:scale(1.1); background:#ff4d6d; color:white; }
</style>
</head>
<body>
<div class="hearts" id="hearts"></div>
<div class="container">
<h1>Special For</h1>
<div class="name">SAHAR 💖</div>
<div class="msg" id="msg">
There are a thousand people in my path, and in my eyes only you! 🌸<br>
Tum ho to sb hseen hai! 😊<br>
My sweet memory your message! 🤗
My biggest sadness your absence! <br>
</div>
<button class="btn" onclick="celebrate()">Click here dear jan! 🎉</button>
<p style="color:white; margin-top:15px; font-size:14px;">From: Your Best Friend (Miss Tooba) 💌</p>
</div>
<script>
function createHeart(){
  const h=document.createElement('div');
  h.className='heart';
  h.innerHTML='❤️';
  h.style.left=Math.random()*100+'vw';
  h.style.animationDuration=(Math.random()*3+2)+'s';
  h.style.fontSize=(Math.random()*20+15)+'px';
  document.getElementById('hearts').appendChild(h);
  setTimeout(()=>h.remove(),5000);
}
setInterval(createHeart,150);
function celebrate(){
  for(let i=0;i<50;i++){ setTimeout(createHeart, i*30); }
  let msg=document.getElementById('msg');
  msg.innerHTML="meri pasandida dost! 🥳💖<br>i always miss our golden days together !<br>Love You Sahar! 💕";
  msg.style.background="#ff4d6d";
}
</script>
</body>
</html>
"""

with open("For_Sahar.html", "w", encoding="utf-8") as f:
    f.write(html_code)

print("Done! For_Sahar.html ban gaya - ab isko open karo")