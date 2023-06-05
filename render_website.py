import json
import os

from livereload import Server


def on_reload():
    return


def main():
    on_reload()
    server = Server()
    server.watch('index.html', on_reload)
    server.serve(root='.', default_filename='index.html')


if __name__ == '__main__':
    main()



