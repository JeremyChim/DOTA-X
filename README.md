<p align="center"><img src="img\logo.png" width="200"/></p>
<h1 align="center">DOTA-X</h1>
<p align="center">
    <img alt="Static Badge" src="https://img.shields.io/badge/Auth-Jeremy-brightgreen">
    <img alt="Static Badge" src="https://img.shields.io/badge/Version-v1.0.0-blue">
    <img alt="Static Badge" src="https://img.shields.io/badge/EnjoyDota-pink">
</p>

## ☕介绍

使用DOTA-X可以识别和修改DOTA2中的英雄和单位数据，并应用至游戏内。

## 🌭安装

### 1、新建文件夹mod

路径：…/SteamLibrary/steamapps/common/dota 2 beta/game/dota/mod

### 2、改gameinfo.gi

路径：…/SteamLibrary/steamapps/common/dota 2 beta/game/dota/gameinfo.gi

```textile
37        // *LANGUAGE* will be replaced with the actual language name. If not running a specific language, these paths will not be mounted
38        Game                 mod
39        Game_Language        dota_*LANGUAGE*
```

### 3、找到pak01_dir.vpk，拉出npc数据文件

路径：…/SteamLibrary/steamapps/common/dota 2 beta/game/dota/pak01_dir.vpk/scripts/npc

- npc_abilities.txt

- npc_heroes.txt

- npc_units.txt

### 4、下载VPK文件夹

```batch
vpk.exe pak01_dir
move "pak01_dir.vpk" "E:\GamePlatform\Steam\steamapps\common\dota 2 beta\game\mod"
@pause
```

### 5、下载饰品MOD

[DotaThoughts - YouTube](https://www.youtube.com/@Dota2oughts)

[(2) YopiDota2 - YouTube](https://www.youtube.com/@YopiDota2)

[(2) Satjakul - YouTube](https://www.youtube.com/@Satjakul)

### 6、steam启动项

```
-novid -prewarm -high -map dota -nod3d9ex -nohltv -novr -nojoy 
```

## 🍕使用

### 1、运行 app.py 或者 DOTA-X.exe

<img src="img\py.png"/>
<br>
<img src="img\exe.png"/>

### 2、主界面

<img src="img\win.png"/>

### 3、运行script.bat

<img src="img\cmd.png"/>

### 4、运行 DOTA2

Enjoy Dota🥂

## 🍦联系

GitHub：[JeremyChim (github.com)](https://github.com/JeremyChim)

E-Mail：[jer888chim@outlook.com](mailto:jer888chim@outlook.com)
