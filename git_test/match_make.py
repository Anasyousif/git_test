from queue import Queue


def matchmake(queue, user):
    name,action = user
    if action == "leave":
        if name in queue.items:
            queue.items.remove(name)
    elif action == "join":
        queue.push(name)

    if queue.size()>=4:
        user1 = queue.pop()
        user2 = queue.pop()
        return f"{user1} matched {user2}!"

    return "No match found"    
        
            
