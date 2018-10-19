import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType


login, password = 'login', 'pass'
vk_session = vk_api.VkApi(login, password)
vk_session.auth()
vk = vk_session.get_api()

#print(vk.wall.post(message='Hello world!'))
longpoll = VkLongPoll(vk_session)


for event in longpoll.listen():
   # if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text :
    if event.type == VkEventType.MESSAGE_NEW and event.to_me :
        print('id{}: "{}"'.format(event.peer_id, event.text), end=' ')

        vk.messages.send(
                    user_id=event.peer_id,
                    message='No results'
        )
