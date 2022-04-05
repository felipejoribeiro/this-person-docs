# Personal WIKI
Here resides all information concerning software development acquired through the ages. This include knowledge about web development, linux, information security and other related topics. The material is composed by notes that are scattered through directories and subdirectories organized by topic. 

![library](./data/books.png)

All files are in **MarkDown** format which is a lightweight markup language that allows plain text formating. The reason for it was that these plain text files are easily searchable with fuzzy finders and grep commands, which makes information queries really easy by grep commands.

An example for this was made when configuring **rofi** to search for these notes. This was made with a simple `bash` command:

```bash
ls -R ~/notes | grep -v README | grep .md | sed "s/;/ /g" | rofi -dmenu -p "Open"
```

Which open the chosen note in **Neovim** for editing or reading. And it's possible to convert these notes to `PDF` as well if required with **Pandoc**:

![gif](./data/rofi.gif)

The dot files are located in this [Repo](https://github.com/felipejoribeiro/my-dev-environment).

## Table of contents
Here goes all subjects and files that are present in the repo:

- [Arch linux](https://github.com/felipejoribeiro/this-person-docs/tree/main/linux)
- [React](https://github.com/felipejoribeiro/this-person-docs/tree/main/programming/webdev/frontend/react)
- [React-native](https://github.com/felipejoribeiro/this-person-docs/tree/main/programming/mobile/react-native)
- [flask](https://github.com/felipejoribeiro/this-person-docs/tree/main/programming/webdev/backend/flask)
- [Node](https://github.com/felipejoribeiro/this-person-docs/tree/main/programming/webdev/backend/node_js)
- [Git](https://github.com/felipejoribeiro/this-person-docs/tree/main/programming/tools/git)
- [Nvim](https://github.com/felipejoribeiro/this-person-docs/tree/main/programming/tools/nvim)
- [PostgreSQL](https://github.com/felipejoribeiro/this-person-docs/tree/main/programming/webdev/backend/PostgreSQL)

## Authorship
All words here were written by myself and were based in a multitude of fonts that range from `Youtube` videos to `books` and academic `articles`. But, as these notes are intended for personal usage, rarely these fonts are mentioned in the text, only when strictly necessary for future research.

## Contributing
If you whish to contribute fell free to send a pull request. New information, revisions or corrections are highly welcome and appreciated.

## Licenses
[MIT](https://github.com/felipejoribeiro/this-person-docs/blob/main/LICENSE)
