let currentPlayer = 'X';
let gameActive = true;
const board = document.getElementById('board');
let cells;

function initializeGame() {
    // Create the game board
    for (let i = 0; i < 9; i++) {
        const cell = document.createElement('div');
        cell.classList.add('cell');
        cell.addEventListener('click', handleCellClick);
        board.appendChild(cell);
    }
    cells = Array.from(document.querySelectorAll('.cell'));
    updateGameStatus();
}

function handleCellClick(e) {
    const cell = e.target;
    if (cell.textContent !== '' || !gameActive) return;

    cell.textContent = currentPlayer;
    cell.classList.add(currentPlayer.toLowerCase());

    if (checkWin()) {
        gameActive = false;
        updateGameStatus(`Le joueur ${currentPlayer} a gagné!`);
    } else if (checkDraw()) {
        gameActive = false;
        updateGameStatus("Match nul!");
    } else {
        currentPlayer = currentPlayer === 'X' ? 'O' : 'X';
        updateGameStatus();
    }
}

function checkWin() {
    const winPatterns = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8], // Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8], // Columns
        [0, 4, 8], [2, 4, 6] // Diagonals
    ];

    return winPatterns.some(pattern => {
        const [a, b, c] = pattern;
        return cells[a].textContent &&
               cells[a].textContent === cells[b].textContent &&
               cells[a].textContent === cells[c].textContent;
    });
}

function checkDraw() {
    return cells.every(cell => cell.textContent !== '');
}

function updateGameStatus(message) {
    const statusElement = document.getElementById('currentPlayer');
    statusElement.textContent = message || `C'est au tour du joueur ${currentPlayer}`;
}

function startNewGame() {
    cells.forEach(cell => {
        cell.textContent = '';
        cell.classList.remove('x', 'o');
    });

    currentPlayer = 'X';
    gameActive = true;
    updateGameStatus();
}

document.addEventListener('DOMContentLoaded', () => {
    initializeGame();
    document.getElementById('newGameBtn').addEventListener('click', startNewGame);
});