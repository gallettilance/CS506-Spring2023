def draw_road():
    def draw_tree(height):
        for i in range(1, height + 1):
            spaces = height - i
            stars = 2 * i - 1
            print(" " * spaces + "*" * stars)
        trunk_height = height // 4
        if trunk_height < 3:
            trunk_height = 3
        spaces = height - trunk_height
        print(" " * spaces + "####" * (trunk_height // 4))
    draw_tree()
    return
