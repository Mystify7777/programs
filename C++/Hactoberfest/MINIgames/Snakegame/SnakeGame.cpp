#include <iostream>
#include <conio.h> // For getch()
#include <windows.h> // For Sleep()
using namespace std;

const int width = 20;
const int height = 20;
int x, y, fruitX, fruitY, score;
int tailX[100], tailY[100]; // Arrays to store the snake's tail
int nTail;
enum eDirection { STOP = 0, LEFT, RIGHT, UP, DOWN };
eDirection dir;

void setup() {
    dir = STOP; // Initial direction
    x = width / 2; // Start position of the snake
    y = height / 2;
    fruitX = rand() % width; // Random fruit position
    fruitY = rand() % height;
    score = 0;
    nTail = 0;
}

void draw() {
    system("cls"); // Clear the console
    for (int i = 0; i < width + 2; i++)
        cout << "#"; // Top wall
    cout << endl;

    for (int i = 0; i < height; i++) {
        for (int j = 0; j < width; j++) {
            if (j == 0) cout << "#"; // Left wall
            if (i == y && j == x)
                cout << "O"; // Snake head
            else if (i == fruitY && j == fruitX)
                cout << "F"; // Fruit
            else {
                bool print = false;
                for (int k = 0; k < nTail; k++) {
                    if (tailX[k] == j && tailY[k] == i) {
                        cout << "o"; // Snake tail
                        print = true;
                    }
                }
                if (!print) cout << " "; // Empty space
            }
            if (j == width - 1) cout << "#"; // Right wall
        }
        cout << endl;
    }

    for (int i = 0; i < width + 2; i++)
        cout << "#"; // Bottom wall
    cout << endl;
    cout << "Score: " << score << endl;
}

void input() {
    if (_kbhit()) {
        switch (_getch()) {
            case 'a':
                dir = LEFT;
                break;
            case 'd':
                dir = RIGHT;
                break;
            case 'w':
                dir = UP;
                break;
            case 's':
                dir = DOWN;
                break;
            case 'x':
                dir = STOP; // Stop the game
                break;
        }
    }
}

void logic() {
    int prevX = tailX[0]; // Previous position of the tail
    int prevY = tailY[0];
    int prev2X, prev2Y;
    tailX[0] = x; // Update the position of the tail
    tailY[0] = y;

    for (int i = 1; i < nTail; i++) {
        prev2X = tailX[i]; // Save previous position
        prev2Y = tailY[i];
        tailX[i] = prevX; // Move the tail
        tailY[i] = prevY;
        prevX = prev2X; // Update the previous position
        prevY = prev2Y;
    }

    switch (dir) {
        case LEFT:
            x--;
            break;
        case RIGHT:
            x++;
            break;
        case UP:
            y--;
            break;
        case DOWN:
            y++;
            break;
        default:
            break;
    }

    // Check for fruit collision
    if (x == fruitX && y == fruitY) {
        score += 10; // Increase score
        fruitX = rand() % width; // Generate new fruit
        fruitY = rand() % height;
        nTail++; // Increase tail length
    }

    // Check for wall collision
    if (x >= width) x = 0; else if (x < 0) x = width - 1;
    if (y >= height) y = 0; else if (y < 0) y = height - 1;

    // Check for tail collision
    for (int i = 0; i < nTail; i++)
        if (tailX[i] == x && tailY[i] == y)
            dir = STOP; // End game on collision
}

int main() {
    setup();
    while (dir != STOP) {
        draw();
        input();
        logic();
        Sleep(100); // Control the speed of the game
    }
    system("pause"); // Add this line before returning from main()

    return 0;
}
