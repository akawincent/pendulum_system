# 使用指南

> 本工程使用python语言编写程序仿真模拟单摆系统、双摆系统、连杆系统等常见物理模型，通过数值求解算法对模型进行求解进而得到系统的运动情况，同时还探究了系统中不同参数对运动情况的影响。

### 工程依赖

- 系统为 `Windows10 64-bit`，其他系统上的兼容性未经过验证
- 需要安装 `python`，开发版本为3.10.2
- 需要安装 `numpy`，开发版本为 1.24.2
- 需要安装 `matplotlib`，开发版本为 3.5.1

### 使用方法

举个例子，在`codebase`文件夹目录下启动终端，键入下面的指令便可以运行python程序了

```powershell
python '.\undamped double pendulum\demo.py'
```

当然也可以选择在IDE下运行，开发时使用的IDE为`VsCode`

### 文件架构

- `System.py`       ***该文件是工程的核心代码文件。不同系统的数学模型以及数值求解方法都封装成了类，对外提供接口***

  - _Undamped_Pendulum_				     描述无阻尼单摆的类

  - _Damping_Pendulum_                         描述有阻尼单摆的类

  - _Damping_Rod_                                    描述有阻尼连杆的类

  - _Undamped_Double_Pendulum_        描述无阻尼双摆的类

    

- `damping pendulum`                    ***有阻尼单摆的仿真程序***
  
  - `graph of function.py`      	展示角度随着时间变化的函数曲线
  
  - `phase map.py`   				        展示系统的相位图
  
  - `theta_0 vary.py`                     探究初值的不同对系统运动的影响
  
    
  
- `damping rod`                               ***有阻尼连杆的仿真程序***
  
  - `graph of function.py`          展示角度随着时间变化的函数曲线
  
  - `k vary.py`                                 探究不同阻尼系数对系统运动的影响
  
  - `theta_0 vary.py`                    探究不同初值对系统运动的影响
  
    
  
- `undamped double pendulum`    ***无阻尼双摆的仿真程序***
  
  - `demo.py`                                    给出双摆系统运动的演示动画以及两个小球的相位图。
  
    
  
- `undamped pendulum`                 ***无阻尼单摆的仿真程序***
  
  - `graph of function.py`         展示角度随着时间变化的函数曲线
  - `delta_t vary.py`                   展示欧拉法求解步长对求解结果的影响。
  - `phase map.py `                         系统的相位图
  - `theta_0 vary.py`                   探究不同初值对系统运动的影响





