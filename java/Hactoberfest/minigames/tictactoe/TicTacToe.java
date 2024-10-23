import java.util.Scanner;

public class TicTacToe {
    private char[][] board;
    private char currentPlayer;
    private int playerMoves; // To count the moves made by the current player

    public TicTacToe() {
        board = new char[3][3];
        currentPlayer = 'X'; // Player X starts
        playerMoves = 0;
    }

    public void printBoard() {
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                System.out.print(board[i][j] == '\0' ? '-' : board[i][j]);
            }
            System.out.println();
        }
    }

    public void play(int row, int col) {
        if (row >= 0 && row < 3 && col >= 0 && col < 3) {
            if (board[row][col] == '\0') {
                board[row][col] = currentPlayer;
                playerMoves++; // Increment the move count for the player

                // Switch players if they haven't reached 4 moves
                if (playerMoves < 4) {
                    currentPlayer = (currentPlayer == 'X') ? 'O' : 'X';
                } else {
                    // Clear board for the next moves after 4 moves
                    clearBoard();
                    playerMoves = 0; // Reset moves for the next cycle
                }
            } else {
                System.out.println("Cell already occupied! Try again.");
            }
        } else {
            System.out.println("Invalid input! Please enter row and column between 0 and 2.");
        }
    }

    public boolean checkWin() {
        // Check rows
        for (int i = 0; i < 3; i++) {
            if (board[i][0] != '\0' && board[i][0] == board[i][1] && board[i][1] == board[i][2]) {
                return true;
            }
        }

        // Check columns
        for (int i = 0; i < 3; i++) {
            if (board[0][i] != '\0' && board[0][i] == board[1][i] && board[1][i] == board[2][i]) {
                return true;
            }
        }

        // Check diagonals
        if (board[0][0] != '\0' && board[0][0] == board[1][1] && board[1][1] == board[2][2]) {
            return true;
        }
        if (board[0][2] != '\0' && board[0][2] == board[1][1] && board[1][1] == board[2][0]) {
            return true;
        }

        return false; // No winner yet
    }

    public void clearBoard() {
        board = new char[3][3]; // Reset the board
    }

    public static void main(String[] args) {
        TicTacToe game = new TicTacToe();
        Scanner scanner = new Scanner(System.in);
        String command;

        while (true) {
            game.printBoard();
            System.out.print("Enter row and column (0, 1, or 2) or 'reset' to reset the game: ");
            command = scanner.nextLine();

            // Reset game if user types "reset"
            if (command.equalsIgnoreCase("reset")) {
                game.clearBoard();
                System.out.println("Game has been reset.");
                continue;
            }

            String[] inputs = command.split(" ");
            if (inputs.length != 2) {
                System.out.println("Invalid input! Please enter two numbers.");
                continue;
            }

            try {
                int row = Integer.parseInt(inputs[0]);
                int col = Integer.parseInt(inputs[1]);
                game.play(row, col);
            } catch (NumberFormatException e) {
                System.out.println("Invalid input! Please enter two valid numbers.");
                continue;
            }

            if (game.checkWin()) {
                game.printBoard();
                System.out.println("Player " + (game.currentPlayer == 'X' ? 'O' : 'X') + " wins!");
                break;
            }
        }
        scanner.close();
    }
}
