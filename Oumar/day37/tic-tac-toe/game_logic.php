<?php
session_start();

function initializeGame() {
    $difficulty = $_SESSION['difficulty'] ?? 'easy';
    $gridSize = ($difficulty == 'easy') ? 3 : (($difficulty == 'medium') ? 4 : 5);
    $_SESSION['board'] = array_fill(0, $gridSize * $gridSize, '');
    $_SESSION['currentPlayer'] = 'X';
    $_SESSION['gameActive'] = true;
    $_SESSION['gridSize'] = $gridSize;
}

function makeMove($index) {
    if ($_SESSION['board'][$index] === '' && $_SESSION['gameActive']) {
        $_SESSION['board'][$index] = $_SESSION['currentPlayer'];
        if (checkWin($_SESSION['currentPlayer'])) {
            $winner = $_SESSION['players'][$_SESSION['currentPlayer']];
            updateScores($winner);
            $_SESSION['gameActive'] = false;
            return ['status' => 'win', 'winner' => $winner];
        } elseif (isBoardFull()) {
            updateScores('ties');
            $_SESSION['gameActive'] = false;
            return ['status' => 'tie'];
        } else {
            $_SESSION['currentPlayer'] = ($_SESSION['currentPlayer'] === 'X') ? 'O' : 'X';
            return ['status' => 'continue'];
        }
    }
    return ['status' => 'invalid'];
}

function checkWin($player) {
    $gridSize = $_SESSION['gridSize'];
    $board = $_SESSION['board'];
    
    // Check rows and columns
    for ($i = 0; $i < $gridSize; $i++) {
        if (checkLine($i * $gridSize, 1, $gridSize, $player)) return true;
        if (checkLine($i, $gridSize, $gridSize, $player)) return true;
    }
    
    // Check diagonals
    if (checkLine(0, $gridSize + 1, $gridSize, $player)) return true;
    if (checkLine($gridSize - 1, $gridSize - 1, $gridSize, $player)) return true;
    
    return false;
}

function checkLine($start, $step, $count, $player) {
    $streak = 0;
    $requiredStreak = ($_SESSION['gridSize'] === 3) ? 3 : 4;
    for ($i = 0; $i < $count; $i++) {
        if ($_SESSION['board'][$start + $i * $step] === $player) {
            $streak++;
            if ($streak === $requiredStreak) return true;
        } else {
            $streak = 0;
        }
    }
    return false;
}

function isBoardFull() {
    return !in_array('', $_SESSION['board']);
}

function updateScores($winner) {
    if (!isset($_SESSION['scores'])) {
        $_SESSION['scores'] = ['X' => 0, 'O' => 0, 'ties' => 0];
    }
    if ($winner === 'ties') {
        $_SESSION['scores']['ties']++;
    } else {
        $_SESSION['scores'][$winner]++;
    }
}

function getGameState() {
    return [
        'board' => $_SESSION['board'],
        'currentPlayer' => $_SESSION['currentPlayer'],
        'gameActive' => $_SESSION['gameActive'],
        'gridSize' => $_SESSION['gridSize'],
        'players' => $_SESSION['players'],
        'scores' => $_SESSION['scores'] ?? ['X' => 0, 'O' => 0, 'ties' => 0],
        'difficulty' => $_SESSION['difficulty']
    ];
}

// Handle AJAX requests
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $action = $_POST['action'] ?? '';
    
    switch ($action) {
        case 'initGame':
            $_SESSION['players'] = [
                'X' => $_POST['playerX'],
                'O' => $_POST['playerO']
            ];
            $_SESSION['difficulty'] = $_POST['difficulty'];
            initializeGame();
            echo json_encode(getGameState());
            break;
        
        case 'makeMove':
            $index = $_POST['index'] ?? -1;
            $result = makeMove($index);
            $result['gameState'] = getGameState();
            echo json_encode($result);
            break;
        
        case 'getState':
            echo json_encode(getGameState());
            break;
        
        case 'resetScores':
            $_SESSION['scores'] = ['X' => 0, 'O' => 0, 'ties' => 0];
            echo json_encode($_SESSION['scores']);
            break;
    }
    exit;
}
?>