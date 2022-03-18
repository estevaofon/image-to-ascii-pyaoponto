import PIL.Image

class ImageToAscii:
    """Convert Image to Ascii"""
    def __init__(self):
        self.ASCII_CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", " "]
        self.ASCII_CHARS.reverse()
        self.new_width = 100

    def resize_image(self, image):
        """rezise image accordint to a new width"""
        width, height = image.size
        ratio = height / width
        new_height = int(self.new_width * ratio/2)
        self.resized_image = image.resize((self.new_width, new_height))
        return (self.resized_image)

    def grayify(self, image):
        """convert each pixel to grayscale"""
        self.grayscale_image = image.convert("L")
        return(self.grayscale_image)

    def pixels_to_ascii(self, image):
        """convert pixel to a string of ASCII character"""
        pixels = image.getdata()
        self.characters = "".join([self.ASCII_CHARS[pixel//25] for pixel in pixels])
        return(self.characters)

    def img_path(self, path):
        """Open from path"""
        try:
            image = PIL.Image.open(path)
        except FileNotFoundError:
            print(path, "is not a valid pathname")
            raise

        self.new_image_data = self.pixels_to_ascii(self.grayify(self.resize_image(image)))

        #format 
        pixel_count = len(self.new_image_data)
        self.ascii_image = "\n".join(
            self.new_image_data[i:(i+self.new_width)] for i in range(0, pixel_count, self.new_width))

    def plot(self):
        print(self.ascii_image)

    def save_to_file(self):    
        with open("ascii_image.txt", "w") as f:
            f.write(self.ascii_image)
        