import argparse
import os

from mhxy import *


class GameProcess:
    _moveOffset = (60, 20)

    def __moveZhuomianbanFunc(self, size):
        windows = pyautogui.getAllWindows()
        zhuomianban = (71, 964)
        i = 0
        for item in list(filter(lambda x: x.title.startswith("梦幻西游："), windows)):
            item.activate()
            log(item)
            if item.left < 0:
                log("notSafe")
            pyautogui.moveTo(item.right - resizeOffset[0], item.bottom - resizeOffset[1])
            pyautogui.dragTo(item.left + (size[0] - resizeOffset[0]), item.top + (size[1] - resizeOffset[1]),
                             duration=1)
            pyautogui.moveTo(item.left + self._moveOffset[0], item.top + self._moveOffset[1])
            cooldown(1)
            pyautogui.dragTo(zhuomianban[i] + self._moveOffset[0], 0 + self._moveOffset[1], duration=1)
            i += 1
            log("处理后：", item)

    def moveZhuomianbanVertical(self):
        windows = pyautogui.getAllWindows()
        zhuomianban = (0, 707 + 1)
        i = 0
        for item in list(filter(lambda x: x.title.startswith("梦幻西游："), windows)):
            item.activate()
            log(item)
            if item.left < 0:
                log("notSafe")
            pyautogui.moveTo(item.right - resizeOffset[0], item.bottom - resizeOffset[1])
            pyautogui.dragTo(item.left + (smallSize[0] - resizeOffset[0]), item.top + (smallSize[1] - resizeOffset[1]),
                             duration=1)
            pyautogui.moveTo(item.left + self._moveOffset[0], item.top + self._moveOffset[1])
            cooldown(1)
            pyautogui.dragTo(71 + self._moveOffset[0], zhuomianban[i] + self._moveOffset[1], duration=1)
            i += 1
            log("处理后：", item)

    def moveZhuomianban(self):
        self.__moveZhuomianbanFunc(smallSize)

    def moveZhuomianban2Origin(self):
        windows = pyautogui.getAllWindows()
        item = list(filter(lambda x: x.title.startswith("梦幻西游"), windows))[0]
        item.activate()
        log(item)
        pyautogui.moveTo(item.right - resizeOffset[0], item.bottom - resizeOffset[1])
        pyautogui.dragTo(item.left + (originSize[0] - resizeOffset[0]), item.top + (originSize[1] - resizeOffset[1]),
                         duration=1)
        cooldown(3)
        log("处理后：", item)

    def moveMoniqi(self):
        self.__moveMoniqiFunc(smallSize)

    def __moveMoniqiFunc(self, size):
        windows = pyautogui.getAllWindows()
        i = 0
        for item in list(filter(lambda x: x.title.startswith("MuMu模拟器12") or x.title.startswith("梦幻西游 - "), windows)):
            item.activate()
            log(item)
            if item.left < 0:
                log("notSafe")
            pyautogui.moveTo(item.right - 5, item.top + 15)
            pyautogui.dragTo(item.left + (size[0] - 5), item.top + 15,
                             duration=1)
            i += 1
            log("处理后：", item)


    def closeMoniqi(self):
        #根据进程名杀死进程 NemuPlayer.exe QtWebEngineProcess.exe NemuHeadless.exe || mymain.exe CCMini.exe
        pro = 'taskkill /f /im %s'% 'NemuHeadless.exe'
        os.system(pro)
        pro = 'taskkill /f /im %s'% 'QtWebEngineProcess.exe'
        os.system(pro)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='OF Generate')
    parser.add_argument('-d', '--direct', default='horizontal', type=str)
    parser.add_argument('--type', default='zhuomian', type=str)
    args = parser.parse_args()

    resize = GameProcess()
    if args.type == 'zhuomian':
        if args.direct == 'horizontal':
            resize.moveZhuomianban()
        else:
            resize.moveZhuomianbanVertical()
    else:
        resize.moveZhuomianban2Origin()
    # 模拟器分辨率设置为：1600*1095 再调整窗口大小可使用脚本
    # resize.moveMoniqi()
