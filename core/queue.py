QUEUE = {}

def add_to_queue(chat_id, track):
    if chat_id not in QUEUE:
        QUEUE[chat_id] = []

    QUEUE[chat_id].append(track)

def get_queue(chat_id):
    return QUEUE.get(chat_id, [])

def pop_queue(chat_id):
    if chat_id in QUEUE and QUEUE[chat_id]:
        return QUEUE[chat_id].pop(0)

    return None

def clear_queue(chat_id):
    if chat_id in QUEUE:
        QUEUE[chat_id] = []
