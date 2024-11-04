# camera-porter

Program for fast media copying from flash with sorting.

## Разработка

Должен быть установлен Python и UI библиотека TKinter

## Сборка

Сначала установите PyInstaller через pip:

```sh
pip install pyinstaller
```

1. Перейдите в директорию со скриптом. Откройте терминал в папке, где находится ваш Python-скрипт, или используйте команду cd для навигации к нужной папке.

2. Запустите PyInstaller:

```sh
pyinstaller --onefile --windowed --icon=./icons/icon.icns camera-porter.py
```

--onefile — упаковывает все файлы в один исполняемый файл.
--windowed — скрывает консольное окно (рекомендуется для программ с GUI на Windows и macOS).
--icon — путь до иконки программы.

После завершения сборки появится новая папка dist, где будет находиться исполняемый файл.

Сборку под конкретную OS нужно выполнять на конкретной OS т.е. если вам нужна программа для Windows - запускайте сборку для windows.
