import json


class Config:
    offset_right: int
    offset_left: int
    offset_top: int
    offset_bottom: int
    monitor_amount: int
    monitor_with_game: int

    def __init__(self, cfg_file: str):
        with open(cfg_file) as f:
            data = json.load(f)
            self.offset_top = data['offsets']['top']
            self.offset_bottom = data['offsets']['bottom']
            self.offset_left = data['offsets']['left']
            self.offset_right = data['offsets']['right']
            self.monitor_amount = data['monitor_amount']
            self.monitor_with_game = data['monitor_with_game']

    def __str__(self):
        return f'offset_top: {self.offset_top}, offset_bottom: {self.offset_bottom}, offset_left: {self.offset_left}, offset_right: {self.offset_right}, monitor_amount: {self.monitor_amount}, monitor_with_game: {self.monitor_with_game}'

    def get_corrected_offsets(self, width, height) -> tuple[int, int, int, int]:
        return (width / self.monitor_amount)*(self.monitor_with_game-1) + self.offset_left, self.offset_top, (width/self.monitor_amount)*self.monitor_with_game - self.offset_right, height - self.offset_bottom
