document.getElementById('gameForm').addEventListener('submit', function(e) {
    e.preventDefault();
    const playerX = document.getElementById('playerX').value;
    const playerO = document.getElementById('playerO').value;
    const difficulty = document.getElementById('difficulty').value;
    
    localStorage.setItem('playerX', playerX);
    localStorage.setItem('playerO', playerO);
    localStorage.setItem('difficulty', difficulty);
    
    window.location.href = 'tic.html';
});