let gameState = {};

function initGame() {
    const playerX = localStorage.getItem('playerX');
    const playerO = localStorage.getItem('playerO');
    const difficulty = localStorage.getItem('difficulty');

    $.post('game_logic.php', {
        action: 'initGame',
        playerX: playerX,
        playerO: playerO,
        difficulty: difficulty
    }, function(response) {
        gameState = JSON.parse(response);
        renderBoard();
        updateDisplay();
    });
}

function makeMove(index) {
    $.post('game_logic.php', {
        action: 'makeMove',
        index: index
    }, function(response) {
        const result = JSON.parse(response);
        gameState = result.gameState;
        renderBoard();
        updateDisplay();

        if (result.status === 'win') {
            alert(`${result.winner} a gagné !`);
            setTimeout(() => { window.location.href = 'scores.html'; }, 1000);
        } else if (result.status === 'tie') {
            alert("Match nul !");
            setTimeout(() => { window.location.href = 'scores.html'; }, 1000);
        }
    });
}

function renderBoard() {
    const boardElement = document.getElementById('board');
    const cellSize = gameState.gridSize === 3 ? 80 : gameState.gridSize === 4 ? 70 : 60;
    boardElement.style.gridTemplateColumns = `repeat(${gameState.gridSize}, ${cellSize}px)`;
    boardElement.innerHTML = '';
    gameState.board.forEach((cell, index) => {
        const cellElement = document.createElement('div');
        cellElement.className = 'cell';
        cellElement.style.width = `${cellSize}px`;
        cellElement.style.height = `${cellSize}px`;
        cellElement.style.fontSize = `${cellSize * 0.6}px`;
        cellElement.onclick = () => makeMove(index);
        cellElement.textContent = cell;
        boardElement.appendChild(cellElement);
    });
}

function updateDisplay() {
    document.getElementById('difficultyDisplay').textContent = `Difficulté: ${gameState.difficulty} (${gameState.gridSize}x${gameState.gridSize})`;
    document.getElementById('currentPlayer').textContent = `Tour de ${gameState.players[gameState.currentPlayer]}`;
}

function changePlayers() {
    window.location.href = 'players.html';
}

$(document).ready(function() {
    initGame();
});