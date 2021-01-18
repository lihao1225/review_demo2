import yaml


class HandleYaml():

    def read_yaml(self, file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            data = yaml.load(f, Loader=yaml.FullLoader)
        return data

    def wirte_yaml(self, data, file_path):
        with open(file_path, "w") as f:
            yaml.dump(data, f, encoding="utf-8", allow_unicode=True)
