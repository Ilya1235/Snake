from tkinter import *
from random import randint
import time

class Snake():
    def __init__(self, row, col, size, field_color, snake_color, food_color):
        self.row = row
        self.col = col
        self.size = size
        self.field_color = field_color
        self.snake_color = snake_color
        self.food_color = food_color
        self.snake_array = []
        self.y = 1
        self.x = 0
        
        #Инициализация загона
        
        self.field_array = []
        self.root = Tk()
        self.root.title("Змея")
        self.root.geometry('800x800')
        self.canvas = Canvas(self.root, width = 800, height = 800, bg = self.field_color)
        self.canvas.pack()
        
        for i in range(row):
            self.field_array.append([])
            for j in range(col):
                self.field_array[i].append(self.canvas.create_rectangle((20 + j * self.size),
                                                                        (20 + i * self.size),
                                                                        (20 + (j + 1) * self.size),
                                                                        (20 + (i + 1) * self.size),
                                                                        fill = self.field_color))

        self.root.bind('<w>', lambda e: self.change_direction(1, 0))
        self.root.bind('<s>', lambda e: self.change_direction(-1, 0))
        self.root.bind('<a>', lambda e: self.change_direction(0, -1))
        self.root.bind('<d>', lambda e: self.change_direction(0, 1))

        while True:
            self.move_snake()
            time.sleep(0.05)
            
    def snake_init(self):
        '''Появление змеи'''   
        self.snake_array = [[self.row // 2, self.col // 2]]
        self.canvas.itemconfig(self.field_array[self.snake_array[0][0]][self.snake_array[0][1]], fill = self.snake_color)


    def food_init(self):
        '''Появление еды'''
        a = randint(0, self.row - 1)
        b = randint(0, self.col - 1)
        food = [a, b]
        food_1 = True
        while food_1 == True:
            food_1 = False
            for i in range(len(self.snake_array)):
                if self.snake_array[i] == food:
                    food_1 = True
                    a = randint(0, self.row - 1)
                    b = randint(0, self.col - 1)
                    food = [a, b]
        self.canvas.itemconfig(self.field_array[a][b], fill = self.food_color)    
    
    
    def snake_restart(self):
        '''Очищает поле от "трупа" змеи'''
        for i in range(len(self.field_array)):
            for j in range(len(self.field_array[0])):
                self.canvas.itemconfig(self.field_array[i][j], fill = self.field_color)
                self.root.update()
        self.snake_init()
        self.food_init()

             
    def move_snake(self):
        '''Движение змеи'''
        #Проверка на границы мира
        if not((self.row > self.snake_array[0][0] - self.y > -1) and (self.col > self.snake_array[0][1] + self.x > -1)):
            self.snake_restart()
        else:
            self.snake_array.insert(0, [self.snake_array[0][0] - self.y, self.snake_array[0][1] + self.x])
            for i in range(1, len(self.snake_array), 1):
                if self.snake_array[0] == self.snake_array[i]:
                    self.snake_restart()
                    return
            if str(self.canvas.itemconfig(self.field_array[self.snake_array[0][0]][self.snake_array[0][1]])['fill'][4]) == self.food_color: 
                self.canvas.itemconfig(self.field_array[self.snake_array[0][0]][self.snake_array[0][1]], fill = self.snake_color)
                self.food_init()
            else:
                self.canvas.itemconfig(self.field_array[self.snake_array[0][0]][self.snake_array[0][1]], fill = self.snake_color)
                self.canvas.itemconfig(self.field_array[self.snake_array[len(self.snake_array) - 1][0]][self.snake_array[len(self.snake_array) - 1][1]], fill = self.field_color)
                del self.snake_array[len(self.snake_array) - 1]
        self.root.update()


    def change_direction(self, y, x):
        self.y = y
        self.x = x



c = Snake(30, 30, 20, "white", "blue", "green")
c.snake_restart()
