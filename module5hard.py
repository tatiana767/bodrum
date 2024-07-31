'''Всего будет 3 класса: UrTube, Video, User.

Общее ТЗ:
Реализовать классы для взаимодействия с платформой, каждый из которых будет содержать методы добавления видео, авторизации и регистрации пользователя и т.д.

Подробное ТЗ:

Каждый объект класса User должен обладать следующими атрибутами и методами:
Атриубуты: nickname(имя пользователя, строка), password(в хэшированном виде, число), age(возраст, число)
Каждый объект класса Video должен обладать следующими атрибутами и методами:
Атриубуты: title(заголовок, строка), duration(продолжительность, секунды), time_now(секунда остановки (изначально 0)), adult_mode(ограничение по возрасту, bool (False по умолчанию))
Каждый объект класса UrTube должен обладать следующими атрибутами и методами:
 Атриубты: users(список объектов User), videos(список объектов Video), current_user(текущий пользователь, User)
Метод log_in, который принимает на вход аргументы: nickname, password и пытается найти пользователя в users с такими же логином и паролем. Если такой пользователь существует, то current_user меняется на найденного. Помните, что password передаётся в виде строки, а сравнивается по хэшу.
Метод register, который принимает три аргумента: nickname, password, age, и добавляет пользователя в список, если пользователя не существует (с таким же nickname). Если существует, выводит на экран: "Пользователь {nickname} уже существует". После регистрации, вход выполняется автоматически.
Метод log_out для сброса текущего пользователя на None.
Метод add, который принимает неограниченное кол-во объектов класса Video и все добавляет в videos, если с таким же названием видео ещё не существует. В противном случае ничего не происходит.
Метод get_videos, который принимает поисковое слово и возвращает список названий всех видео, содержащих поисковое слово. Следует учесть, что слово 'UrbaN' присутствует в строке 'Urban the best' (не учитывать регистр).
Метод watch_video, который принимает название фильма, если не находит точного совпадения(вплоть до пробела), то ничего не воспроизводится, если же находит - ведётся отчёт в консоль на какой секунде ведётся просмотр. После текущее время просмотра данного видео сбрасывается.
Для метода watch_video так же учитывайте следующие особенности:
Для паузы между выводами секунд воспроизведения можно использовать функцию sleep из модуля time.
Воспроизводить видео можно только тогда, когда пользователь вошёл в UrTube. В противном случае выводить в консоль надпись: "Войдите в аккаунт, чтобы смотреть видео"
Если видео найдено, следует учесть, что пользователю может быть отказано в просмотре, т.к. есть ограничения 18+. Должно выводиться сообщение: "Вам нет 18 лет, пожалуйста покиньте страницу"
После воспроизведения нужно выводить: "Конец видео"'''


class User:
    def __init__(self, nickname, password, age):
        """
        Класс пользователя содержащий логин и парооль
        :param username:
        :param password:
        :param password_confirmation:
        """
        self.nickname = nickname
        self.password = hash(password)
        self.age = age

class Video:

    def __init__(self, title, duration, time_now = 0, adult_mode = False ):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode
        #print(f'video object: {self.title}  {self.duration} ')



class urTube :

    videos = []
    users = []




    def __init__(self, Users=[], Videos=[], current_user='' ):
        self.users = list(*Users)
        self.videos = list(*Videos)
        self.current_user = current_user
        #print("users", self.users)
        #print("videos", self.videos)

    def  log_in(self, nickname, password):
      print()

    def log_out(self):
        self.current_user = None

    def register(self, nickname, password, age):
        e = 0
        for i in self.users:
           if i.nickname == nickname:
               print(f' пользователь {i.nickname} уже существует')
               e = 1
               break

        if e == 0:
            self.users.append(User(nickname, hash(password), age))
            self.current_user = User(nickname, hash(password), age)
            #print(self.users)



    def add(self, *Videos):

        #print(*Videos)
        for i in Videos:
                if self.videos.__contains__(i):
                    print('такое видео существует')
                else:
                    self.videos.append(i)

    def get_videos(self, title):
        c = []
        #print(len(self.videos))
        #print('ищем:', title)
        for i in self.videos:

            if str(i.title).upper().__contains__(title.upper()):
               # print(i.title, i.duration)
                c.append(i.title)
        return c

    def watch_video(self, title):
        for i in self.videos:

            if str(i.title) == title:
                #print(i.title, i.duration)
                if self.current_user != '':
                   if  i.adult_mode == True and self.current_user.age < 18 :
                            print('Вам нет 18 лет, пожалуйста покиньте страницу')
                   else:
                        from time import sleep as sleep

                        for i in range(0, i.duration):
                             print(i, end = ' ')
                             sleep(1)
                        print('конец видео')
                else:
                    print('Войдите в аккаунт, чтобы смотреть видео"')






if __name__ == '__main__':

    ur = urTube()
    v1 = Video('Лучший язык программирования 2024 года', 200)
    v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

    # Добавление видео
    ur.add(v1, v2)
   # print(ur.videos[0].title)
    print(ur.get_videos('Лучший'))
    print(ur.get_videos('ПРОГ'))
    # Проверка на вход пользователя и возрастное ограничение
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('vasya_pupkin', 'lolkekcheburek', 13)
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
    ur.watch_video('Для чего девушкам парень программист?')

    # Проверка входа в другой аккаунт
    ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
    print(ur.current_user.nickname)

    # Попытка воспроизведения несуществующего видео
    ur.watch_video('Лучший язык программирования 2024 года!')


'''['Лучший язык программирования 2024 года']
['Лучший язык программирования 2024 года', 'Для чего девушкам парень программист?']
Войдите в аккаунт, чтобы смотреть видео
Вам нет 18 лет, пожалуйста покиньте страницу
1 2 3 4 5 6 7 8 9 10 Конец видео
Пользователь vasya_pupkin уже существует
urban_pythonist
'''
