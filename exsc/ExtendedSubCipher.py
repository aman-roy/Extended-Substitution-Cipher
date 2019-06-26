import random
import string


class ExtendedSubCipher:
	def __init__(self, key):
		self.__all_char = string.ascii_letters+string.digits+string.punctuation+" "
		self.__key_split(key)
		self.__list_of_random_lists = list()
		self.__generate_random_lists()

	def __key_split(self, key):
		try:
			self.__seed, self.__number_of_lists = key.split(".")
			self.__number_of_lists = int(self.__number_of_lists)
		except:
			raise Exception('Invalid key.\nValid key format: <seed:[int/float/string]>.<no_of_lists:[int]>')
 
	def __generate_random_lists(self):
		random.seed(self.__seed)
		for i in range(self.__number_of_lists):
			temp = list(self.__all_char)
			random.shuffle(temp)
			self.__list_of_random_lists.append(''.join(temp))


	def __substitute(self, lista, listb, c):
		try:
			return listb[lista.index(c)]
		except: 
			return c

	def encrypt(self, text):
		final=""
		for i, letter in enumerate(text):
			temp = self.__substitute(self.__all_char, self.__list_of_random_lists[i%self.__number_of_lists], letter)
			final += temp
		return final

	def decrypt(self, text):
		final=""
		for i, letter in enumerate(text):
			temp = self.__substitute(self.__list_of_random_lists[i%self.__number_of_lists], self.__all_char, letter)
			final += temp
		return final

	def update_key(self, key):
		self.__init__(key)
