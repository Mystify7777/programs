#include <SFML/Graphics.hpp>
#include <SFML/Window.hpp>
#include <SFML/System.hpp>
#include <iostream>
#include <deque>
#include <cstdlib>
#include <ctime>

using namespace std;
using namespace sf;

const int WIDTH = 600;
const int HEIGHT = 400;
const int DOT_SIZE = 10;
const int INITIAL_LENGTH = 3;

class SnakeGame {
public:
    SnakeGame() : window(VideoMode(WIDTH, HEIGHT), "Snake Game"), direction(Right), isGameOver(false) {
        srand(static_cast<unsigned>(time(0)));
        snake.push_front(Vector2i(WIDTH / 2, HEIGHT / 2));
        spawnFruit();
    }

    void run() {
        while (window.isOpen()) {
            processEvents();
            if (!isGameOver) {
                update();
            }
            render();
        }
    }

private:
    enum Direction { Up, Down, Left, Right };
    RenderWindow window;
    deque<Vector2i> snake;
    Direction direction;
    Vector2i fruit;
    bool isGameOver;

    void processEvents() {
        Event event;
        while (window.pollEvent(event)) {
            if (event.type == Event::Closed)
                window.close();
            if (event.type == Event::KeyPressed) {
                switch (event.key.code) {
                    case Keyboard::Up:
                        if (direction != Down) direction = Up; break;
                    case Keyboard::Down:
                        if (direction != Up) direction = Down; break;
                    case Keyboard::Left:
                        if (direction != Right) direction = Left; break;
                    case Keyboard::Right:
                        if (direction != Left) direction = Right; break;
                    default: break;
                }
            }
        }
    }

    void update() {
        Vector2i newHead = snake.front();

        switch (direction) {
            case Up:    newHead.y -= DOT_SIZE; break;
            case Down:  newHead.y += DOT_SIZE; break;
            case Left:  newHead.x -= DOT_SIZE; break;
            case Right: newHead.x += DOT_SIZE; break;
        }

        if (newHead.x < 0 || newHead.x >= WIDTH || newHead.y < 0 || newHead.y >= HEIGHT || 
            find(snake.begin(), snake.end(), newHead) != snake.end()) {
            isGameOver = true;
            return;
        }

        snake.push_front(newHead);
        if (newHead == fruit) {
            spawnFruit();
        } else {
            snake.pop_back();
        }
    }

    void spawnFruit() {
        int x = (rand() % (WIDTH / DOT_SIZE)) * DOT_SIZE;
        int y = (rand() % (HEIGHT / DOT_SIZE)) * DOT_SIZE;
        fruit = Vector2i(x, y);
    }

    void render() {
        window.clear(Color::Black);
        
        // Draw the snake
        for (const auto& segment : snake) {
            RectangleShape rect(Vector2f(DOT_SIZE, DOT_SIZE));
            rect.setFillColor(Color::Green);
            rect.setPosition(segment.x, segment.y);
            window.draw(rect);
        }

        // Draw the fruit
        RectangleShape fruitRect(Vector2f(DOT_SIZE, DOT_SIZE));
        fruitRect.setFillColor(Color::Red);
        fruitRect.setPosition(fruit.x, fruit.y);
        window.draw(fruitRect);

        if (isGameOver) {
            Font font;
            if (!font.loadFromFile("arial.ttf")) {
                cout << "Could not load font!" << endl;
            }
            Text text("Game Over", font, 30);
            text.setFillColor(Color::White);
            text.setPosition(WIDTH / 2 - 70, HEIGHT / 2 - 15);
            window.draw(text);
        }

        window.display();
    }
};

int main() {
    SnakeGame game;
    game.run();
    return 0;
}
