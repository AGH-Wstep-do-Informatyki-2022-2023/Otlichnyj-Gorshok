class Util:

    def images_binder(self, path, img_list):
        bind_list = []
        for j in range(0, len(img_list)):
            img_list[j] = path + img_list[j]
        for i in range(0, len(img_list), 2):
            bind_list.append(img_list[i:i + 2])

        return bind_list
