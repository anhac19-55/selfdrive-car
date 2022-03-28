
import pygame

pygame.init()

# define the RGB value for white,
# green, blue colour .
white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)


X = 400
Y = 400

# create the display surface object
# of specific dimension..e(X, Y).
display_surface = pygame.display.set_mode((X, Y))

# set the pygame window name
pygame.display.set_caption('Show Text')

# create a font object.
# 1st parameter is the font file
# which is present in pygame.
# 2nd parameter is size of the font
font = pygame.font.Font('freesansbold.ttf', 32)

# create a text surface object,
# on which text is drawn on it.
text = font.render('SELF-driving car', True, green, blue)

# create a rectangular object

textRect = text.get_rect()

# set the center of the rectangular object.
textRect.center = (X // 2, Y // 2)

# infinite loop
while True:

	# completely fill the surface object

	display_surface.fill(white)


	# to the display surface object
	# at the center coordinate.
	display_surface.blit(text, textRect)

	# iterate over the list of Event objects
	# that was returned by pygame.event.get() method.
	for event in pygame.event.get():

		# if event object type is QUIT
		# then quitting the pygame
		# and program both.
		if event.type == pygame.QUIT:

			# deactivates the pygame library
			pygame.quit()


			quit()


		pygame.display.update()


