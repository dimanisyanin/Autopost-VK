from post import main
import logging
import traceback

logging.basicConfig(level=logging.INFO)

class post:
    def posts():
        while True:
            try:
                main()
            except Exception as e:
                return 'Ошибка:\n' + traceback.format_exc()

#if __name__ == '__main__':
#    post.posts()