
from telebot.types import InlineKeyboardMarkup, ReplyKeyboardMarkup, InlineKeyboardButton

class Question:

    def __init__(self, text, answer_id, *options):
        self.__text = text
        self.__answer_id = answer_id
        self.options = options

    @property
    def get_text(self):
        return self.__text


    def gen_markup(self):
        markup = InlineKeyboardMarkup()
        markup.row_width = len(self.options)

        for i, option in enumerate(self.options):
            if i == self.__answer_id:
                markup.add(InlineKeyboardButton(option, callback_data='correct'))
            else:
                markup.add(InlineKeyboardButton(option, callback_data='wrong'))
        return markup

quiz_questions =  [
    Question("Как называется устройство, которое выполняет основные вычисления и операции в компьютере?", 1, "Северный мост", "Процессор (CPU)", "Жесткий диск (HDD)", "Оперативная память (RAM)" ),
    Question("Какая разрядность операционной системы позволяет использовать более 4 ГБ оперативной памяти?",3 , "16-битная","32-битная", "128-битная", "64-битная"),
    Question("Какой компонент компьютера отвечает за обработку графики и вывод изображения на экран?", 1, "Звуковая карта", "Видео карта", "Видео процессор", "Процессор"),
    Question("Чем отличается оперативная память (ОЗУ) от жесткого диска (HDD/SSD)?", 1, "ОЗУ хранит данные навсегда, а HDD/SSD – временно", "ОЗУ быстрее и очищается при выключении, HDD/SSD – медленнее, но хранит данные постоянно", "Никак не отличаются", "Нет правильного ответа"),
    Question("Как назывался первый программируемый компьютер, созданный в 1940-х годах?", 0, "ENIAC", "IBM PC", "Apple I","Altair 8800"),
    Question("Кто считается создателем первого алгоритма для вычислительной машины?",2 , "Билл Гейтс", "Алан Тьюринг", "Ада Лавлейс", "Стив Джобс"),
    Question("На какую тематику был веб сайт, который был запущен в 1991 году",2 , "Польза фруктов", "Компьютеры и их строение", "Сайты, и то как они созданы", "Реклама ресторана"),
    Question("Когда была выпущена первая версия операционной системы Windows?", 1, "1981", "1985", "1991", "1993"),
    Question("В каком году был анонсирован первый компьютерный вирус?", 1, "1981", "1986", "1992", "1996"),
    Question("Первым программистом мира является:",1 , "Б.Паскаль", "А.Лавлейс", "Г.Лейбниц", "А.Эйнштейн"),
    ]
