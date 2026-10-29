import json


forlk = {
    "title": "ой чій то кінь стоїть",
    "genre": "пісня",
    "region": "Житомирщіна",
    "narrator": "народ",
    "year": 1600,
    "content": "ой чій то кінь стоїть, що сива гривонька",
    "tags": ["любов", "сім'я", "традиція"],
    "verified": True
}

# json_forlk = json.dumps(forlk, ensure_ascii=False, indent=4)

# forlk_py = json.loads(json_forlk)

# print(forlk_py)
# print(type(forlk_py))
# print(f'{forlk_py["title"]}, {forlk_py["genre"]}')


records = [
    {
        "title": "Ой у лузі червона калина",
        "genre": "пісня",
        "region": "Полтавщина",
        "narrator": "Ганна Остапенко",
        "year": 1932,
        "content": "Патріотична народна пісня",
        "tags": ["народна", "патріотична"],
        "verified": True
    },
    {
        "title": "Про лисицю та журавля",
        "genre": "казка",
        "region": "Поділля",
        "narrator": "Петро Коваль",
        "year": 1956,
        "content": "Казка про хитру лисицю та журавля",
        "tags": ["тварини", "мораль"],
        "verified": True
    },
    {
        "title": "Де згода, там і перемога",
        "genre": "прислів'я",
        "region": "Харківщина",
        "narrator": "Марія Бондар",
        "year": 1974,
        "content": "Прислів'я про важливість єдності",
        "tags": ["мудрість", "згода"],
        "verified": False
    },
    {
        "title": "Легенда про криницю",
        "genre": "легенда",
        "region": "Київщина",
        "narrator": "Олена Шевченко",
        "year": 1968,
        "content": "Легенда про походження старої сільської криниці",
        "tags": ["легенда", "село"],
        "verified": True
    },
    {
        "title": "Ой ходила дівчина бережком",
        "genre": "пісня",
        "region": "Львівщина",
        "narrator": "Іван Мельник",
        "year": 1948,
        "content": "Народна пісня про дівчину та її кохання",
        "tags": ["кохання", "народна"],
        "verified": False
    }
]

with open("folklore_archive.json", "w", encoding= "utf-8") as file:
    json.dump(records, file, indent = 4, ensure_ascii = False)

with open("folklore_archive.json", "r", encoding="utf-8") as file:
    json_records = json.load(file)

print(len(json_records))

for number, i in enumerate(json_records):
    print(f'{number+1}. {i["title"]}, ({i["genre"]}, {i["region"]})')


class FolkloreRecord:

    def __init__(self, title, genre, region, narrator, year, content, tags, verified):
        self.title = title
        self.genre = genre
        self.region = region
        self.narrator = narrator
        self.year = year
        self.content = content
        self.tags = tags
        self.verified = verified

    def to_dict(self):
        return {
            "title": self.title,
            "genre": self.genre,
            "region": self.region,
            "narrator": self.narrator,
            "year": self.year,
            "content": self.content,
            "tags": self.tags,
            "verified": self.verified 
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            title = data["title"],
            genre = data["genre"],
            region = data["region"],
            narrator = data["narrator"],
            year = data["year"],
            content = data["content"],
            tags = data["tags"],
            verified = data["verified"]
        )

    def __str__(self):
        return f"[{self.genre}] {self.title} - {self.region}, {self.year} (оповідач: {self.narrator})"

object1 = FolkloreRecord(
    "Чом ти не прийшов",
    "пісня",
    "Харків",
    "Софія Красива",
    1700,
    "Чом ти не прийшов, як місяць узійшов ...",
    ["любов", "сім`я"],
    True
    )
object2 = FolkloreRecord(
    "Про лисицю та журавля",
    "казка",
    "Поділля",
    "Петро Коваль",
    1956,
    "Казка про хитру лисицю та журавля",
    ["тварини", "мораль"],
    True
)

object3 = FolkloreRecord(
    "Легенда про криницю",
    "легенда",
    "Київщина",
    "Олена Шевченко",
    1968,
    "Легенда про походження старої сільської криниці",
    ["легенда", "село"],
    True
)

print(object3)

records_objects = [object1, object2, object3]
dict_records = []

for i in records_objects:
    dict_records.append(i.to_dict())

with open("folklore_archive.json", "w", encoding = "utf-8") as file:
    json.dump(dict_records, file, indent=4, ensure_ascii=False)

with open("folklore_archive.json", "r", encoding = "utf-8") as file:
    json_records = json.load(file)

new_record = []

for i in json_records:
    new_record.append(FolkloreRecord.from_dict(i))

for i in new_record:
    print(i.__str__())

class FieldExpedition:
    def __init__(self, expedition_id, researcher, location, date):
        self.expedition_id = expedition_id
        self.researcher = researcher
        self.location = location
        self.date = date
        self.records = []
        

    def add_record(self,record):
        for i in self.records:
            if i.title == record.title:
                return f"Запис '{record.title}' вже є в експедиції"
        self.records.append(record)

    def remove_record(self,title):
        for i in self.records:
            if i.title == title:
                self.records.remove(i)
                return
        return f"Запис '{title}' не знайдено"

    def find_by_genre(self, genre):
        genre_list = []
        for i in self.records:
            if i.genre == genre:
                genre_list.append(i)
                    
        return genre_list

    def to_dict(self):

        list_dict =[]
        for i in self.records:
            list_dict.append(i.to_dict())

        return {
            "expedition_id": self.expedition_id,
            "researcher": self.researcher,
            "location": self.location,
            "date": self.date,
            "records": list_dict
        }
    @classmethod
    def from_dict(cls, data):
        expedition = cls(
            data["expedition_id"],
            data["researcher"],
            data["location"],
            data["date"]
        )

        for i in data["records"]:
            record = FolkloreRecord.from_dict(i)
            expedition.add_record(record)

        return expedition

    def save(self, filepath):
        with open(filepath, "w", encoding="utf-8") as file:
            json.dump(
                self.to_dict(),
                file,
                indent=4,
                ensure_ascii=False
            )

    @classmethod
    def load(cls, filepath):
        try:
            with open(filepath, "r", encoding="utf-8") as file:
                data = json.load(file)

            return cls.from_dict(data)

        except FileNotFoundError:
            print(f"Файл '{filepath}' не знайдено")

        except json.JSONDecodeError:
            print(f"Файл '{filepath}' містить некоректний JSON")

expedition = FieldExpedition(
    1,
    "Сергій Загоруйко",
    "Харківщина",
    "2026-09-05"
)

expedition.add_record(object1)
expedition.add_record(object2)
expedition.add_record(object3)

expedition.save("expedition.json")

new_expedition = FieldExpedition.load("expedition.json")

songs = new_expedition.find_by_genre("пісня")

for i in songs:
    print(i)

new_expedition.remove_record("Про лисицю та журавля")

new_expedition.save("expedition.json")


def merge_archives(filepaths):
    all_records = []

    for filepath in filepaths:
        try:
            expedition = FieldExpedition.load(filepath)

            if expedition is not None:
                all_records.extend(expedition.records)

        except (FileNotFoundError, json.JSONDecodeError):
            print(f"Попередження: файл '{filepath}' пропущено")

    return all_records


def filter_records(records, genre=None, region=None, verified=None):
    result = []

    for i in records:
        if genre is not None and i.genre != genre:
            continue

        if region is not None and i.region != region:
            continue

        if verified is not None and i.verified != verified:
            continue

        result.append(i)

    return result


def export_summary(records, filepath):
    summary = []

    for i in records:
        summary.append({
            "title": i.title,
            "genre": i.genre,
            "region": i.region,
            "verified": i.verified
        })

    with open(filepath, "w", encoding="utf-8") as file:
        json.dump(
            summary,
            file,
            indent=4,
            ensure_ascii=False
        )


expedition1 = FieldExpedition(
    1,
    "Сергій",
    "Харківщина",
    "2026-09-01"
)

expedition1.add_record(object1)
expedition1.add_record(object2)

expedition2 = FieldExpedition(
    2,
    "Іван",
    "Полтавщина",
    "2026-09-02"
)

expedition2.add_record(object3)


expedition1.save("expedition1.json")
expedition2.save("expedition2.json")

all_records = merge_archives([
    "expedition1.json",
    "expedition2.json"
])

filtered_records = filter_records(
    all_records,
    region="Харківщина",
    verified=True
)

for i in filtered_records:
    print(i)

export_summary(
    filtered_records,
    "summary.json"
)
