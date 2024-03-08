from PIL import ImageGrab, ImageDraw
from config import Config


def make_board(config: Config):
    pil_img = ImageGrab.grab(all_screens=False, xdisplay=None)
    width, height = pil_img.size
    game_img = pil_img.crop(config.get_corrected_offsets(width, height))
    draw = ImageDraw.Draw(game_img)

    for col in range(0, 6):
        for row in range(0, 6):
            draw.rectangle((8 + (164 * col), 8 + (32 * row), 8 + (164 * col) + 22, 8 + (32 * row) + 18), None,
                           '#e51212', 1)

    game_img.show()
