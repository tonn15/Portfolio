// Animation des vecteurs sur le canvas
const canvas = document.getElementById('vectorCanvas');
const ctx = canvas.getContext('2d');
let width, height;

function resizeCanvas() {
    width = window.innerWidth;
    height = window.innerHeight;
    canvas.width = width;
    canvas.height = height;
}
resizeCanvas();
window.addEventListener('resize', resizeCanvas);

// Création de particules/vecteurs
class Vector {
    constructor() {
        this.x = Math.random() * width;
        this.y = Math.random() * height;
        this.vx = (Math.random() - 0.5) * 2;
        this.vy = (Math.random() - 0.5) * 2;
        this.size = 10;
    }

    move() {
        this.x += this.vx;
        this.y += this.vy;

        if (this.x < 0 || this.x > width) this.vx *= -1;
        if (this.y < 0 || this.y > height) this.vy *= -1;
    }

    draw() {
        ctx.beginPath();
        ctx.arc(this.x, this.y, this.size, 0, Math.PI * 2);
        ctx.fillStyle = 'white';
        ctx.fill();
    }
}

// Initialiser les vecteurs
const vectors = [];
for (let i = 0; i < 20; i++) {
    vectors.push(new Vector());
}

// Animation du canvas
function animate() {
    ctx.clearRect(0, 0, width, height);

    // Dessiner et mettre à jour chaque vecteur
    vectors.forEach(vector => {
        vector.move();
        vector.draw();

        // Relier les vecteurs proches par des lignes
        vectors.forEach(other => {
            const dx = vector.x - other.x;
            const dy = vector.y - other.y;
            const distance = Math.sqrt(dx * dx + dy * dy);

            if (distance < 250) {
                ctx.beginPath();
                ctx.moveTo(vector.x, vector.y);
                ctx.lineTo(other.x, other.y);
                ctx.strokeStyle = `rgba(255, 255, 255, ${2 - distance / 100})`;
                ctx.lineWidth = 2;
                ctx.stroke();
            }
        });
    });

    requestAnimationFrame(animate);
}
animate();