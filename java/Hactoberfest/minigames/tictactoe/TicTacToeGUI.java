import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.util.Random;

public class TicTacToeGUI extends JFrame implements ActionListener {
    private JButton[][] buttons = new JButton[3][3];
    private char currentPlayer = 'X';
    private boolean isAIEnabled = false;
    private String difficulty = "Easy"; // Default difficulty

    public TicTacToeGUI() {
        setTitle("Tic Tac Toe");
        setSize(400, 400);
        setDefaultCloseOperation(EXIT_ON_CLOSE);
        setLayout(new GridLayout(4, 4));

        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                buttons[i][j] = new JButton("");
                buttons[i][j].setFont(new Font("Arial", Font.PLAIN, 60));
                buttons[i][j].setFocusPainted(false);
                buttons[i][j].addActionListener(this);
                add(buttons[i][j]);
            }
        }

        JButton resetButton = new JButton("Reset");
        resetButton.addActionListener(e -> resetGame());
        add(resetButton);

        JButton aiButton = new JButton("Play AI");
        aiButton.addActionListener(e -> toggleAI());
        add(aiButton);

        String[] difficulties = {"Easy", "Medium", "Hard"};
        JComboBox<String> difficultySelector = new JComboBox<>(difficulties);
        difficultySelector.addActionListener(e -> difficulty = (String) difficultySelector.getSelectedItem());
        add(difficultySelector);

        setVisible(true);
    }

    @Override
    public void actionPerformed(ActionEvent e) {
        JButton buttonClicked = (JButton) e.getSource();

        if (buttonClicked.getText().equals("")) {
            buttonClicked.setText(String.valueOf(currentPlayer));

            if (checkWin()) {
                JOptionPane.showMessageDialog(this, "Player " + currentPlayer + " wins!");
                resetGame();
            } else if (isBoardFull()) {
                JOptionPane.showMessageDialog(this, "It's a tie!");
                resetGame();
            } else {
                currentPlayer = (currentPlayer == 'X') ? 'O' : 'X';

                if (isAIEnabled && currentPlayer == 'O') {
                    aiMove();
                }
            }
        }
    }

    private void aiMove() {
        if (difficulty.equals("Easy")) {
            randomMove();
        } else if (difficulty.equals("Medium")) {
            if (!blockWinningMove('X')) { // Block player's winning move if needed
                randomMove();
            }
        } else if (difficulty.equals("Hard")) {
            minimax('O'); // AI plays as 'O'
        }
    
        // Check for a win or tie after AI move
        if (checkWin()) {
            JOptionPane.showMessageDialog(this, "Player " + currentPlayer + " wins!");
            resetGame();
        } else if (isBoardFull()) {
            JOptionPane.showMessageDialog(this, "It's a tie!");
            resetGame();
        } else {
            currentPlayer = 'X'; // Switch back to player
        }
    }
    
    private void minimax(char player) {
        int bestScore = (player == 'O') ? Integer.MIN_VALUE : Integer.MAX_VALUE;
        int moveRow = -1, moveCol = -1;
    
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                if (buttons[i][j].getText().equals("")) {
                    buttons[i][j].setText(String.valueOf(player));
                    int score = minimaxScore(player == 'O' ? 'X' : 'O');
                    buttons[i][j].setText(""); // Undo the move
    
                    if (player == 'O' && score > bestScore) {
                        bestScore = score;
                        moveRow = i;
                        moveCol = j;
                    } else if (player == 'X' && score < bestScore) {
                        bestScore = score;
                        moveRow = i;
                        moveCol = j;
                    }
                }
            }
        }
    
        if (moveRow != -1 && moveCol != -1) {
            buttons[moveRow][moveCol].setText(String.valueOf('O')); // AI makes its move
        }
    }
    
    private int minimaxScore(char player) {
        if (checkWin()) {
            return (player == 'O') ? 1 : -1; // AI wins or loses
        }
        if (isBoardFull()) {
            return 0; // Tie
        }
    
        int bestScore = (player == 'O') ? Integer.MIN_VALUE : Integer.MAX_VALUE;
    
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                if (buttons[i][j].getText().equals("")) {
                    buttons[i][j].setText(String.valueOf(player));
                    int score = minimaxScore(player == 'O' ? 'X' : 'O');
                    buttons[i][j].setText(""); // Undo the move
    
                    if (player == 'O') {
                        bestScore = Math.max(score, bestScore);
                    } else {
                        bestScore = Math.min(score, bestScore);
                    }
                }
            }
        }
    
        return bestScore;
    }
    
    

    private void randomMove() {
        Random rand = new Random();
        int row, col;
        do {
            row = rand.nextInt(3);
            col = rand.nextInt(3);
        } while (!buttons[row][col].getText().equals(""));

        buttons[row][col].setText(String.valueOf(currentPlayer));
    }

    private boolean blockWinningMove(char player) {
        for (int i = 0; i < 3; i++) {
            // Check rows and columns for a winning move
            if (buttons[i][0].getText().equals(String.valueOf(player)) && 
                buttons[i][1].getText().equals(String.valueOf(player)) && 
                buttons[i][2].getText().equals("")) {
                buttons[i][2].setText(String.valueOf(currentPlayer));
                return true;
            }
            if (buttons[0][i].getText().equals(String.valueOf(player)) && 
                buttons[1][i].getText().equals(String.valueOf(player)) && 
                buttons[2][i].getText().equals("")) {
                buttons[2][i].setText(String.valueOf(currentPlayer));
                return true;
            }
        }

        // Check diagonals for a winning move
        if (buttons[0][0].getText().equals(String.valueOf(player)) && 
            buttons[1][1].getText().equals(String.valueOf(player)) && 
            buttons[2][2].getText().equals("")) {
            buttons[2][2].setText(String.valueOf(currentPlayer));
            return true;
        }
        if (buttons[0][2].getText().equals(String.valueOf(player)) && 
            buttons[1][1].getText().equals(String.valueOf(player)) && 
            buttons[2][0].getText().equals("")) {
            buttons[2][0].setText(String.valueOf(currentPlayer));
            return true;
        }
        return false;
    }

    private boolean checkWin() {
        for (int i = 0; i < 3; i++) {
            if (buttons[i][0].getText().equals(String.valueOf(currentPlayer)) && 
                buttons[i][1].getText().equals(String.valueOf(currentPlayer)) && 
                buttons[i][2].getText().equals(String.valueOf(currentPlayer))) {
                return true;  // Check rows
            }
            if (buttons[0][i].getText().equals(String.valueOf(currentPlayer)) && 
                buttons[1][i].getText().equals(String.valueOf(currentPlayer)) && 
                buttons[2][i].getText().equals(String.valueOf(currentPlayer))) {
                return true;  // Check columns
            }
        }
        if (buttons[0][0].getText().equals(String.valueOf(currentPlayer)) && 
            buttons[1][1].getText().equals(String.valueOf(currentPlayer)) && 
            buttons[2][2].getText().equals(String.valueOf(currentPlayer))) {
            return true;  // Check diagonal
        }
        if (buttons[0][2].getText().equals(String.valueOf(currentPlayer)) && 
            buttons[1][1].getText().equals(String.valueOf(currentPlayer)) && 
            buttons[2][0].getText().equals(String.valueOf(currentPlayer))) {
            return true;  // Check anti-diagonal
        }
        return false;
    }

    private boolean isBoardFull() {
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                if (buttons[i][j].getText().equals("")) {
                    return false;  // Found an empty cell
                }
            }
        }
        return true;  // No empty cells left
    }

    private void resetGame() {
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                buttons[i][j].setText("");
            }
        }
        currentPlayer = 'X';  // Reset to player X
    }

    private void toggleAI() {
        isAIEnabled = !isAIEnabled;  // Toggle AI mode
        JOptionPane.showMessageDialog(this, isAIEnabled ? "AI Enabled" : "AI Disabled");
        resetGame();  // Reset game on toggle
    }

    public static void main(String[] args) {
        new TicTacToeGUI();
    }
}
