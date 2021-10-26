import sqlite3

class SQLighter:

    def __init__(self, database):
        """Подключаемся к БД и сохраняем курсор соединения"""
        self.connection = sqlite3.connect(database)
        self.cursor = self.connection.cursor()

    def post_exists(self, wall_id):
        """Проверяем, есть ли уже юзер в базе"""
        with self.connection:
            result = self.cursor.execute('SELECT * FROM `posts` WHERE `wall_id` = ?', (wall_id,)).fetchall()
            return bool(len(result))
            
    def add_post(self, post_id, owner_id, text, wall_id, attachment, stop):
        """Добавляем нового подписчика"""
        with self.connection:
            return self.cursor.execute("INSERT INTO `posts` (`post_id`, `owner_id`, `text`, `wall_id`, `attachment`, `stop_slovo`) VALUES(?,?,?,?,?,?)", (post_id, owner_id, text, wall_id, attachment, stop))