from service import convert_doc_to_pdf
from priority import PriorityQueue


def main():
    q = PriorityQueue()
    q.enqueue(("martin.docx", "martin"), 10)
    q.enqueue(("yaroslav.docx", "yaroslav"),10)
    q.enqueue(("oleg.docx", "oleg"), 10)
    q.enqueue(("oleksandra.docx", "oleksandra"), 5)
    q.enqueue(("Roman.docx", "Roman"), 1)

    while not q.is_empty():
        task = q.dequeue()
        result = convert_doc_to_pdf(*task)
        print(f"Done! task: {task}, result: {result}")


if __name__ == "__main__":
    main()
