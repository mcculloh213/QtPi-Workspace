import board as _b
import neopixel as _np


class QtPy(object):
    @property
    def BYTES_PER_PIXEL(self) -> int:
        """ The number of bytes to use when setting the color of the onboard NeoPixel. """
        return 3

    @property
    def NEOPIXEL_COLOR_CHANNEL_ORDER(self) -> str:
        """ The pixel color channel order of the onboard NeoPixel. """
        return _np.GRB

    @property
    def pixel(self) -> _np.NeoPixel:
        """
        The onboard NeoPixel.
        """
        return self.__pixel

    def show_pixel(self):
        """
        Calls the associated write function to display color changes of the onboard NeoPixel, if it is not set to
        automatically set the color when modified.
        """
        self.pixel.show()

    def set_pixel_color(self, red: int, green: int, blue: int, brightness: float = None):
        """
        Sets the color of the onboard NeoPixel using an RGB color.
        :param red: an 8-bit integer [0x00, 0xFF]
        :param green: an 8-bit integer [0x00, 0xFF]
        :param blue: an 8-bit integer [0x00, 0xFF]
        :param brightness: the brightness of the onboard NeoPixel [0.0, 1.0]
        """
        if brightness is not None:
            self.pixel.brightness = min(max(brightness, 0.0), 1.0)
        self.pixel.fill((red, green, blue))

    def set_pixel_color_hex(self, color: int, brightness: float = None):
        """
        Sets the color of the onboard NeoPixel using a 24-bit integer (0xBBGGRR).
        :param color: a 24-bit integer [0x000000, 0xFFFFFF]
        :param brightness: the brightness of the onboard NeoPixel [0.0, 1.0]
        """
        blue = (color & 0xFF0000) >> 16
        green = (color & 0x00FF00) >> 8
        red = (color & 0x0000FF) >> 0
        self.set_pixel_color(red, green, blue, brightness=brightness)

    def __init__(self, neopixel_brightness: float = 1.0, neopixel_auto_write: bool = True):
        """
        # Adafruit QT Py SAMD21 Development Board

        The `board` package will contain the following standard Pins:
          * 'A0', 'A1', 'A2','A3', 'A6', 'A7', 'A8','A9', 'A10'
          * 'D0', 'D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8', 'D9', 'D10'
          * 'I2C', 'STEMMA_I2C'
          * 'MISO', 'MOSI'
          * 'NEOPIXEL', 'NEOPIXEL_POWER'
          * 'TX', 'RX'
          * 'SCK', 'SCL', 'SDA', 'SPI', 'UART'

        :param neopixel_brightness: Brightness of the onboard NeoPixel; [0.0, 1.0] where 1.0 is full brightness
        :param neopixel_auto_write: True if the onboard NeoPixel should immediately change when set.
                                    If False,`show_pixel` must be called explicitly.
        """
        # noinspection PyUnresolvedReferences
        self.__pixel = _np.NeoPixel(_b.NEOPIXEL, 1, bpp=self.BYTES_PER_PIXEL, brightness=neopixel_brightness,
                                    auto_write=neopixel_auto_write, pixel_order=self.NEOPIXEL_COLOR_CHANNEL_ORDER)
