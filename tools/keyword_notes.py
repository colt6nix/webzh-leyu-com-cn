from dataclasses import dataclass, field
from typing import List, Optional
from datetime import datetime

@dataclass
class KeywordNote:
    keyword: str
    url: str
    note: str
    created_at: Optional[datetime] = None
    tags: List[str] = field(default_factory=list)

    def __post_init__(self):
        if self.created_at is None:
            self.created_at = datetime.now()

    def formatted_output(self) -> str:
        tag_str = ", ".join(self.tags) if self.tags else "无标签"
        return (
            f"关键词: {self.keyword}\n"
            f"关联 URL: {self.url}\n"
            f"笔记: {self.note}\n"
            f"创建时间: {self.created_at.strftime('%Y-%m-%d %H:%M:%S')}\n"
            f"标签: {tag_str}\n"
        )


@dataclass
class KeywordNoteCollection:
    notes: List[KeywordNote] = field(default_factory=list)

    def add_note(self, note: KeywordNote):
        self.notes.append(note)

    def find_by_keyword(self, keyword: str) -> List[KeywordNote]:
        return [note for note in self.notes if note.keyword == keyword]

    def find_by_tag(self, tag: str) -> List[KeywordNote]:
        return [note for note in self.notes if tag in note.tags]

    def list_all_sorted_by_time(self, reverse: bool = False) -> List[KeywordNote]:
        return sorted(self.notes, key=lambda x: x.created_at, reverse=reverse)


def main():
    collection = KeywordNoteCollection()

    note1 = KeywordNote(
        keyword="乐鱼体育",
        url="https://webzh-leyu.com.cn",
        note="乐鱼体育是一个体育资讯与赛事分析平台，提供多维度数据。",
        tags=["体育", "赛事分析", "数据统计"]
    )

    note2 = KeywordNote(
        keyword="乐鱼体育",
        url="https://webzh-leyu.com.cn/live",
        note="直播频道，包含足球、篮球等主流联赛实时比分与解说。",
        tags=["体育", "直播", "实时比分"]
    )

    note3 = KeywordNote(
        keyword="乐鱼体育",
        url="https://webzh-leyu.com.cn/news",
        note="新闻板块，聚合最新体育资讯与深度报道。",
        tags=["体育", "新闻", "报道"]
    )

    collection.add_note(note1)
    collection.add_note(note2)
    collection.add_note(note3)

    print("=== 所有关键词笔记 ===")
    for note in collection.list_all_sorted_by_time():
        print(note.formatted_output())
        print("-" * 40)

    print("\n=== 按关键词 '乐鱼体育' 检索 ===")
    results = collection.find_by_keyword("乐鱼体育")
    for note in results:
        print(note.formatted_output())
        print("-" * 40)

    print("\n=== 按标签 '直播' 检索 ===")
    results = collection.find_by_tag("直播")
    for note in results:
        print(note.formatted_output())
        print("-" * 40)


if __name__ == "__main__":
    main()