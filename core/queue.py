queues = {}

def add_to_queue(chat_id, song):
    if chat_id not in queues:
        queues[chat_id] = []

    queues[chat_id].append(song)


def get_queue(chat_id):
    return queues.get(chat_id, [])


def clear_queue(chat_id):
    if chat_id in queues:
        queues.pop(chat_id)


def pop_from_queue(chat_id):
    if chat_id in queues and queues[chat_id]:
        return queues[chat_id].pop(0)

    return None
