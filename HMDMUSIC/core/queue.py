queues = {}


def get_queue(chat_id):
    return queues.get(chat_id, [])


def clear_queue(chat_id):
    queues[chat_id] = []


def add_to_queue(chat_id, song):
    if chat_id not in queues:
        queues[chat_id] = []

    queues[chat_id].append(song)
