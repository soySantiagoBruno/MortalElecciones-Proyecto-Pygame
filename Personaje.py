import pygame

class Personaje:
    def __init__(self, player, x, y, flip, imagen_inactivo, attack_image, sound):
        self.player = player
        self.flip = flip
        
        # Cargar las imágenes de los personajes
        self.imagen_inactivo = pygame.image.load(imagen_inactivo).convert_alpha()

        # Uso scale para escalar la imágen y hacerla mas chica
        self.imagen_inactivo = pygame.transform.scale(
            self.imagen_inactivo,
            (self.imagen_inactivo.get_width() / 2.5, self.imagen_inactivo.get_height() / 2.5)
        )

        self.attack_image = pygame.image.load(attack_image).convert_alpha()
        # Uso scale para escalar la imágen y hacerla mas chica
        self.attack_image = pygame.transform.scale(
            self.attack_image,
            (self.attack_image.get_width() / 2.5, self.attack_image.get_height() / 2.5)
        )
        
        # Inicializar la imagen y el rectángulo
        self.image = self.imagen_inactivo
        self.rect = self.image.get_rect(center=(x, y))
        
        # Sonido del ataque
        self.attack_sound = sound
        
        # Atributos de movimiento, ataque, etc.
        self.attacking = False
        self.attack_cooldown = 0
        self.health = 100
        self.alive = True
        self.jump = False  # Aquí inicializas el atributo 'jump'
        self.vel_y = 0  # Velocidad de salto

    def move(self, screen_width, screen_height, target, round_over):
        SPEED = 10
        GRAVITY = 2
        dx = 0
        dy = 0

        key = pygame.key.get_pressed()
        if not self.attacking and self.alive and not round_over:

            # CONTROLES JUGADOR 1
            if self.player == 1:  # Player 1 controls
                if key[pygame.K_a]:  # Move left
                    dx = -SPEED
                if key[pygame.K_d]:  # Move right
                    dx = SPEED
                if key[pygame.K_r]:  # Attack
                    self.attack(target)
                if key[pygame.K_w] and not self.jump:  # Saltar
                    self.vel_y = -30  # Ajusta la altura del salto
                    self.jump = True

            # CONTROLES JUGADOR 2
            elif self.player == 2:
                if key[pygame.K_LEFT]:  # Move left
                    dx = -SPEED
                if key[pygame.K_RIGHT]:  # Move right
                    dx = SPEED
                if key[pygame.K_o]:  # Attack
                    self.attack(target)
                if key[pygame.K_UP] and not self.jump:  # Saltar
                    self.vel_y = -30  # Ajusta la altura del salto
                    self.jump = True

        # Aplicar gravedad
        dy += self.vel_y
        self.vel_y += GRAVITY  # Asegura que la gravedad se aplique

        # Asegurar que el jugador no se salga de la pantalla
        if self.rect.left + dx < 0:
            dx = -self.rect.left
        if self.rect.right + dx > screen_width:
            dx = screen_width - self.rect.right
        if self.rect.bottom + dy > screen_height - 110:  # Asegurar que no se caiga del escenario
            dy = screen_height - 110 - self.rect.bottom
            self.vel_y = 0
            self.jump = False  # El jugador ya no está saltando

        # Actualizar la posición
        self.rect.x += dx
        self.rect.y += dy

        # Hacer que los jugadores se enfrenten
        self.flip = target.rect.centerx < self.rect.centerx

        # Aplicar cooldown del ataque
        if self.attack_cooldown > 0:
            self.attack_cooldown -= 1

    def update(self):
        # Actualizar imagen según el estado
        if self.attacking:
            self.image = self.attack_image
        else:
            self.image = self.imagen_inactivo

        # Reiniciar estado de ataque después del cooldown
        if self.attack_cooldown == 0:
            self.attacking = False

        # Verificar si el jugador está muerto
        if self.health <= 0:
            self.alive = False

    def attack(self, target):
        if self.attack_cooldown == 0:
            self.attacking = True
            self.attack_cooldown = 20
            self.attack_sound.play()

            # Ajustamos el área de daño para que se alinee con la imagen del jugador
            # El tamaño del rectángulo de ataque dependerá del tamaño del jugador y la dirección en que está mirando

            attack_width = self.rect.width // 2  # El ancho del área de ataque es la mitad del jugador
            attack_height = self.rect.height // 2  # La altura del área de ataque es la mitad del jugador

            if self.flip:  # Si el jugador está mirando hacia la izquierda
                attack_rect = pygame.Rect(
                    self.rect.centerx - attack_width,  # El área de ataque estará a la izquierda
                    self.rect.top + 10,  # Ajuste de altura para alinearse con la imagen
                    attack_width,  # Ancho del área de ataque
                    attack_height  # Altura del área de ataque
                )
            else:  # Si el jugador está mirando hacia la derecha
                attack_rect = pygame.Rect(
                    self.rect.centerx,  # El área de ataque estará a la derecha
                    self.rect.top + 10,  # Ajuste de altura para alinearse con la imagen
                    attack_width,  # Ancho del área de ataque
                    attack_height  # Altura del área de ataque
                )

            # Verificar si el rectángulo de ataque colisiona con el rectángulo del objetivo
            if attack_rect.colliderect(target.rect):
                target.health -= 10  # Reducir la vida del objetivo



    def draw(self, surface):
        img = pygame.transform.flip(self.image, self.flip, False)
        surface.blit(img, self.rect)
