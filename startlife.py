from info import Info


class StartLife:
    life = Info()
    game = Info()
    game.draw_border()
    game.show_rules()
    game.show_gold()
    life.show_lives()
