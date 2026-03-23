#!/usr/bin/env python3
"""
获取鼠标位置的脚本
支持两种模式：
1. 实时打印模式：持续打印鼠标位置
2. 单次获取模式：获取一次后退出

注意：此脚本需要在有图形界面的环境中运行
"""

import sys

def get_mouse_position_pynput():
    """使用 pynput 库获取鼠标位置（跨平台）"""
    try:
        from pynput.mouse import Controller
        mouse = Controller()
        return mouse.position
    except ImportError:
        print("提示: 未找到 pynput 库")
        print("请运行: pip install pynput")
        return None
    except Exception as e:
        # 在没有显示器的环境中会出错
        return None

def get_mouse_position_pyautogui():
    """使用 pyautogui 库获取鼠标位置（跨平台）"""
    try:
        import pyautogui
        return pyautogui.position()
    except ImportError:
        print("提示: 未找到 pyautogui 库")
        print("请运行: pip install pyautogui")
        return None
    except Exception as e:
        # 在没有显示器的环境中会出错
        return None

def continuous_monitor():
    """持续监控并打印鼠标位置"""
    print("开始监控鼠标位置 (按 Ctrl+C 停止)...")
    print("-" * 40)
    
    try:
        last_pos = None
        while True:
            pos = get_mouse_position_pynput() or get_mouse_position_pyautogui()
            
            if pos:
                if pos != last_pos:
                    print(f"X: {pos[0]:4d}, Y: {pos[1]:4d}", end='\r')
                    last_pos = pos
            
            # 短暂休眠以减少 CPU 使用
            import time
            time.sleep(0.05)
            
    except KeyboardInterrupt:
        print("\n\n监控已停止")

def get_single_position():
    """获取单次鼠标位置"""
    pos = get_mouse_position_pynput() or get_mouse_position_pyautogui()
    
    if pos:
        print(f"当前鼠标位置: X={pos[0]}, Y={pos[1]}")
        return pos
    else:
        print("无法获取鼠标位置")
        return None

if __name__ == "__main__":
    print("=" * 40)
    print("鼠标位置获取脚本")
    print("=" * 40)
    
    # 检查参数
    if len(sys.argv) > 1 and sys.argv[1] == "--continuous":
        continuous_monitor()
    else:
        # 默认单次获取
        get_single_position()
        
        # 询问是否进入连续监控模式
        print("\n是否进入连续监控模式？(y/n): ", end='')
        try:
            response = input().strip().lower()
            if response in ['y', 'yes', '是']:
                continuous_monitor()
        except EOFError:
            pass
