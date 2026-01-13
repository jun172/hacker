// particles.js
const canvas = document.getElementById('hero-canvas');
const ctx = canvas.getContext('2d');
canvas.width = window.innerWidth;
canvas.height = window.innerHeight;

const particles = [];
const particleCount = 80;

for(let i=0;i<particleCount;i++){
    particles.push({
        x: Math.random()*canvas.width,
        y: Math.random()*canvas.height,
        r: Math.random()*3 + 1,
        dx: (Math.random()-0.5)*0.5,
        dy: (Math.random()-0.5)*0.5
    });
}

function animate(){
    ctx.clearRect(0,0,canvas.width,canvas.height);
    for(let i=0;i<particles.length;i++){
        let p = particles[i];
        ctx.beginPath();
        ctx.arc(p.x,p.y,p.r,0,Math.PI*2);
        ctx.fillStyle = 'rgba(255,255,255,0.7)';
        ctx.fill();
        p.x += p.dx;
        p.y += p.dy;

        if(p.x < 0 || p.x > canvas.width) p.dx *= -1;
        if(p.y < 0 || p.y > canvas.height) p.dy *= -1;
    }
    requestAnimationFrame(animate);
}

animate();

window.addEventListener('resize',()=>{
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;
});
