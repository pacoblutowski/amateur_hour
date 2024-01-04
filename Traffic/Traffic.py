import pygame
import random
from sys import exit

pygame.init()

WIDTH = 1600
HEIGHT = 1000
FPS = 60
GAME_ACTIVE = True

def main():
	pygame.init()
	screen = pygame.display.set_mode((WIDTH,HEIGHT))
	pygame.display.set_caption('Traffic')
	clock = pygame.time.Clock()

	DAMAGE = 0
	MAX_DAMAGE = 1000
	title_font = pygame.font.Font(None, 75)
	damage_font = pygame.font.Font(None, 75)
	ending_font = pygame.font.Font(None,200)
	hero_x_pos = WIDTH//2-55
	hero_y_pos = HEIGHT-210
	villain1_y_pos = -210
	villain1_x_pos = WIDTH//2-150
	villain2_y_pos = -210
	villain2_x_pos = WIDTH//2+40
	middle_line_y_pos = 0
	finish_line_y_pos = -(HEIGHT*30)


	title_surface = title_font.render('TRAFFIC',False,'white')
	shoulder = pygame.Surface((500,HEIGHT))
	shoulder.fill((125,125,125,255))
	road = pygame.Surface((400,HEIGHT))
	road.fill('darkgray')
	banner = pygame.Surface((WIDTH-40,HEIGHT//6))
	banner.fill('white')
	banner_rect = banner.get_rect(midtop = (WIDTH//2,HEIGHT//6))
	banner_border = pygame.Surface((WIDTH,HEIGHT//6+20))
	banner_border.fill('black')


	hero = pygame.image.load('Graphics/GTI.png').convert_alpha()
	hero_rect = hero.get_rect(topleft = (hero_x_pos,hero_y_pos))
	villain_1 = pygame.image.load('Graphics/Blue_Ford.png').convert_alpha()
	villain_1_rect = villain_1.get_rect(topleft = (villain1_x_pos,villain1_y_pos))
	villain_2 = pygame.image.load('Graphics/Black_Ford.png').convert_alpha()
	villain_2_rect = villain_2.get_rect(topleft = (villain2_x_pos,villain2_y_pos))
	finish_line = pygame.image.load('Graphics/Finish.png').convert_alpha()
	finish_line_rect = finish_line.get_rect(midtop = (WIDTH//2,finish_line_y_pos))
	rando = (random.randint(0,3))
	pygame.time.delay(1000)

	def direct_crash():
		pygame.time.delay(70)

	def total_damage():
		pygame.init()
		totaled_surface = ending_font.render('LOSER!',True,'orange')
		totaled_surface_rect = totaled_surface.get_rect(midtop = (WIDTH//2,HEIGHT//2))
		screen.blit(totaled_surface,(totaled_surface_rect))
		pygame.display.update()
		pygame.time.delay(2000)
		while True:
			pygame.init()
			replay_text_background = pygame.Surface((WIDTH,HEIGHT -200))
			replay_text_background.fill('white')
			replay_text_surf = title_font.render('                  Press ENTER to Play Again or ESC to Quit',False,'black')
			replay_text_rect = replay_text_surf.get_rect(topleft = (0,HEIGHT-70))
			screen.blit(replay_text_background,(replay_text_rect))
			screen.blit(replay_text_surf,(replay_text_rect))
			pygame.display.update()
			for event in pygame.event.get():
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_RETURN: 
						main()
					elif event.key == pygame.K_ESCAPE:
						pygame.quit()
						exit()

	def winner_winner():
		pygame.init()
		winner_surf = ending_font.render('Congrats F*ck Face!', False, 'black')
		winner_surf_rect = winner_surf.get_rect(midtop = (WIDTH//2, HEIGHT//5))
		screen.blit(banner_border,(banner_rect))
		pygame.display.update()		
		screen.blit(banner,(banner_rect))
		pygame.display.update()
		screen.blit(winner_surf,(winner_surf_rect))
		pygame.display.update()
		pygame.time.delay(3000)
		while True:
			pygame.init()
			replay_text_background = pygame.Surface((WIDTH,HEIGHT -200))
			replay_text_background.fill('white')
			replay_text_surf = title_font.render('Press ENTER to Play Again or ESC to Quit',False,'black')
			replay_text_rect = replay_text_surf.get_rect(midtop = (WIDTH//2,HEIGHT-70))
			screen.blit(replay_text_background,(0,HEIGHT-80))
			screen.blit(replay_text_surf,(replay_text_rect))
			pygame.display.update()
			for event in pygame.event.get():
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_RETURN: 
						main()
					elif event.key == pygame.K_ESCAPE:
						pygame.quit()
						exit()

	while True:
		pygame.init()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				exit()

		keys_pressed = pygame.key.get_pressed()
		if keys_pressed[pygame.K_LEFT] and hero_rect.x - VEL > (WIDTH//2-450): hero_rect.x -= VEL
		if keys_pressed[pygame.K_RIGHT] and hero_rect.x + VEL < (WIDTH//2+350): hero_rect.x += VEL
		if keys_pressed[pygame.K_UP] and hero_rect.y + VEL > 0: hero_rect.y -= VEL
		if keys_pressed[pygame.K_DOWN] and hero_rect.y + VEL < (HEIGHT-100): hero_rect.y += VEL
		if hero_rect.y <= (HEIGHT//2):
			VEL = 10 
		elif hero_rect.y > (HEIGHT//2):
			VEL = 5

		screen.fill('darkgreen')
		damage_display = (DAMAGE/10)	
		damage_surface = damage_font.render(f'Damage: {damage_display} %',True,'red')
		screen.blit(damage_surface,(10,100))
		screen.blit(shoulder,(WIDTH//2-250,0))
		screen.blit(road,(WIDTH//2-200,0))
		race_border_1 = pygame.Surface((200,HEIGHT))
		race_border_1.fill('darkgreen')
		race_border_1_rect = race_border_1.get_rect(topleft = ((WIDTH//2-450),0))
		race_border_2 = pygame.Surface((200,HEIGHT))
		race_border_2.fill('darkgreen')
		race_border_2_rect = race_border_2.get_rect(topleft = ((WIDTH//2+250),0))

		pygame.draw.ellipse(screen,(115,115,115),(pygame.Rect((WIDTH//2-400),middle_line_y_pos,100,75)))
		pygame.draw.ellipse(screen,(115,115,115),(pygame.Rect((WIDTH//2+325),-900+middle_line_y_pos,100,75)))
		pygame.draw.line(screen,'white',(WIDTH//2-200,0),(WIDTH//2-200,HEIGHT),5)
		pygame.draw.line(screen,'white',(WIDTH//2+200,0),(WIDTH//2+200,HEIGHT),5)
		pygame.draw.line(screen,'white',((WIDTH//2-3),(middle_line_y_pos + HEIGHT - 3000)),((WIDTH//2-3),(middle_line_y_pos+HEIGHT-3000+100)),6)
		pygame.draw.line(screen,'white',((WIDTH//2-3),(middle_line_y_pos + HEIGHT - 2800)),((WIDTH//2-3),(middle_line_y_pos+HEIGHT-2800+100)),6)
		pygame.draw.line(screen,'white',((WIDTH//2-3),(middle_line_y_pos + HEIGHT - 2600)),((WIDTH//2-3),(middle_line_y_pos+HEIGHT-2600+100)),6)
		pygame.draw.line(screen,'white',((WIDTH//2-3),(middle_line_y_pos + HEIGHT - 2400)),((WIDTH//2-3),(middle_line_y_pos+HEIGHT-2400+100)),6)
		pygame.draw.line(screen,'white',((WIDTH//2-3),(middle_line_y_pos + HEIGHT - 2200)),((WIDTH//2-3),(middle_line_y_pos+HEIGHT-2200+100)),6)
		pygame.draw.line(screen,'white',((WIDTH//2-3),(middle_line_y_pos + HEIGHT - 2000)),((WIDTH//2-3),(middle_line_y_pos+HEIGHT-2000+100)),6)
		pygame.draw.line(screen,'white',((WIDTH//2-3),(middle_line_y_pos + HEIGHT - 1800)),((WIDTH//2-3),(middle_line_y_pos+HEIGHT-1800+100)),6)
		pygame.draw.line(screen,'white',((WIDTH//2-3),(middle_line_y_pos + HEIGHT - 1600)),((WIDTH//2-3),(middle_line_y_pos+HEIGHT-1600+100)),6)
		pygame.draw.line(screen,'white',((WIDTH//2-3),(middle_line_y_pos + HEIGHT - 1400)),((WIDTH//2-3),(middle_line_y_pos+HEIGHT-1400+100)),6)
		pygame.draw.line(screen,'white',((WIDTH//2-3),(middle_line_y_pos + HEIGHT - 1200)),((WIDTH//2-3),(middle_line_y_pos+HEIGHT-1200+100)),6)
		pygame.draw.line(screen,'white',((WIDTH//2-3),(middle_line_y_pos + HEIGHT - 1000)),((WIDTH//2-3),(middle_line_y_pos+HEIGHT-1000+100)),6)
		pygame.draw.line(screen,'white',((WIDTH//2-3),(middle_line_y_pos + HEIGHT - 800)),((WIDTH//2-3),(middle_line_y_pos+HEIGHT-800+100)),6)
		pygame.draw.line(screen,'white',((WIDTH//2-3),(middle_line_y_pos + HEIGHT - 600)),((WIDTH//2-3),(middle_line_y_pos+HEIGHT-600+100)),6)
		pygame.draw.line(screen,'white',((WIDTH//2-3),(middle_line_y_pos + HEIGHT - 400)),((WIDTH//2-3),(middle_line_y_pos+HEIGHT-400+100)),6)
		pygame.draw.line(screen,'white',((WIDTH//2-3),(middle_line_y_pos + HEIGHT - 200)),((WIDTH//2-3),(middle_line_y_pos+HEIGHT-200+100)),6)
		pygame.draw.line(screen,'white',((WIDTH//2-3),(middle_line_y_pos + HEIGHT - 0)),((WIDTH//2-3),(middle_line_y_pos+HEIGHT-0+100)),6)

		middle_line_y_pos += 25
		if middle_line_y_pos > (HEIGHT+800): middle_line_y_pos = 0
			
		screen.blit(title_surface,(10,10))
		screen.blit(finish_line,finish_line_rect)

		finish_line_y_pos += 25
		finish_line_rect.top +=25

		screen.blit(villain_1,villain_1_rect)
		villain_1_rect.top += (VEL-2)

		if villain_1_rect.top > HEIGHT: villain_1_rect.top = -210
			
		screen.blit(villain_2,villain_2_rect)
		villain_2_rect.top += (VEL*2-3)

		screen.blit(hero,hero_rect)

		if villain_2_rect.top > HEIGHT+300: villain_2_rect.top = -210

		if hero_rect.colliderect(villain_1_rect): DAMAGE += 2
		#pygame.display.update()
		
		if hero_rect.colliderect(villain_2_rect): DAMAGE += 2
		#pygame.display.update()		

		if hero_rect.colliderect(race_border_1_rect): DAMAGE += 2
		#pygame.display.update()		

		if hero_rect.colliderect(race_border_2_rect): DAMAGE += 2
		pygame.display.update()

		if villain_1_rect.collidepoint((hero_rect.midtop)):
			DAMAGE += 30
			direct_crash()

		if villain_2_rect.collidepoint((hero_rect.midtop)):
			DAMAGE += 30
			direct_crash()

		if DAMAGE >= (MAX_DAMAGE):
			pygame.display.update()
			total_damage()

		if finish_line_rect.collidepoint((hero_rect.midtop)):
			winner_winner()
		
		clock.tick(FPS)

if __name__ == "__main__": 
	main()
