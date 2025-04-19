if snake.head.x == apple.x and snake.head.y == apple.y:
    score += apple.ves
    last = snake.body[0]
    new_block = pygame.Rect(last.x, last.y, BLOCK_SIZE, BLOCK_SIZE)
    snake.body.insert(0, new_block)
    apple.respawn()

    if score % 4 == 0:
        level += 1
        speed += 3 / 2
