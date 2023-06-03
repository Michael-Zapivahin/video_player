import json
import os

from livereload import Server

server = Server()


def on_reload():
    return


def main():
    on_reload()


if __name__ == '__main__':
    main()


server.watch('index.html', on_reload)
server.serve(root='.', default_filename='index.html')
