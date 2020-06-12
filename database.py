import sqlite3

class Database:
	"""docstring for Database"""
	
	def __init__(self, database_file):
		'''Подключение к БД и сохранение курсора соединения'''
		self.connection = sqlite3.connect(database_file)
		self.cursor = self.connection.cursor()

	def get_subscriptions(self, status = True):
		'''Получаем всех активных подписчиков бота'''
		with self.connection:
			return self.cursor.execute("SELECT * FROM `subscriptions` where `status` = ?",(status,)).fetchall()

	def subscriber_exists(self, user_id):
		'''Проверяет существование юзера в базе'''
		with self.connection:
			result = self.cursor.execute("SELECT * FROM `subscriptions` where `user_id` = ?", (user_id,)).fetchall()
			return bool(len(result))

	def add_subscriber(self, user_id, status = True):
		'''Добавляем нового подписчика'''
		with self.connection:
			return self.cursor.execute("INSERT INTO `subscriptions` (`user_id`, `status`) VALUES (?, ?)", (user_id, status))

	def update_subscription(self, user_id, status):
		'''Обновляем статус подписки'''
		with self.connection:
			return self.cursor.execute("UPDATE `subscriptions` SET `status` = ? WHERE `user_id` = ?", (status, user_id))

	def close(self):
		'''Закрываем соединение'''
		self.connection.close()
