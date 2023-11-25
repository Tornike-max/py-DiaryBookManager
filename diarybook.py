class Diary:
    last_id = 0

    def __init__(self, memo, tags=' '):
        self.memo = memo
        self.tags = tags
        Diary.last_id += 1
        self.id = Diary.last_id

    def match(self, keyword):
        return keyword in self.memo or keyword in self.tags


class DiaryBook:
    def __init__(self):
        self.diaries = []

    def new_diary(self, memo, tags=''):
        self.diaries.append(Diary(memo, tags))

    def search_diary(self, keyword):
        filtered_diaries = []
        for diary in self.diaries:
            if diary.match(keyword):
                filtered_diaries.append(diary)
            return filtered_diaries
