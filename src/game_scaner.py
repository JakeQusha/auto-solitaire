import copy

from PIL import ImageGrab, ImageDraw, Image
from src.definitions import Config, CardType, Card, Game


def check_pixel_white(image: Image, x: int, y: int) -> bool:
    return image.getpixel((x, y)) == (255, 255, 255)


def get_card(image: Image, x: int, y: int) -> Card:
    # phase 1
    # T-thing
    if check_pixel_white(image, x + 6, y + 4):
        return Card(CardType.T_THING)
    # Queen
    if check_pixel_white(image, x + 14, y + 12):
        return Card(CardType.QUEEN)
    # 10
    if check_pixel_white(image, x + 4, y + 10):
        return Card(CardType.TEN)
    # phase 2
    # King
    if check_pixel_white(image, x + 14, y + 14):
        return Card(CardType.KING)
    # Jack
    if check_pixel_white(image, x + 4, y + 12):
        return Card(CardType.JACK)
    # 7
    if check_pixel_white(image, x + 6, y + 10):
        return Card(CardType.SEVEN)
    # phase 3
    # 9
    if check_pixel_white(image, x + 12, y + 8):
        return Card(CardType.NINE)
    # 6
    if check_pixel_white(image, x, y + 8):
        return Card(CardType.SIX)
    # else
    # 8
    return Card(CardType.EIGHT)


def make_board(config: Config, dbg=False) -> Game:
    pil_img = ImageGrab.grab(all_screens=False, xdisplay=None)
    width, height = pil_img.size
    game_img = pil_img.crop(config.get_corrected_offsets(width, height))
    if dbg:
        draw_game = copy.deepcopy(game_img)
        draw = ImageDraw.Draw(draw_game)
    game = Game()
    for col in range(0, 6):
        for row in range(0, 6):
            x = 8 + (164 * col)
            y = 8 + (32 * row)
            game.add_card(get_card(game_img, x, y), col)
            if dbg:
                draw.rectangle((x, y, x + 22, y + 18), None, '#e51212', 1)
    if dbg:
        for col in range(0, 6):
            for row in range(0, 6):
                print(f'col: {col} , row: {row}: {game.cards[col][row].type}')
        draw.rectangle(config.get_corrected_offsets(width, height), None, '#e11212', 1)
        draw_game.show()
    return game


if __name__ == "__main__":
    config = Config('../config.json')
    print(config)
    make_board(config, True)
