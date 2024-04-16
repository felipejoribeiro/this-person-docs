# Rofi
Here we will see how to configure a rofi menu for any task.

```bash
#!/bin/bash

choice="$(ls -R ~/notes | grep -v README | grep .md | sed "s/;/ /g" | rofi -dmenu -p "Open")"

if [[ -z $choice ]];then
	echo "Nothing chosen"
else
	file=$(find ~/notes/ -name $choice)
	alacritty -e nvim "$file"&
fi
```

In this example we created a bash script that calls rofi. It will take the elements piped to it and display for us to chose one. The chosen element is then returned as text. So on the line bellow we can find the file by name and edit it with neovim.
For simple `Query` like this, that one command to call `Rofi` is good enough. But if you want to set shortcuts and other things, then a python script would be better.
