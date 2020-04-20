from pygame import image, font
import logging
import os
import json

def list_resources(path):
    result = list()
    for r, _, f in os.walk(path):
        for name in f:
            subpath = os.path.join(r, name).split(path)[-1].replace("\\", "/")
            result.append(subpath)
    return result

class Resource:

    def __init__(self, filename):
        self.filename = filename
        self.instance = None

    def get_resource(self):
        raise NotImplementedError

class ImageResource(Resource):

    def __init__(self, filename, desired_size=None):
        super().__init__(filename)
        self.desired_size = desired_size

    def get_resource(self):
        if self.instance:
            return self.instance
        else:
            print(f"Instantiating ImageResource {self.filename}")
            self.instance = image.load("resources/images/" + self.filename)
            return self.instance


class FontResource(Resource):

    def __init__(self, filename, size):
        super().__init__(filename)
        self.size = size

    def get_resource(self):
        if self.instance:
            return self.instance
        else:
            print(f"Instantiating ImageResource {self.filename}")
            self.instance = font.Font("resources/fonts/" + self.filename, self.size)
            return self.instance

class ResourceManager:

    # TODO: Cargar todos los archivos de resources/images automáticamente
    resources = {
        "image": {resource: ImageResource(resource) for resource in list_resources("resources/images/")},
        "font": {
            "menu_large": FontResource("SourceCodePro-Bold.otf", 26),
            "menu_medium": FontResource("SourceCodePro-Regular.otf", 16),
            "menu_small": FontResource("SourceCodePro-Regular.otf", 12),
            "window_title": FontResource("SourceCodePro-Bold.otf", 14),
            "time": FontResource("SourceCodePro-Bold.otf", 18),
            "icon_name": FontResource("SourceCodePro-Bold.otf", 14),
            "status_name": FontResource("SourceCodePro-Bold.otf", 16),
            "status_desc": FontResource("SourceCodePro-Bold.otf", 12),
            "error": FontResource("SourceCodePro-Bold.otf", 32)
        }
    }

    def get_image(self, image):
        return ResourceManager.resources["image"][image].get_resource()

    def get_font(self, font):
        return ResourceManager.resources["font"][font].get_resource()

    def get_sound(self, sound):
        # TODO: Implementar para sonidos, y hacer clase SoundResource
        raise NotImplementedError

    def get_map(self, map_index):
        with open("resources/maps.json") as map_file:
            mapdata = json.loads(map_file.read())
            return mapdata["maps"][map_index]
