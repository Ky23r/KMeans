import pygame
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from tkinter import Tk, filedialog

pygame.init()


def select_image_path():
    root = Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(
        title="Select an image file", filetypes=[("Image files", "*.png;*.jpg;*.jpeg")]
    )
    return file_path


K = 1

BACKGROUND = (126, 45, 140)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PURPLE = (255, 0, 255)


def create_text_render(text, size=50, color=WHITE):
    font = pygame.font.SysFont("sans", size)
    return font.render(text, True, color)


pygame.display.set_caption("3D KMeans Visualization")
screen = pygame.display.set_mode((1200, 700))

running = True

while running:
    pygame.time.Clock().tick(60)
    screen.fill(BACKGROUND)

    screen.blit(create_text_render("KMEANS", 100, PURPLE), (150, 50))
    screen.blit(create_text_render("IN", 100, PURPLE), (260, 200))
    screen.blit(create_text_render("DATA", 100, PURPLE), (200, 350))
    screen.blit(create_text_render("COMPRESSION", 100, PURPLE), (20, 500))

    pygame.draw.rect(screen, BLACK, (800, 100, 300, 100))
    pygame.draw.rect(screen, BLACK, (800, 250, 125, 100))
    pygame.draw.rect(screen, BLACK, (975, 250, 125, 100))

    screen.blit(create_text_render("RUN", 100), (860, 90))
    screen.blit(create_text_render("+", 150), (825, 210))
    screen.blit(create_text_render("-", 150), (1015, 195))

    mouse_x, mouse_y = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if 800 < mouse_x < 1100 and 100 < mouse_y < 200:
                file_path = select_image_path()
                if file_path:
                    img = plt.imread(file_path)
                    width, height = img.shape[0], img.shape[1]
                    img_reshaped = img.reshape(width * height, 3)
                    if img.max() > 1.0:
                        img_reshaped = img_reshaped / 255.0
                    kmeans = KMeans(n_clusters=K).fit(img_reshaped)
                    labels = kmeans.predict(img_reshaped)
                    clusters = kmeans.cluster_centers_
                    _img = clusters[labels].reshape(width, height, 3)
                    plt.imshow(_img)
                    plt.axis("off")
                    plt.show()

            if 800 < mouse_x < 925 and 250 < mouse_y < 350:
                K += 1

            if 975 < mouse_x < 1100 and 250 < mouse_y < 350:
                if K > 1:
                    K -= 1

    screen.blit(create_text_render("K = " + str(K), 100), (850, 400))

    pygame.display.flip()

pygame.quit()
