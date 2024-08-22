const bird = document.querySelector('.bird');
const pipeTop = document.querySelector('.pipe-top');
const pipeBottom = document.querySelector('.pipe-bottom');
const statusDisplay = document.querySelector('.status');
const scoreDisplay = document.querySelector('.score');
const restartButton = document.getElementById('restart');
const headerDisplay = document.querySelector('.header');

const gameContainerHeight = document.querySelector('.game-container').offsetHeight;
let birdHeight = bird.offsetHeight; // Altura del pájaro
let birdY = gameContainerHeight / 2 - birdHeight / 2; // Centrar el pájaro inicialmente
const maxBirdY = gameContainerHeight - birdHeight; // Altura máxima permitida (altura contenedor - altura pájaro)
let birdVelocity = 0;
let gravity = 0.5;
let isGameOver = false;
let pipeX = 400;
let minGap = birdHeight * 4; // Mínimo espacio entre postes para que quepan cuatro pájaros
let maxNegativeBirdY = - birdHeight * 4; // Permitir que el pájaro suba 4 veces su altura fuera de la pantalla
let score = 0;

const startGame = () => {
    birdY = gameContainerHeight / 2 - birdHeight / 2;
    birdVelocity = 0;
    pipeX = 400;
    score = 0;
    isGameOver = false;
    statusDisplay.innerHTML = "";
    scoreDisplay.innerHTML = "Puntuación: 0";
    restartButton.style.display = "none";
    headerDisplay.style.justifyContent = 'center';
    gameLoop();
};

const gameLoop = () => {
    if (isGameOver) return;

    birdVelocity += gravity;
    birdY += birdVelocity;

    // Permitir que el pájaro suba hasta 4 veces su altura fuera de la pantalla
    if (birdY < maxNegativeBirdY) birdY = maxNegativeBirdY;

    // Si toca el suelo, el juego termina
    if (birdY > maxBirdY) {
        gameOver();
        return;
    }

    bird.style.top = birdY + 'px';

    pipeX -= 2;
    if (pipeX < -60) {
        pipeX = 400;

        // Generar una altura aleatoria para el poste superior asegurando que el espacio mínimo sea `minGap`
        const randomHeight = Math.floor(Math.random() * (gameContainerHeight - minGap)) + 50;
        pipeTop.style.height = randomHeight + 'px';
        pipeBottom.style.height = (gameContainerHeight - randomHeight - minGap) + 'px';

        score++;
        scoreDisplay.innerHTML = `Puntuación: ${score}`;
    }
    
    pipeTop.style.left = pipeX + 'px';
    pipeBottom.style.left = pipeX + 'px';

    // Verificar colisiones con los postes
    if (
        pipeX < 90 && pipeX > 30 && 
        (birdY < parseInt(pipeTop.style.height) || birdY > gameContainerHeight - parseInt(pipeBottom.style.height))
    ) {
        gameOver();
    } else {
        requestAnimationFrame(gameLoop);
    }
};

const gameOver = () => {
    isGameOver = true;
    headerDisplay.style.justifyContent = 'space-evenly';
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
