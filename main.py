import pygame
import pygame_gui
import sys

pygame.init()

screen = pygame.display.set_mode((800, 480), pygame.FULLSCREEN)
pygame.display.set_caption('Pygame')

manager = pygame_gui.UIManager((800, 480))

close_button = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect((-50, 0), (50, 30)), text='🗙', manager=manager,
    anchors={'top': 'top', 'left': 'right', 'bottom': 'top', 'right': 'right'}
)
maximize_button = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect((-50, 0), (50, 30)), text='🗖',
    manager=manager,
    anchors={'top': 'top', 'left': 'right', 'bottom': 'top', 'right': 'right', 'right_target': close_button}
)
minimize_button = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect((-50, 0), (50, 30)),
    text='🗕',
    manager=manager,
    anchors={'top': 'top', 'left': 'right', 'bottom': 'top', 'right': 'right', 'right_target': maximize_button}
)

fps_label = pygame_gui.elements.UILabel(
    relative_rect=pygame.Rect((0, -30), (150, 30)),
    text='FPS: 0',
    manager=manager,
    anchors={'top': 'bottom', 'left': 'left', 'bottom': 'bottom', 'right': 'left'}
)

mouse_pos_label = pygame_gui.elements.UILabel(
    relative_rect=pygame.Rect((150, -30), (150, 30)),
    text='Mouse: (0, 0)',
    manager=manager,
    anchors={'top': 'bottom', 'left': 'left', 'bottom': 'bottom', 'right': 'left'}
)

clock = pygame.time.Clock()
is_fullscreen = True

running = True
while running:
    time_delta = clock.tick(60) / 1000.0
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        manager.process_events(event)
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == minimize_button:
                pygame.display.iconify()
            elif event.ui_element == maximize_button:
                if is_fullscreen:
                    screen = pygame.display.set_mode((800, 480))
                else:
                    screen = pygame.display.set_mode((800, 480), pygame.FULLSCREEN)
                is_fullscreen = not is_fullscreen
            elif event.ui_element == close_button:
                running = False

    fps = clock.get_fps()
    fps_label.set_text(f'FPS: {int(fps)}')

    mouse_pos = pygame.mouse.get_pos()
    mouse_pos_label.set_text(f'Mouse: {mouse_pos}')

    manager.update(time_delta)
    manager.draw_ui(screen)
    pygame.display.flip()

pygame.quit()
sys.exit()
