const bird = document.querySelector('.bird');
const pipeTop = document.querySelector('.pipe-top');
const pipeBottom = document.querySelector('.pipe-bottom');
const statusDisplay = document.querySelector('.status');
const restartButton = document.getElementById('restart');

let birdY = 250;
let birdVelocity = 0;
let gravity = 0.5;
let isGameOver = false;
let pipeX = 400;
let gap = 150;

const startGame = () => {
    birdY = 250;
    birdVelocity = 0;
    pipeX = 400;
    isGameOver = false;
    statusDisplay.innerHTML = "";
    restartButton.style.display = "none";
    gameLoop();
};

const gameLoop = () => {
    if (isGameOver) return;

    birdVelocity += gravity;
    birdY += birdVelocity;
    bird.style.top = birdY + 'px';

    pipeX -= 2;
    if (pipeX < -60) {
        pipeX = 400;
        const randomHeight = Math.floor(Math.random() * (400 - gap)) + 50;
        pipeTop.style.height = randomHeight + 'px';
        pipeBottom.style.height = (400 - randomHeight - gap) + 'px';
    }
    
    pipeTop.style.left = pipeX + 'px';
    pipeBottom.style.left = pipeX + 'px';

    if (
        birdY <= 0 || birdY >= 560 || 
        (pipeX < 90 && pipeX > 30 && 
         (birdY < parseInt(pipeTop.style.height) || birdY > 600 - parseInt(pipeBottom.style.height)))
    ) {
        gameOver();
    } else {
        requestAnimationFrame(gameLoop);
    }
};

const gameOver = () => {
    isGameOver = true;
    statusDisplay.innerHTML = "¡Has perdido!";
    restartButton.style.display = "inline-block";
};

document.addEventListener('keydown', (e) => {
    if (e.code === 'Space' && !isGameOver) {
        birdVelocity = -8;
    } else if (isGameOver && e.code === 'Space') {
        startGame();
    }
});

restartButton.addEventListener('click', startGame);

startGame();
