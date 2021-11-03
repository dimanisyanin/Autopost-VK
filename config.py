VK_API_STADALONE = ''
"""
Приложения создаются по ссылке https://vk.com/apps?act=manage
Инструкция по получению VK_API_STADALONE

Берём эту ссылку и подставляем вместо [CLIENT_ID] ID вашего приложения:

https://oauth.vk.com/authorize?client_id=[CLIENT_ID]&display=page&redirect_uri=https://oauth.vk.com/blank.html&scope=photos,wall,offline&response_type=token&v=5.131

Учтите, что приложение должно быть включено
"""
VK_API_USER = '' #https://vkhost.github.io/
VK_API_V = '5.131'
vk_group = ["-72685559", "-74761029", "-90634038", "-65269630", "-32493847", "-72378974"]
filter_wallGet = 'all'
count_wallGet = 10
extended_wallGet = 0
ownerId_wallPost = '-201637165' #ID группы
from_group_wallPost = 1
blacklist = ["#corsair ", "#corsair", "#palit ", "#palit", "#nvidia ", "#nvidia", "#Sapphire ", "#Sapphire", "#sapphire ", "#sapphire ", "@amdrussia"]
stop_list = ["GFN", "GFN.RU", "реклама", "Реклама", "Команда NVIDIA", "http", "club", ".ru", ".RU", ".com", ".COM", "пишите", "Видео", "видео", "ролик", "Ролик"]
TRANSPARENCY = 15
tSleep = 5
tSleep_for = 5
tSleep_post = 1728