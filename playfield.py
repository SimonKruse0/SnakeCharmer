from snake import *

class Playfield:
    def __init__(self, length_x, length_y, topology = None):
        self.length_x = length_x
        self.length_y = length_y
        self.playarea = np.zeros((length_x, length_y), dtype=np.int16)
        self.topology = topology
        if not self.topology is None:
            raise Exception(f"Encountered unsupported topology {self.topology}.")

    def clear_playarea(self):
        self.playarea = np.zeros((self.length_x, self.length_y), dtype=np.int16)

    def add_snake(self, snake, value = 1):
        self.clear_playarea()
        for snake_part in snake.shape:
            self.playarea.itemset((snake_part), value)
        self.snake_head = snake_part

    def add_apple(self):
        self.playarea.itemset(self.apple, 2)

    def place_apple(self):
        empty_fields = self.get_empty_fields()
        self.apple = random.choice(empty_fields)

    def get_empty_fields(self):
          empty_fields = []
          for y in range(self.length_y):
              for x in range(self.length_x):
                  if self.playarea[x,y] == 0:
                      empty_fields.append((x,y))
          return empty_fields


    def print_playfield(self, output = "terminal"):
        if output == "terminal":
            for line in self.playarea:
                for field in line:
                    print(field, end=" ")
                print("\n")
        elif output == "opencv":
          img = np.zeros((self.length_x,self.length_y,3))
          for y in range(self.length_y):
              for x in range(self.length_x):
                  if self.playarea[x,y] == 1:
                      img[x][y] = [255,0,0]
          cv2.imshow("snake", img)
          cv2.waitKey(0)


