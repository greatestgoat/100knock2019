import gzip
import json
import re 


def read_json(filename: str, title: str):
    with gzip.open(filename, "rt", "utf_8") as f:
        for line in f:
            json_data = json.loads(line)  # jsonデータを辞書型に変換
            if json_data['title'] == title:
                return json_data['text']


def file_name(text: str):
    text_list = text.split('\n')
    for line in text_list:
        if re.match(r'^.*?(ファイル|File):.*\]\]$', line):
            name = re.match(r'^.*?(File|ファイル):(.+?)\|.+$', line)
            print(name.group(1) + ' : ' + name.group(2))


def main():
    text = read_json("jawiki-country.json.gz", "イギリス")
    file_name(text)


if __name__ == '__main__':
    main()
