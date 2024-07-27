import pygame
from sklearn.cluster import KMeans
from math import sqrt
from random import randint


def distance(x, y):
    return sqrt((x[0] - y[0]) ** 2 + (x[1] - y[1]) ** 2)


pygame.init()

pygame.display.set_caption("KMeans Visualization")
screen = pygame.display.set_mode((1200, 700))

BACKGROUND = (126, 45, 140)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
LIGHT_GREY = (219, 219, 219)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
PURPLE = (255, 0, 255)
SKY = (0, 255, 255)
ORANGE = (255, 125, 25)
GRAPE = (100, 25, 125)
GRASS = (55, 155, 65)

colors = [YELLOW, RED, GREEN, BLUE, PURPLE, SKY, ORANGE, GRAPE, GRASS]


def create_text_render(x, size=50, color=WHITE):
    font = pygame.font.SysFont("sans", size)
    return font.render(x, True, color)


K = 0
points = []
clusters = []
labels = []
error = 0


def draw_interface():
    screen.blit(create_text_render("O"), (8, 1))
    screen.blit(create_text_render("x"), (790, 0))
    screen.blit(create_text_render("y"), (10, 560))
    pygame.draw.rect(screen, BLACK, (45, 45, 725, 5))
    pygame.draw.polygon(screen, BLACK, [(780, 47), (770, 40), (770, 55)])
    pygame.draw.rect(screen, BLACK, (45, 45, 5, 525))
    pygame.draw.polygon(screen, BLACK, [(47, 580), (40, 570), (55, 570)])
    pygame.draw.rect(screen, LIGHT_GREY, (50, 50, 700, 500))

    pygame.draw.rect(screen, BLACK, (850, 50, 50, 50))
    screen.blit(create_text_render("+"), (863, 45))
    pygame.draw.rect(screen, BLACK, (950, 50, 50, 50))
    screen.blit(create_text_render("-"), (968, 42))
    screen.blit(create_text_render("K = " + str(K)), (1050, 45))
    pygame.draw.rect(screen, BLACK, (850, 125, 150, 50))
    screen.blit(create_text_render("RUN"), (882, 120))
    pygame.draw.rect(screen, BLACK, (850, 200, 150, 50))
    screen.blit(create_text_render("RND"), (882, 195))
    pygame.draw.rect(screen, BLACK, (850, 275, 150, 50))
    screen.blit(create_text_render("ALGO"), (869, 270))
    pygame.draw.rect(screen, BLACK, (850, 350, 150, 50))
    screen.blit(create_text_render("RESET"), (857, 345))

    if 50 < mouse_x < 750 and 50 < mouse_y < 550:
        screen.blit(
            create_text_render(
                "(" + str(mouse_x - 50) + ", " + str(mouse_y - 50) + ")", 20, BLACK
            ),
            (mouse_x + 20, mouse_y + 20),
        )

    if 850 < mouse_x < 1000 and 275 < mouse_y < 325:
        screen.blit(
            create_text_render("Using Kmeans provided by scikit-learn", 20, YELLOW),
            (785, 250),
        )


running = True

while running == True:
    pygame.time.Clock().tick(60)
    screen.fill(BACKGROUND)

    mouse_x, mouse_y = pygame.mouse.get_pos()

    draw_interface()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if 50 < mouse_x < 750 and 50 < mouse_y < 550:
                labels = []
                point = [mouse_x - 50, mouse_y - 50]
                points.append(point)

            if 850 < mouse_x < 900 and 50 < mouse_y < 100:
                if K < 9:
                    K += 1

            if 950 < mouse_x < 1000 and 50 < mouse_y < 100:
                if K > 0:
                    K -= 1

            if 850 < mouse_x < 1000 and 125 < mouse_y < 175:
                labels = []
                distances_to_cluster = []

                if clusters == []:
                    continue

                for p in points:
                    for c in clusters:
                        dis = distance(p, c)
                        distances_to_cluster.append(dis)

                    min_dis = min(distances_to_cluster)
                    label = distances_to_cluster.index(min_dis)
                    labels.append(label)
                    distances_to_cluster.clear()

                for i in range(K):
                    sum_i, sum_j, cnt = 0, 0, 0
                    for j in range(len(points)):
                        if labels[j] == i:
                            sum_i += points[j][0]
                            sum_j += points[j][1]
                            cnt += 1
                    if cnt != 0:
                        new_cluster_i, new_cluster_j = sum_i / cnt, sum_j / cnt
                        clusters[i] = [new_cluster_i, new_cluster_j]

            if 850 < mouse_x < 1000 and 200 < mouse_y < 250:
                clusters = []
                for i in range(K):
                    random_cluster_point = [randint(10, 690), randint(10, 490)]
                    clusters.append(random_cluster_point)

            if 850 < mouse_x < 1000 and 275 < mouse_y < 325:
                if K > 0:
                    kmeans = KMeans(n_clusters=K).fit(points)
                    clusters = list(kmeans.cluster_centers_)
                    labels = list(kmeans.labels_)

            if 850 < mouse_x < 1000 and 350 < mouse_y < 400:
                K = 0
                points = []
                clusters = []
                labels = []
                error = 0

    for i in range(len(clusters)):
        pygame.draw.circle(
            screen, colors[i], (int(clusters[i][0]) + 50, int(clusters[i][1]) + 50), 10
        )

    for i in range(len(points)):
        pygame.draw.circle(screen, BLACK, (points[i][0] + 50, points[i][1] + 50), 6)
        if labels == []:
            pygame.draw.circle(screen, WHITE, (points[i][0] + 50, points[i][1] + 50), 5)
        else:
            pygame.draw.circle(
                screen, colors[labels[i]], (points[i][0] + 50, points[i][1] + 50), 5
            )

    error = 0
    if len(clusters) > 0 and len(labels) > 0:
        for i in range(len(points)):
            error += distance(points[i], clusters[labels[i]])

    screen.blit(create_text_render("ERROR = " + str(int(error))), (800, 450))

    pygame.display.flip()

pygame.quit()
