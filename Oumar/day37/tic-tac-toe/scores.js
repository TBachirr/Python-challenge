function loadScores() {
    $.post('game_logic.php', { action: 'getState' }, function(response) {
        const gameState = JSON.parse(response);
        
        document.getElementById('playerXName').textContent = gameState.players.X;
        document.getElementById('playerOName').textContent = gameState.players.O;
        document.getElementById('scoreX').textContent = gameState.scores[gameState.players.X] || 0;
        document.getElementById('scoreO').textContent = gameState.scores[gameState.players.O] || 0;
        document.getElementById('scoreTies').textContent = gameState.scores.ties || 0;

        const difficultyText = gameState.difficulty === 'easy' ? 'Facile (3x3)' : 
                               gameState.difficulty === 'medium' ? 'Moyen (4x4)' : 'Difficile (5x5)';
        document.getElementById('difficultyDisplay').textContent = `Difficulté: ${difficultyText}`;

        // Display player history and scores
        const historyTable = document.getElementById('playerHistory');
        historyTable.innerHTML = '<tr><th>Joueur</th><th>Score</th></tr>';
        Object.entries(gameState.scores).forEach(([player, score]) => {
            if (player !== 'ties') {
                const row = historyTable.insertRow();
                row.insertCell(0).textContent = player;
                row.insertCell(1).textContent = score;
            }
        });
    });
}

function newGame() {
    window.location.href = 'tic.html';
}

function resetScores() {
    $.post('game_logic.php', { action: 'resetScores' }, function(response) {
        loadScores();
    });
}

function returnToPlayerPage() {
    window.location.href = 'players.html';
}

$(document).ready(function() {
    loadScores();
});