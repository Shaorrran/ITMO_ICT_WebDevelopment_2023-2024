# Выводы

Работа с сокетами полезна как для понимания устройства работы веб-серверов, так и для общего образования в области устройства компьютерных сетей, и без базовых знаний сложно переходить к более высокоуровневым абстракциям. В целом, я научился работать с сокетами в Python.

Также нужно отметить работу с библиотекой `threading` для многопоточности в Python. Однако, работа с `threading` в Python сопряжена с определёнными трудностями не только из-за самой природы многопоточности, но и из-за устройства стандартного интерпретатора CPython, в частности, из-за Global Interpreter Lock. Разработчики обычно предпочитают `multiprocessing` или более высокоуровневые обёртки над ней, например, `joblib` (или используют `cython` для разработки, требующей снятия GIL).