class Keyboard:
    def __init__(self):
        self.one_pressed = False
        self.zero_pressed = False

    def input_letter(self, letter):
        bin_str = '{:07b}'.format(ord(letter))
        for c in bin_str:
            if c == "0":
                self.zero_pressed = not self.zero_pressed
            else:
                self.one_pressed = not self.one_pressed
    def any_pressed(self):
        return self.one_pressed or self.zero_pressed

try:
    while True:
        line = input()
        # if line == "":
        #     break
        keyboard = Keyboard()
        for letter in line:
            keyboard.input_letter(letter)

        print("trapped" if keyboard.any_pressed() else "free")

except EOFError:
    pass
