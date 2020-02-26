class Box:
	class Cell:
		
		def __init__(self, row, col):
			self.value = 0
			self.row = row
			self.col = col
			self.neighbors = [] 
		
		def fill_neighbours(self, grid):
			for i in range(-1, 2):
				for j in range(-1, 2):
					if i == 0 and j == 0:
						continue
					if self.row + i < len(grid) and self.col + j < len(grid[0]):
						self.neighbors.append(grid[self.row + i][self.col + j])
		
		def near_alive(self):
			return sum([i.value for i in self.neighbors])
		
		def is_alive(self):
			return self.value
			
		def set_alive(self, val):
			self.value = val
					
			
	def __init__(self, row, col):
		self.grid = []
		for i in range(row):
			temp = []
			for j in range(col):
				temp.append(self.Cell(i, j))
			self.grid.append(temp)
		for i in self.grid:
			for j in i:
				j.fill_neighbours(self.grid)
	def step(self):
		for i in self.grid:
			for j in i:
				if j.near_alive() == 3:
					j.set_alive(1)
				else:
					j.set_alive(0)
	def listed_view(self):
		return [[j.is_alive() for j in i] for i in self.grid]
				
	def box_printer(self):
		[print(i) for i in self.listed_view()]